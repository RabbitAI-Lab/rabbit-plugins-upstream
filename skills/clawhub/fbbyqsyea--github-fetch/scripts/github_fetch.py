#!/usr/bin/env python3
"""github_fetch — 从 GitHub 拉取仓库/release 资产/单文件，直连优先，代理自动降级。

用法:
  # 下载单个 URL（release 资产 / raw 文件 / 归档）
  github_fetch.py <github-url> [--out DIR] [--extract] [--install DIR]
                  [--sha256 HEX] [--verify-url URL] [--timeout 20] [--min-speed 1M]

  # 查询最新 release 并匹配资产下载（--asset-pattern 正则，默认取第一个）
  github_fetch.py --release owner/repo [--tag latest] [--asset-pattern REGEX] [--out DIR]

  # clone 整个仓库（含子模块）
  github_fetch.py --clone owner/repo [--recursive] [--branch main] [--depth 1] [--out DIR]

环境变量:
  GITHUB_PROXIES   代理前缀列表（逗号分隔），覆盖默认镜像
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

DEFAULT_PROXIES = [
    "https://ghfast.top",
    "https://gh-proxy.com",
    "https://ghproxy.net",
    "https://gh.ddlc.top",
    "https://github.moeyy.xyz",
]


def _parse_speed(s: str) -> float:
    """把 1.5M / 800K / 1234 解析为字节/秒"""
    s = s.strip().upper()
    if s.endswith("K"):
        return float(s[:-1]) * 1024
    if s.endswith("M"):
        return float(s[:-1]) * 1048576
    if s.endswith("G"):
        return float(s[:-1]) * 1073741824
    try:
        return float(s)
    except ValueError:
        return 0.0


def _run(cmd, timeout=None, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, **kw)


def probe_speed(url: str, timeout: int = 15) -> tuple[bool, float, int]:
    """测速：请求前 1MB。返回 (可用, 速度B/s, http状态码)。206=支持range(可续传)。"""
    try:
        r = subprocess.run(
            ["curl", "-sL", "-o", "/dev/null", "-r", "0-1048575",
             "-w", "%{http_code} %{speed_download}", url],
            capture_output=True, text=True, timeout=timeout)
        out = r.stdout.strip().split()
        code = int(out[0]) if out else 0
        speed = _parse_speed(out[1]) if len(out) > 1 else 0.0
        return code in (200, 206) and speed > 0, speed, code
    except subprocess.TimeoutExpired:
        return False, 0.0, 0


def pick_best_mirror(gh_url: str, proxies: list[str], timeout: int = 15,
                     min_speed: float = 1024 * 1024) -> tuple[str | None, str | None, float]:
    """直连优先，不行就探测代理。返回 (下载URL, 来源名, 速度)。"""
    ok, speed, code = probe_speed(gh_url, timeout)
    if ok and speed >= min_speed:
        return gh_url, "直连", speed
    print(f"[i] 直连不可用（{code}，{speed/1024:.0f}KB/s），探测代理镜像...")
    best_url, best_name, best_speed = None, None, 0.0
    for p in proxies:
        proxied = f"{p}/{gh_url}"
        ok, sp, code = probe_speed(proxied, timeout)
        if ok and sp > best_speed:
            best_url, best_name, best_speed = proxied, p, sp
            print(f"    {p}: {code} {sp/1024:.0f}KB/s  ✓")
        else:
            print(f"    {p}: {code} {sp/1024:.0f}KB/s  ✗")
    return best_url, best_name, best_speed


def download(url: str, dest: Path, min_speed_hint: bool = True, timeout: int = 600) -> bool:
    """断点续传下载。dest 已存在则继续。返回是否成功。"""
    cmd = ["curl", "-sL", "-C", "-", "-o", str(dest), "--retry", "3",
           "--retry-delay", "2", "-m", str(timeout), url]
    t0 = time.time()
    r = _run(cmd, timeout=timeout + 30)
    dt = time.time() - t0
    if r.returncode != 0 or not dest.exists() or dest.stat().st_size == 0:
        print(f"[x] 下载失败 rc={r.returncode}: {url}")
        return False
    print(f"[✓] 下载完成 {dest.stat().st_size/1048576:.1f}MB，耗时 {dt:.1f}s，来源 url={url}")
    return True


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def verify(dest: Path, sha256: str | None = None, verify_url: str | None = None) -> bool:
    if sha256:
        actual = sha256_of(dest)
        ok = actual.lower() == sha256.lower()
        print(f"[{'✓' if ok else '✗'}] SHA256 {'匹配' if ok else f'不匹配: 期望{sha256} 实际{actual}'}")
        return ok
    if verify_url:
        r = _run(["curl", "-sL", verify_url], timeout=60)
        expected = None
        for line in r.stdout.splitlines():
            h, _, name = line.partition("  ")
            if dest.name in name:
                expected = h.strip().lower()
                break
        if expected:
            actual = sha256_of(dest)
            ok = actual == expected
            print(f"[{'✓' if ok else '✗'}] SHA256(官方) {'匹配' if ok else '不匹配'}")
            return ok
        print("[i] checksums 文件中未找到本文件条目，跳过校验")
    return True


def extract(dest: Path, out_dir: Path) -> Path | None:
    """解压，返回解压后的顶层目录（若有）。"""
    out_dir.mkdir(parents=True, exist_ok=True)
    name = dest.name.lower()
    try:
        if name.endswith((".tar.xz", ".tar.gz", ".tar.bz2", ".tar", ".tgz", ".tar.zst")):
            _run(["tar", "xf", str(dest), "-C", str(out_dir)], timeout=600)
        elif name.endswith(".zip"):
            _run(["unzip", "-q", "-o", str(dest), "-d", str(out_dir)], timeout=600)
        else:
            print("[i] 非归档文件，跳过解压")
            return None
    except Exception as e:
        print(f"[x] 解压失败: {e}")
        return None
    # 找顶层目录
    subs = [p for p in out_dir.iterdir() if p.is_dir() and not p.name.startswith(".")]
    print(f"[✓] 已解压到 {out_dir}")
    return subs[0] if len(subs) == 1 else None


def install(src: Path, install_dir: Path, links: list[str] | None = None) -> None:
    """安装：复制 bin 到 install_dir，按需建符号链接到 /usr/local/bin。"""
    install_dir.mkdir(parents=True, exist_ok=True)
    src_bin = src if src.is_dir() else src.parent
    # 常见结构：顶层/bin，或直接可执行文件
    if (src / "bin").is_dir():
        src_bin = src / "bin"
    shutil.copytree(src_bin, install_dir / src_bin.name, dirs_exist_ok=True)
    print(f"[✓] 已安装 {src_bin.name} -> {install_dir}")
    if links:
        for link in links:
            target = src_bin / link
            if target.exists():
                dst = Path("/usr/local/bin") / link
                dst.unlink(missing_ok=True)
                dst.symlink_to(target)
                print(f"[✓] 符号链接: {dst} -> {target}")


def resolve_release(owner_repo: str, tag: str = "latest",
                    pattern: str = None, proxies: list[str] = None) -> str:
    """查 release 资产 URL。tag 缺省 latest；pattern 正则匹配资产名（默认第一个）。"""
    api = f"https://api.github.com/repos/{owner_repo}/releases/{tag}"
    r = _run(["curl", "-sL", api], timeout=30)
    try:
        data = json.loads(r.stdout)
    except json.JSONDecodeError:
        print("[x] release API 解析失败（直连可能被墙，请手动指定完整 URL）")
        sys.exit(1)
    if isinstance(data, dict) and "assets" not in data:
        print(f"[x] API 返回异常: {data.get('message', data)}")
        sys.exit(1)
    assets = data.get("assets", [])
    if not assets:
        print("[x] 该 release 无资产")
        sys.exit(1)
    names = [a["name"] for a in assets]
    print(f"[i] release={data.get('tag_name','?')} 资产: {', '.join(names)}")
    if pattern:
        cands = [n for n in names if re.search(pattern, n)]
        if not cands:
            print(f"[x] 无资产匹配 {pattern}")
            sys.exit(1)
        pick = cands[0]
    else:
        pick = names[0]
    return f"https://github.com/{owner_repo}/releases/download/{data['tag_name']}/{pick}"


def main():
    ap = argparse.ArgumentParser(description="GitHub 拉取：直连→代理→续传→校验→解压→安装")
    ap.add_argument("url", nargs="?", help="GitHub 下载 URL")
    ap.add_argument("--release", metavar="owner/repo", help="查询最新 release 并下载资产")
    ap.add_argument("--tag", default="latest")
    ap.add_argument("--asset-pattern", help="正则匹配资产名")
    ap.add_argument("--clone", metavar="owner/repo", help="git clone 整个仓库")
    ap.add_argument("--recursive", action="store_true", help="clone 含子模块")
    ap.add_argument("--branch", default=None)
    ap.add_argument("--depth", type=int, default=1)
    ap.add_argument("--out", default=".", help="输出目录")
    ap.add_argument("--extract", action="store_true", help="下载后解压")
    ap.add_argument("--install", metavar="DIR", help="安装到指定目录（配合 --extract）")
    ap.add_argument("--sha256", help="期望 SHA256 哈希")
    ap.add_argument("--verify-url", help="官方 checksums.sha256 地址")
    ap.add_argument("--min-speed", default="1M", help="直连可接受的最低速度（默认 1M）")
    ap.add_argument("--timeout", type=int, default=600, help="下载超时秒数")
    args = ap.parse_args()

    proxies = [p.strip() for p in os.environ.get("GITHUB_PROXIES", "").split(",") if p.strip()] \
        or DEFAULT_PROXIES
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    min_speed = _parse_speed(args.min_speed)

    # clone 分支
    if args.clone:
        url = f"https://github.com/{args.clone}.git"
        cmd = ["git", "clone"]
        if args.recursive:
            cmd.append("--recursive")
        if args.depth and args.depth > 0:
            cmd += ["--depth", str(args.depth)]
        if args.branch:
            cmd += ["--branch", args.branch]
        cmd += [url, str(out_dir / args.clone.split("/")[-1])]
        print(f"[i] git clone {url}")
        r = _run(cmd, timeout=1800)
        if r.returncode != 0:
            # 直连 clone 失败 → 走代理
            ok, _, _ = probe_speed(f"https://github.com/{args.clone}.git", 10)
            if not ok:
                print("[i] 直连 clone 失败，尝试代理镜像...")
                for p in proxies:
                    r2 = _run(["git", "clone", "--depth", "1"] +
                              (["--recursive"] if args.recursive else []) +
                              [f"{p}/https://github.com/{args.clone}.git",
                               str(out_dir / args.clone.split("/")[-1])], timeout=1800)
                    if r2.returncode == 0:
                        print(f"[✓] clone 成功（经 {p}）")
                        return
        if r.returncode == 0:
            print("[✓] clone 完成")
        else:
            print("[x] clone 失败")
        return

    # 解析下载 URL
    if args.release:
        url = resolve_release(args.release, args.tag, args.asset_pattern, proxies)
    elif args.url:
        url = args.url
    else:
        ap.error("需要 <url>、--release 或 --clone 之一")

    dest = out_dir / Path(url.split("?")[0]).name
    if not dest.name:
        dest = out_dir / "download.bin"

    # 下载：直连 → 代理
    best_url, source, speed = pick_best_mirror(url, proxies, min_speed=min_speed)
    if not best_url:
        print("[x] 直连与所有代理均不可用")
        sys.exit(1)
    print(f"[i] 选择 {source}（{speed/1024:.0f}KB/s）")
    if not download(best_url, dest, timeout=args.timeout):
        sys.exit(1)

    # 校验
    if not verify(dest, args.sha256, args.verify_url):
        print("[x] 校验失败，文件已删除")
        dest.unlink(missing_ok=True)
        sys.exit(1)

    # 解压
    extracted = None
    if args.extract:
        extracted = extract(dest, out_dir)

    # 安装
    if args.install:
        src = extracted or dest
        install(src, Path(args.install))

    print(f"[✓] 完成，输出: {dest}")
    print("    磁盘占用清理提示: 确认无误后可删除压缩包 "
          f"`rm {dest}`（{dest.stat().st_size/1048576:.0f}MB）")


if __name__ == "__main__":
    main()
