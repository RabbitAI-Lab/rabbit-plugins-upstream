#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill-distributor 主分发脚本
将技能包发布到 GitHub（单一事实源）并自动同步 ClawHub / MCP Registry / 腾讯 SkillHub / 镜像站。

用法:
  python distribute.py --skill <技能目录> [--tag v1.0.0] [--dry-run] [--skip github,clawhub,mcp,skillhub,mirror]

密钥来源（优先级）: 环境变量 > ~/.skill-distributor/secrets.json
支持的环境变量: GITHUB_TOKEN, CLAWHUB_AUTH, SKILLHUB_TOKEN, MIRROR_URLS
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

HOME_CONFIG_DIR = Path.home() / ".skill-distributor"
SECRETS_FILE = HOME_CONFIG_DIR / "secrets.json"

DEFAULT_CONFIG = {
    "github": {"owner": "", "repo": "", "private": True, "default_branch": "main"},
    "identity": {"name": "", "email": ""},
    "platforms": {
        "clawhub": {"enabled": True},
        "mcp_registry": {"enabled": True},
        "skillhub": {"enabled": True, "command": "skillhub publish"},
        "mirrors": {"enabled": False, "repos": []},
    },
}

EXCLUDE_DIRS = {".git", "__pycache__", ".skill-distributor", ".workbuddy"}
EXCLUDE_FILES = {"secrets.json"}


# ---------- 基础工具 ----------

def log(msg):
    print(f"[distribute] {msg}")


def robust_rmtree(path, retries=3, delay=1.0):
    """健壮删除目录：git 对象文件只读会使 Windows rmtree 失败，先清除只读位再带重试删除"""
    path = Path(path)
    if not path.exists():
        return True

    def _clear_readonly(root):
        for dirpath, _, filenames in os.walk(root):
            for f in filenames:
                try:
                    os.chmod(os.path.join(dirpath, f), 0o777)
                except OSError:
                    pass

    _clear_readonly(path)
    for i in range(retries):
        try:
            shutil.rmtree(path)
            return True
        except OSError:
            time.sleep(delay)
    # 仍失败：可能确有进程持有句柄，交给延迟清理兜底
    return not path.exists()


def schedule_late_cleanup(path, delay_sec=90):
    """rmtree 兜底仍失败时，派生独立进程延迟重删，脚本退出后也会继续清理"""
    path = Path(path)
    if not path.exists():
        return True
    if os.name == "nt":
        cmd = (f'start "" /b cmd /c "timeout /t {int(delay_sec)} /nobreak >nul & '
               f'rd /s /q \\"{path}\\""')
        subprocess.Popen(cmd, shell=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        return False
    import atexit
    atexit.register(lambda: shutil.rmtree(path, ignore_errors=True))
    return False


def run(cmd, cwd=None, check=True):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"命令失败: {' '.join(cmd)}\n{proc.stderr.strip()[:500]}")
    return proc


def merge_config(base, override):
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            merge_config(base[k], v)
        else:
            base[k] = v
    return base


def load_config(skill_dir):
    """配置优先级: 技能目录内 .skill-distributor/config.json > ~/.skill-distributor/config.json > 默认"""
    config = json.loads(json.dumps(DEFAULT_CONFIG))
    local_cfg = Path(skill_dir) / ".skill-distributor" / "config.json"
    candidates = []
    if local_cfg.exists():
        candidates.append(local_cfg)
    if HOME_CONFIG_DIR.joinpath("config.json").exists():
        candidates.append(HOME_CONFIG_DIR.joinpath("config.json"))
    for p in candidates:
        try:
            merge_config(config, json.loads(p.read_text(encoding="utf-8-sig")))
        except Exception as e:
            log(f"警告: 读取配置 {p} 失败: {e}")
    return config


def load_secret(name):
    """从环境变量或 secrets 文件读取密钥，绝不打印值"""
    val = os.environ.get(name)
    if val:
        return val
    if SECRETS_FILE.exists():
        try:
            data = json.loads(SECRETS_FILE.read_text(encoding="utf-8-sig"))
            return data.get(name, "")
        except Exception:
            return ""
    return ""


# ---------- 技能包校验 ----------

def parse_frontmatter(skill_dir):
    skill_md = Path(skill_dir) / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"错误: {skill_dir} 下没有 SKILL.md，不是有效技能包")
    text = skill_md.read_text(encoding="utf-8-sig")
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        raise SystemExit(f"错误: {skill_md} 缺少 YAML frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"\'')
    return fm, skill_md


def build_publish_copy(skill_dir, asset_dir, repo_name):
    """复制技能到临时目录作为发布副本，注入 release.yml 与 .gitignore"""
    tmp = Path(tempfile.mkdtemp(prefix="skill-dist-"))
    dest = tmp / repo_name
    dest.mkdir(parents=True)

    for item in Path(skill_dir).iterdir():
        if item.name in EXCLUDE_DIRS or item.name in EXCLUDE_FILES:
            continue
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        else:
            shutil.copy2(item, target)
    # SKILL.md 去除 UTF-8 BOM，避免平台 YAML 解析异常
    dest_md = dest / "SKILL.md"
    if dest_md.exists() and dest_md.read_bytes()[:3] == b"\xef\xbb\xbf":
        dest_md.write_text(dest_md.read_text(encoding="utf-8-sig"), encoding="utf-8")

    wf_dir = dest / ".github" / "workflows"
    wf_dir.mkdir(parents=True, exist_ok=True)
    release_tpl = Path(asset_dir) / "release.yml"
    if release_tpl.exists():
        shutil.copy2(release_tpl, wf_dir / "release.yml")
    gitignore_tpl = Path(asset_dir) / ".gitignore.example"
    if gitignore_tpl.exists():
        shutil.copy2(gitignore_tpl, dest / ".gitignore")
    return dest


def inject_skillhub_meta(work_dir, repo_name, version, slug_override=""):
    """为发布副本的 SKILL.md 注入 SkillHub 所需 frontmatter 字段（源技能保持豆包规范）"""
    skill_md = Path(work_dir) / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8-sig")
    m = re.match(r"^(---\s*\n)(.*?)(\n---)", text, re.S)
    if not m:
        return
    head, body, tail = m.group(1), m.group(2), m.group(3)
    lines = body.splitlines()
    fields = {}
    for line in lines:
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"\'')
    add_lines = []
    slug_replaced = False
    if slug_override:
        # slug 已被平台封禁/占用时，覆盖为 config 指定的新 slug
        new_lines = []
        for line in lines:
            if line.startswith("slug:"):
                new_lines.append(f"slug: {slug_override}")
                slug_replaced = True
            else:
                new_lines.append(line)
        body = "\n".join(new_lines)
        if not slug_replaced:
            add_lines.append(f"slug: {slug_override}")
    elif "slug" not in fields:
        add_lines.append(f"slug: {repo_name}")
    if "displayName" not in fields:
        add_lines.append(f"displayName: {fields.get('name', repo_name)}")
    if "version" not in fields:
        add_lines.append(f"version: {version.lstrip('v')}")
    if "summary" not in fields:
        desc = fields.get("description", "") or ""
        summary = re.sub(r"[\"'#:]", "", desc.splitlines()[0])[:100] if desc else f"{repo_name} skill"
        add_lines.append(f"summary: {summary}")
    if not add_lines and not slug_replaced:
        return
    new_body = body.rstrip() + "\n" + "\n".join(add_lines)
    skill_md.write_text(head + new_body + tail, encoding="utf-8")
    log(f"已为 SkillHub 注入 frontmatter: {', '.join(l.split(':')[0] for l in add_lines) or ('slug: ' + slug_override)}")


# ---------- GitHub ----------

def setup_proxy(config):
    """从 config.proxy 或环境变量设置代理（供 GitHub API 与 git push 使用）"""
    proxy = (config.get("proxy", "") or os.environ.get("HTTPS_PROXY")
             or os.environ.get("https_proxy") or "")
    if proxy:
        os.environ["HTTPS_PROXY"] = proxy
        os.environ["HTTP_PROXY"] = proxy
        log(f"已启用代理: {proxy}")
    return proxy


def gh_request(method, url, token, body=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github+json")
    data = None
    if body is not None:
        req.add_header("Content-Type", "application/json")
        data = json.dumps(body).encode("utf-8")
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or ""
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})) if proxy else urllib.request.build_opener()
    try:
        with opener.open(req, data=data, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def ensure_git_identity(config, cwd):
    name = config["identity"].get("name") or run(["git", "config", "--global", "user.name"], check=False).stdout.strip()
    email = config["identity"].get("email") or run(["git", "config", "--global", "user.email"], check=False).stdout.strip()
    if not name or not email:
        raise SystemExit("错误: 缺少 git 身份。请在 config.json 的 identity 中填写 name/email，或执行 git config --global user.name/email")
    run(["git", "config", "user.name", name], cwd=cwd)
    run(["git", "config", "user.email", email], cwd=cwd)


def publish_github(config, token, work_dir, version, dry_run, force):
    owner = config["github"].get("owner", "")
    repo = config["github"].get("repo", "")
    branch = config["github"].get("default_branch", "main")
    private = config["github"].get("private", True)
    if not owner or not repo:
        if dry_run:
            log("警告: config.json 未填写 github.owner/repo（dry-run 不实际执行）")
        else:
            raise SystemExit("错误: config.json 需填写 github.owner 与 github.repo")
    if not token:
        if dry_run:
            log("警告: 未配置 GITHUB_TOKEN（dry-run 不实际执行）")
        else:
            raise SystemExit("错误: 缺少 GITHUB_TOKEN（环境变量或 secrets.json）")

    tag = f"v{version}" if not version.startswith("v") else version
    api = "https://api.github.com"
    if dry_run:
        log(f"[dry-run] 将创建（如不存在）GitHub 仓库 {owner}/{repo} (private={private})，推送代码并打 tag {tag}")
        return tag
    status, _ = gh_request("GET", f"{api}/repos/{owner}/{repo}", token)
    if status == 404:
        st, resp = gh_request("POST", f"{api}/user/repos", token,
                              {"name": repo, "private": private, "description": f"Skill distribution source: {repo}"})
        if st not in (200, 201):
            raise RuntimeError(f"创建仓库失败 ({st}): {resp}")
        log(f"已创建仓库 {owner}/{repo}")
    elif status != 200:
        raise RuntimeError(f"检查仓库失败 ({status}): 请确认 token 有 repo 权限")

    remote_url = f"https://{token}@github.com/{owner}/{repo}.git"
    clean_url = f"https://github.com/{owner}/{repo}.git"
    run(["git", "init", "-b", branch], cwd=work_dir)
    run(["git", "add", "-A"], cwd=work_dir)

    ensure_git_identity(config, work_dir)
    run(["git", "commit", "-m", f"release {tag}"], cwd=work_dir)
    run(["git", "remote", "remove", "origin"], cwd=work_dir, check=False)
    run(["git", "remote", "add", "origin", remote_url], cwd=work_dir)
    # main 以发布副本为准强制推送（本工具是唯一写入者），避免非快进被拒导致 main 长期陈旧
    run(["git", "push", "--force", "-u", "origin", branch], cwd=work_dir)
    # 打 tag（已存在则报错，可用 --force）
    tag_flag = ["--force"] if force else []
    proc = run(["git", "tag"] + tag_flag + [tag], cwd=work_dir, check=False)
    if proc.returncode != 0:
        run(["git", "fetch", "--tags", "origin"], cwd=work_dir, check=False)
        raise SystemExit(f"错误: tag {tag} 可能已存在。确认后用 --force 覆盖，或改用 --tag 指定新版本")
    run(["git", "push", "origin", tag], cwd=work_dir)
    # 移除 remote URL 中的 token，防止残留
    run(["git", "remote", "set-url", "origin", clean_url], cwd=work_dir)
    log(f"GitHub 发布完成: {clean_url} (tag {tag})")
    return tag


# ---------- 各平台 ----------

def run_cmd(exe, args, cwd, env=None):
    """执行命令；Windows 下对 .cmd/.bat/.ps1 包装经 cmd.exe /c 运行并正确处理带空格路径"""
    if exe.lower().endswith((".cmd", ".bat", ".ps1")):
        quoted = " ".join(f'"{a}"' if any(c.isspace() for c in a) else a for a in args)
        return subprocess.run(f'"{exe}" {quoted}', cwd=cwd, capture_output=True,
                              text=True, env=env or os.environ, shell=True)
    return subprocess.run([exe] + args, cwd=cwd, capture_output=True, text=True, env=env or os.environ)


def publish_clawhub(config, work_dir, tag, dry_run):
    exe = shutil.which("clawhub")
    if not exe:
        log("跳过 ClawHub: 未安装 clawhub CLI（npm install -g clawhub）")
        return
    pcfg = config["platforms"].get("clawhub", {})
    if not pcfg.get("enabled", True):
        return
    auth = load_secret("CLAWHUB_AUTH")
    if dry_run:
        log(f"[dry-run] clawhub skill publish . --version {tag.lstrip('v')}")
        return
    env = dict(os.environ)
    if auth:
        env["CLAWHUB_AUTH"] = auth
    args = ["skill", "publish", ".", "--version", tag.lstrip("v"), "--changelog", f"Release {tag}"]
    if pcfg.get("owner"):
        args += ["--owner", pcfg["owner"]]
    proc = run_cmd(exe, args, work_dir, env=env)
    if proc.returncode == 0:
        log("ClawHub 发布完成")
    else:
        log(f"ClawHub 发布失败（不影响其他平台）: {proc.stderr.strip()[:300]}")


def publish_mcp(work_dir, dry_run):
    if not (Path(work_dir) / "server.json").exists():
        log("跳过 MCP Registry: 技能包不含 server.json（非 MCP 工具型）")
        return
    if shutil.which("mcp-publisher") is None:
        log("跳过 MCP Registry: 未安装 mcp-publisher CLI")
        return
    if dry_run:
        log("[dry-run] mcp-publisher publish（需先 mcp-publisher login github 完成一次登录）")
        return
    proc = subprocess.run(["mcp-publisher", "publish"], cwd=work_dir, capture_output=True, text=True)
    if proc.returncode == 0:
        log("MCP Registry 发布完成")
    else:
        log(f"MCP Registry 发布失败（可稍后手动执行）: {proc.stderr.strip()[:300]}")


def publish_skillhub(config, work_dir, tag, dry_run):
    pcfg = config["platforms"].get("skillhub", {})
    if not pcfg.get("enabled", True):
        return
    command = pcfg.get("command", "skillhub publish").split()
    exe = shutil.which(command[0]) if command else None
    if not exe:
        log("跳过腾讯 SkillHub: 未找到 CLI（命令: " + " ".join(command) + "）")
        return
    if dry_run:
        log(f"[dry-run] {' '.join(command)} . --version {tag.lstrip('v')}（仅技能内容，排除 .git/.github/.gitignore）")
        return
    # SkillHub 只接受技能内容文件，递归排除所有点开头文件（.git/.github/.gitignore/.*.example）
    clean_dir = Path(tempfile.mkdtemp(prefix="skillhub-clean-"))

    def _skip_dots(directory, names):
        return {n for n in names if n.startswith(".")}

    try:
        for item in Path(work_dir).iterdir():
            if item.name.startswith("."):
                continue
            target = clean_dir / item.name
            if item.is_dir():
                shutil.copytree(item, target, ignore=_skip_dots)
            else:
                shutil.copy2(item, target)
        token = load_secret("SKILLHUB_TOKEN")
        env = dict(os.environ)
        if token:
            env["SKILLHUB_TOKEN"] = token
        args = command[1:] + [str(clean_dir), "--version", tag.lstrip("v")]
        if token:
            args += ["--token", token]
        proc = run_cmd(exe, args, work_dir, env=env)
        if proc.returncode == 0:
            log("腾讯 SkillHub 发布完成")
        else:
            log(f"腾讯 SkillHub 发布失败（不影响其他平台）: {proc.stderr.strip()[:300]}")
    finally:
        # SkillHub 干净副本位于系统缓存目录，发布后自动清理
        ok = robust_rmtree(clean_dir)
        if not ok:
            schedule_late_cleanup(clean_dir)
            log(f"SkillHub 临时副本被短暂占用，已排程延迟清理: {clean_dir}")
        else:
            log(f"已清理 SkillHub 临时副本: {clean_dir}")


def publish_mirrors(config, work_dir, dry_run):
    pcfg = config["platforms"].get("mirrors", {})
    if not pcfg.get("enabled", False):
        return
    repos = pcfg.get("repos", []) or (load_secret("MIRROR_URLS") or "").splitlines()
    if not repos:
        log("跳过镜像: mirrors.repos 为空")
        return
    for i, url in enumerate(repos):
        url = url.strip()
        if not url:
            continue
        if dry_run:
            log(f"[dry-run] push --mirror {url}")
            continue
        run(["git", "remote", "remove", f"mirror{i}"], cwd=work_dir, check=False)
        run(["git", "remote", "add", f"mirror{i}", url], cwd=work_dir)
        proc = run(["git", "push", "--mirror", f"mirror{i}"], cwd=work_dir, check=False)
        if proc.returncode == 0:
            log(f"镜像完成: {url}")
        else:
            log(f"镜像失败（不影响其他平台）: {url}")


# ---------- 主入口 ----------

def main():
    parser = argparse.ArgumentParser(description="技能分发: GitHub 单一事实源 + 多平台同步")
    parser.add_argument("--skill", required=True, help="技能目录（含 SKILL.md）")
    parser.add_argument("--tag", default="", help="版本 tag（如 v1.0.0，缺省读取 SKILL.md frontmatter 的 version）")
    parser.add_argument("--dry-run", action="store_true", help="只预览不执行")
    parser.add_argument("--force", action="store_true", help="允许覆盖已存在的 tag")
    parser.add_argument("--skip", default="", help="逗号分隔: github,clawhub,mcp,skillhub,mirror")
    args = parser.parse_args()

    skill_dir = Path(args.skill).resolve()
    if not skill_dir.is_dir():
        raise SystemExit(f"错误: 技能目录不存在 {skill_dir}")

    config = load_config(skill_dir)
    setup_proxy(config)
    skip = set(s.strip() for s in args.skip.split(",") if s.strip())

    fm, _ = parse_frontmatter(skill_dir)
    version = args.tag.lstrip("v") or str(config.get("version", "") or "") or fm.get("version", "0.1.0")

    skill_root = Path(__file__).resolve().parent.parent
    asset_dir = skill_root / "assets"
    repo_name = config["github"].get("repo") or skill_dir.name
    work_dir = build_publish_copy(skill_dir, asset_dir, repo_name)
    log(f"发布副本: {work_dir}")
    log(f"技能: {skill_dir.name} | 版本: {version}")
    try:
        if "skillhub" not in skip and config["platforms"].get("skillhub", {}).get("enabled", True):
            sh_slug = config["platforms"].get("skillhub", {}).get("slug", "")
            inject_skillhub_meta(work_dir, repo_name, version, sh_slug)

        tag = None
        if "github" not in skip:
            token = load_secret("GITHUB_TOKEN")
            tag = publish_github(config, token, work_dir, version, args.dry_run, args.force)
        else:
            log("跳过 GitHub（--skip github）")

        if "clawhub" not in skip:
            publish_clawhub(config, work_dir, tag or version, args.dry_run)
        if "mcp" not in skip:
            publish_mcp(work_dir, args.dry_run)
        if "skillhub" not in skip:
            publish_skillhub(config, work_dir, tag or version, args.dry_run)
        if "mirror" not in skip:
            publish_mirrors(config, work_dir, args.dry_run)

        if args.dry_run:
            log("dry-run 结束，未执行任何写操作。确认后去掉 --dry-run 执行。")
        else:
            log("全部分发动作完成。后续更新: 修改技能目录后重跑本命令，或在 GitHub 打 tag 由 release.yml 自动同步。")
    finally:
        # 发布副本位于系统缓存目录（tempfile.mkdtemp），发布完成后删除缓存根目录，不留残留
        tmp_root = work_dir.parent if work_dir.parent.name.startswith("skill-dist-") else work_dir
        ok = robust_rmtree(tmp_root)
        if not ok:
            schedule_late_cleanup(tmp_root)
            log(f"发布副本被短暂占用，已排程延迟清理: {tmp_root}")
        else:
            log(f"已清理发布副本: {tmp_root}")


if __name__ == "__main__":
    main()
