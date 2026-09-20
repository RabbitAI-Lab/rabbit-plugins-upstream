#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
skill-distributor 发布前检测（preflight check）
把「技能生产级测试」32 维检查框架中可静态自动化的维度，实现为发布前的自动门禁。

用法:
  python preflight_check.py --skill <技能目录> [--json]
  exit code: 0=通过(可发布)  1=P0/P1 阻断(不可发布)  2=仅警告(可发布但有建议)

覆盖维度（与测试清单 v5 对齐）:
  维度 10  上架就绪度: frontmatter 完整性 / slug / version / displayName
  维度 5   文档一致性: config 版本与 SKILL.md 版本一致性
  维度 11  脚本真实性: 全部 .py 语法编译 / 关键文件存在
  维度 12  成本效率(静态): SKILL.md 与 references 体积
  维度 13  提示注入(静态线索): references 中可疑"忽略规则"类指令
  维度 17  隐私 PII(静态子集): 密钥 / token / 密码 / 私钥 / 绝对路径泄露扫描
  维度 18  可发现性/关键字优化: description 长度与功能动词 / 中英文关键词 / displayName / 场景触发词 / 名称呼应
安全: 检测只报告"发现位置"，绝不打印密钥值本身。
"""
import argparse
import json
import re
import sys
from pathlib import Path

# ---------- 基础 ----------

P0, P1, P2, P3 = "P0", "P1", "P2", "P3"
SEV_ORDER = {P0: 0, P1: 1, P2: 2, P3: 3}

# 不应被打包进发布副本的目录/文件（与 distribute.py EXCLUDE 保持一致）
EXCLUDE_DIRS = {".git", "__pycache__", ".skill-distributor", ".workbuddy", "node_modules"}
# 密钥载体文件：不扫描内容（存在即 P0 阻断，见 check_secrets）
EXCLUDE_FILES = {"secrets.json", ".env", ".npmrc", ".pypirc", ".netrc"}
# 密钥文件变体（发现即 P0：.env.local / .env.prod 等携带真实密钥）
ENV_FILE_BLOCK = [".env.local", ".env.prod", ".env.production", ".env.dev", ".env.development",
                  ".env.test", ".env.staging", ".env.uat", ".env.qa"]
# 可放行的示例/模板文件（只含占位符，无真实密钥）
ENV_FILE_ALLOW = {".env.example", ".env.sample", ".env.template"}

# 高置信密钥模式（命中即 P0：真实密钥，如 GitHub PAT / AWS / 私钥 / Slack token / JWT / 连接串）
HIGH_CONFIDENCE = [
    (r"\bghp_[A-Za-z0-9]{20,}\b", "GitHub Personal Access Token (ghp_)"),
    (r"\bgithub_pat_[A-Za-z0-9_]{20,}\b", "GitHub fine-grained PAT"),
    (r"\bgh[ousr]_[A-Za-z0-9]{20,}\b", "GitHub OAuth/User/Server/Refresh token"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS Access Key ID"),
    (r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----", "私钥 (PRIVATE KEY)"),
    (r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b", "Slack token"),
    (r"\bsk-ant-[A-Za-z0-9_-]{20,}\b", "Anthropic API key (sk-ant-)"),
    (r"\bsk-[A-Za-z0-9]{20,}\b", "疑似 OpenAI/第三方 API key (sk-)"),
    (r"\bAIza[0-9A-Za-z_-]{20,}\b", "Google API key"),
    (r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}\b", "JWT / OAuth Bearer token (eyJ...)"),
    (r"(?i)\b(?:postgres|mysql|mariadb|redis|mongodb(?:\+srv)?|amqp|https?|ftps?)://[^\s/]+:[^\s/@]{4,}@", "URL 内联凭证 (user:password@host)"),
]

# 一般敏感赋值（命中即 P1：token/password/api_key 等赋了引号包裹的真实值）
SENSITIVE_ASSIGN = [
    (r'(?i)\b(token|password|passwd|pwd|api[_-]?key|apikey|secret|access[_-]?key|auth|credential)\b\s*[=:]\s*["\'][^"\']{8,}["\']', "敏感字段赋值（引号包裹值）"),
    (r'(?i)(GITHUB_TOKEN|GITHUB_PAT|SKILLHUB_TOKEN|CLAWHUB_AUTH|MIRROR_URLS|OPENAI_API_KEY|ANTHROPIC_API_KEY|AWS_SECRET_ACCESS_KEY|GOOGLE_API_KEY|AZURE_OPENAI_API_KEY)\s*[=:]\s*\S{8,}', "平台密钥环境变量赋值"),
    (r'(?i)\b_authToken\b\s*[=:]\s*\S{8,}', "npm/pip 凭证 (_authToken)"),
]

# 可疑提示注入线索（P2）
INJECTION_HINTS = [
    (r"(?i)忽略(上述|之前|所有)?(规则|指令|指示)", "疑似提示注入指令 (忽略规则)"),
    (r"(?i)ignore (all |the )?(previous )?(instructions|rules|prompt)", "疑似提示注入指令 (ignore instructions)"),
    (r"(?i)你(现在|必须|一定要).{0,6}(扮演|假装)", "疑似角色劫持指令"),
]

# 绝对本地路径泄露（P2：可能泄露用户名/机器结构）
PATH_LEAK = [
    (r"[A-Za-z]:\\Users\\", "Windows 用户绝对路径 (C:\\Users\\)"),
    (r"/Users/[A-Za-z0-9_\-]+", "macOS 用户绝对路径 (/Users/)"),
    (r"/home/[A-Za-z0-9_\-]+", "Linux 用户绝对路径 (/home/)"),
]

# ---- 维度 18 可发现性 / 关键字优化 ----

# 功能动词（中英）——description 应至少命中一个，说明"技能能做什么"
FUNCTION_VERBS = [
    "推荐", "生成", "创建", "分析", "搜索", "查询", "检测", "测试", "发布", "分发",
    "转换", "翻译", "提取", "总结", "整理", "规划", "设计", "编写", "写作", "修复",
    "优化", "比较", "筛选", "评估", "审核", "解读", "记录", "监控", "提醒", "收集",
    "recommend", "generate", "create", "analyze", "search", "detect", "test",
    "publish", "distribute", "convert", "translate", "extract", "summarize",
    "plan", "design", "write", "build", "compare", "evaluate", "review", "monitor",
]

# 场景触发词——description 含这些词利于 AI 触发判断与用户搜索
TRIGGER_WORDS = ["当", "用于", "需要", "使用", "如果", "when", "use", "used", "if", "help", "for"]

# 显示名常见噪声后缀（去除后取核心词做"名称呼应"检查）
DISPLAYNAME_NOISE = ["技能", "工具", "助手", "中心", "平台", "系统", "模块", "工作台",
                     "Skill", "Tool", "Assistant", "Hub"]

SKIP_SCAN_SUFFIX = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".gz", ".faiss", ".woff", ".woff2", ".ttf", ".otf", ".mp3", ".mp4")


def log(msg):
    print(f"[preflight] {msg}")


def severity_rank(sev):
    return SEV_ORDER.get(sev, 3)


# ---------- 检查实现 ----------

class Preflight:
    def __init__(self, skill_dir):
        self.skill_dir = Path(skill_dir)
        self.issues = []  # (severity, dim, message, file, line)
        self.checked = []  # (dim, result)

    def add(self, sev, dim, message, file="", line=None):
        self.issues.append({"severity": sev, "dimension": dim, "message": message,
                            "file": str(file) if file else "", "line": line})

    def check(self, dim, result, detail=""):
        self.checked.append({"dimension": dim, "result": result, "detail": detail})

    # 维度 10: 基础结构 + frontmatter
    def check_structure(self):
        dim = "10-上架就绪"
        skill_md = self.skill_dir / "SKILL.md"
        if not skill_md.exists():
            self.add(P0, dim, "SKILL.md 不存在，不是有效技能包", skill_md)
            self.check(dim, "FAIL", "缺少 SKILL.md")
            return False
        text = skill_md.read_text(encoding="utf-8-sig", errors="replace")
        m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
        if not m:
            self.add(P0, dim, "SKILL.md 缺少 YAML frontmatter (--- ---)", skill_md)
            self.check(dim, "FAIL", "无 frontmatter")
            return False
        fields = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fields[k.strip()] = v.strip().strip('"\'')
        self.fm = fields  # 供可发现性等维度复用
        # 必填
        for req in ("name", "description"):
            if not fields.get(req):
                self.add(P1, dim, f"frontmatter 缺少必填字段: {req}", skill_md)
        if not fields.get("name") or not fields.get("description"):
            self.check(dim, "WARN", "必填字段缺失")
            return False
        # 建议字段
        for opt in ("license", "displayName", "summary", "slug", "version"):
            if not fields.get(opt):
                self.add(P3, dim, f"建议补充 frontmatter 字段: {opt}", skill_md)
        # slug 合法性
        slug = fields.get("slug", fields.get("name", ""))
        if not re.match(r"^[a-z0-9][a-z0-9-]*$", slug):
            self.add(P1, dim, f"slug 不合法（需 kebab-case 小写）: {slug}", skill_md)
        elif not (2 <= len(slug) <= 128):
            self.add(P1, dim, f"slug 长度需 2-128: {slug}", skill_md)
        # version 合法性
        ver = fields.get("version", "")
        if ver and not re.match(r"^\d+\.\d+\.\d+$", ver):
            self.add(P1, dim, f"version 不合法（需 SemVer x.y.z）: {ver}", skill_md)
        # 中文字段抽查（维度 25 静态线索）
        self.check(dim, "OK", f"frontmatter 字段: {', '.join(k for k in fields if k in ('name','description','displayName','slug','version','license','summary'))}")
        return True

    # 维度 5: config 版本与 frontmatter 版本一致性
    def check_version_consistency(self):
        dim = "5-文档一致性"
        cfg = self.skill_dir / ".skill-distributor" / "config.json"
        cfg_home = Path.home() / ".skill-distributor" / "config.json"
        ver_cfg = None
        if cfg.exists():
            try:
                ver_cfg = json.loads(cfg.read_text(encoding="utf-8")).get("version")
            except Exception:
                pass
        elif cfg_home.exists():
            try:
                ver_cfg = json.loads(cfg_home.read_text(encoding="utf-8")).get("version")
            except Exception:
                pass
        ver_fm = None
        skill_md = self.skill_dir / "SKILL.md"
        if skill_md.exists():
            text = skill_md.read_text(encoding="utf-8-sig", errors="replace")
            m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
            if m:
                for line in m.group(1).splitlines():
                    if line.startswith("version:"):
                        ver_fm = line.split(":", 1)[1].strip().strip('"\'')
                        break
        if ver_cfg and ver_fm and ver_cfg != ver_fm:
            self.add(P2, dim, f"版本不一致: config={ver_cfg} vs SKILL.md={ver_fm}", cfg)
            self.check(dim, "WARN", f"config={ver_cfg} fm={ver_fm}")
        else:
            self.check(dim, "OK", f"版本一致({ver_cfg or ver_fm})")

    # 维度 11: 脚本语法
    def check_scripts(self):
        dim = "11-脚本真实性"
        scripts_dir = self.skill_dir / "scripts"
        if not scripts_dir.exists():
            self.check(dim, "OK", "无 scripts 目录")
            return
        py_files = sorted(scripts_dir.rglob("*.py"))
        bad = []
        for f in py_files:
            try:
                import ast
                ast.parse(f.read_text(encoding="utf-8", errors="replace"))
            except SyntaxError as e:
                bad.append((f, e))
                self.add(P1, dim, f"Python 语法错误: {e}", f, getattr(e, "lineno", None))
        self.check(dim, "FAIL" if bad else "OK", f"{len(py_files)} 个 .py，{'语法错误 ' + str(len(bad)) if bad else '全部通过'}")

    # 维度 12: 体积（静态）
    def check_size(self):
        dim = "12-成本效率"
        skill_md = self.skill_dir / "SKILL.md"
        if skill_md.exists():
            words = len(re.findall(r"\S+", skill_md.read_text(encoding="utf-8", errors="replace")))
            if words > 5000:
                self.add(P2, dim, f"SKILL.md 词数 {words} > 5000，触发即撑爆上下文", skill_md)
            self.check(dim, "OK" if words <= 5000 else "WARN", f"SKILL.md {words} 词")
        refs_dir = self.skill_dir / "references"
        if refs_dir.exists():
            big = []
            for f in sorted(refs_dir.rglob("*.md")):
                w = len(re.findall(r"\S+", f.read_text(encoding="utf-8", errors="replace")))
                if w > 10000:
                    big.append((f, w))
            if big:
                for f, w in big[:5]:
                    self.add(P2, dim, f"references 单文件 {w} 词 > 10000，建议提供 grep 检索模式", f)

    # 维度 13: 提示注入静态线索
    def check_injection(self):
        dim = "13-提示注入"
        hits = []
        for f in list((self.skill_dir / "references").rglob("*.md")) if (self.skill_dir / "references").exists() else []:
            for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                for pat, desc in INJECTION_HINTS:
                    if re.search(pat, line):
                        hits.append((f, i, desc, line))
                        break
        if hits:
            for f, i, desc, line in hits[:8]:
                self.add(P2, dim, f"疑似注入线索 [{desc}]: {line[:60]}", f, i)
        self.check(dim, "WARN" if hits else "OK", f"{len(hits)} 处可疑")

    # 维度 17: 敏感信息 / 密钥 / 路径泄露（静态子集）
    def check_secrets(self):
        dim = "17-隐私PII"
        p0 = p1 = p2 = 0
        for f in sorted(self.skill_dir.rglob("*")):
            if not f.is_file():
                continue
            rel = f.relative_to(self.skill_dir)
            if any(part in EXCLUDE_DIRS for part in rel.parts):
                continue
            if f.name in EXCLUDE_FILES or f.name.endswith(SKIP_SCAN_SUFFIX):
                continue
            if f.name in ENV_FILE_ALLOW:
                # .env.example 等占位符示例：放行，不扫描内容
                continue
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            lines = text.splitlines()
            for i, line in enumerate(lines, 1):
                for pat, desc in HIGH_CONFIDENCE:
                    if re.search(pat, line):
                        p0 += 1
                        self.add(P0, dim, f"发现高置信密钥 [{desc}]", f, i)
                        break
                for pat, desc in SENSITIVE_ASSIGN:
                    if re.search(pat, line):
                        p1 += 1
                        self.add(P1, dim, f"发现敏感赋值 [{desc}]", f, i)
                        break
                for pat, desc in PATH_LEAK:
                    if re.search(pat, line):
                        p2 += 1
                        self.add(P2, dim, f"本地绝对路径泄露 [{desc}]", f, i)
                        break
        # 密钥载体文件存在性：.env / .npmrc 等发现即 P0（携带真实密钥，严禁发布）
        for env_name in EXCLUDE_FILES:
            if (self.skill_dir / env_name).exists():
                self.add(P0, dim, f"技能目录内发现密钥载体文件 {env_name}，严禁发布", self.skill_dir / env_name)
        for env_name in ENV_FILE_BLOCK:
            if (self.skill_dir / env_name).exists():
                self.add(P0, dim, f"技能目录内发现密钥文件变体 {env_name}，严禁发布（如需示例请改名 .env.example）", self.skill_dir / env_name)
        # 全目录级 .env.* 变体（含子目录）同样阻断
        for f in sorted(self.skill_dir.rglob(".env.*")):
            if f.name in ENV_FILE_ALLOW:
                continue
            rel = f.relative_to(self.skill_dir)
            if any(part in EXCLUDE_DIRS for part in rel.parts):
                continue
            self.add(P0, dim, f"发现密钥文件变体 {rel}，严禁发布（如需示例请改名 .env.example）", f)
        self.check(dim, "FAIL" if p0 else ("WARN" if p1 else "OK"), f"P0={p0} P1={p1} P2={p2}")

    # 维度 18: 可发现性 / 关键字优化（利于真人搜索 + AI 检索触发）
    def check_discoverability(self):
        dim = "18-可发现性"
        fm = getattr(self, "fm", {})
        skill_md = self.skill_dir / "SKILL.md"
        desc = fm.get("description", "") or ""
        name = fm.get("name", "") or ""
        dname = fm.get("displayName", "") or ""
        sugg = 0

        if not desc:
            self.add(P2, dim, "description 为空，无法被搜索与 AI 触发", skill_md)
            self.check(dim, "WARN", "description 为空")
            return

        # 1. description 长度：过短无法理解功能，过长稀释关键词
        if len(desc) < 40:
            self.add(P2, dim, f"description 过短（{len(desc)} 字符，建议 60-300），搜索与 AI 触发难以理解功能", skill_md)
            sugg += 1
        elif len(desc) > 500:
            self.add(P3, dim, f"description 过长（{len(desc)} 字符，建议 ≤300），关键词被稀释", skill_md)
            sugg += 1

        # 2. 功能动词：说明"能做什么"，是搜索与触发的主命中点
        verbs = [v for v in FUNCTION_VERBS if re.search(r"(?i)" + re.escape(v), desc)]
        if not verbs:
            self.add(P2, dim, "description 未含功能动词（推荐/生成/分析/搜索/发布等），用户与 AI 无法确定技能能力", skill_md)
            sugg += 1

        # 3. 英文关键词：国际平台（GitHub/ClawHub）与英文检索命中
        if not re.search(r"[A-Za-z]{3,}", desc):
            self.add(P3, dim, "description 无英文关键词，国际平台与英文检索难以命中，建议补充英文功能词", skill_md)
            sugg += 1

        # 4. 中文显示名：利于中文用户搜索与识别
        if not dname:
            self.add(P2, dim, "缺少 displayName（中文显示名），建议补充以利于中文搜索", skill_md)
            sugg += 1
        elif not re.search(r"[\u4e00-\u9fff]", dname):
            self.add(P2, dim, f"displayName 无中文（{dname}），建议使用中文显示名利于搜索", skill_md)
            sugg += 1

        # 5. 场景触发词：AI 判断"何时用"依赖场景表述
        triggers = [t for t in TRIGGER_WORDS if t in desc]
        if not triggers:
            self.add(P3, dim, "description 未含场景词（当/用于/需要/使用/when/use 等），AI 触发判断弱，建议补充使用场景", skill_md)
            sugg += 1

        # 6. 名称呼应：displayName 核心词（按分隔符拆词）是否出现在 description（搜索技能名时命中）
        core = dname or name
        for noise in DISPLAYNAME_NOISE:
            core = core.replace(noise, "")
        candidates = [c for c in re.split(r"[·:：\-_ .]+", core) if len(c) >= 2]
        hit = any(c in desc for c in candidates)
        if candidates and not hit:
            self.add(P2, dim, f"displayName 核心词「{'/'.join(candidates)}」未出现在 description，按名称搜索时命中率低", skill_md)
            sugg += 1

        # 7. summary：发布时自动注入，但首句质量决定摘要质量
        if not fm.get("summary"):
            self.add(P3, dim, "无 summary（发布时自动注入），建议 description 首句即点明核心功能，便于生成优质摘要", skill_md)
            sugg += 1

        detail = f"动词命中={','.join(verbs[:4]) if verbs else '无'} 场景词={','.join(triggers[:4]) if triggers else '无'} 建议={sugg}"
        self.check(dim, "WARN" if sugg else "OK", detail)

    def run(self):
        self.check_structure()
        self.check_version_consistency()
        self.check_scripts()
        self.check_size()
        self.check_injection()
        self.check_secrets()
        self.check_discoverability()
        return self

    # 裁决
    def verdict(self):
        if not self.issues:
            return "ship", "全部检测通过，可以发布"
        sev = min(severity_rank(i["severity"]) for i in self.issues)
        p0 = [i for i in self.issues if i["severity"] == P0]
        p1 = [i for i in self.issues if i["severity"] == P1]
        if p0:
            return "no-ship", f"存在 {len(p0)} 个 P0 缺陷（安全/致命），禁止发布"
        if p1:
            return "no-ship", f"存在 {len(p1)} 个 P1 缺陷（生产阻塞），默认禁止发布（--force 可强制）"
        if p0 or p1:
            return "no-ship", "存在阻塞缺陷"
        return "ship-with-warnings", f"存在 {len(self.issues)} 个 P2/P3 建议项，不影响发布"


def main():
    parser = argparse.ArgumentParser(description="skill-distributor 发布前检测")
    parser.add_argument("--skill", required=True, help="技能目录（含 SKILL.md）")
    parser.add_argument("--json", action="store_true", help="输出 JSON")
    args = parser.parse_args()

    skill_dir = Path(args.skill).resolve()
    if not skill_dir.is_dir():
        print(json.dumps({"error": f"目录不存在: {skill_dir}"}, ensure_ascii=False))
        return 2

    pf = Preflight(skill_dir).run()
    verdict, reason = pf.verdict()

    if args.json:
        out = {
            "skill": str(skill_dir),
            "verdict": verdict,
            "reason": reason,
            "checked": pf.checked,
            "issues": pf.issues,
            "exit_code": 1 if verdict == "no-ship" else (2 if verdict == "ship-with-warnings" else 0),
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return out["exit_code"]

    # 文本报告
    print(f"\n========== 发布前检测报告 ==========")
    print(f"技能目录: {skill_dir}")
    print(f"检测维度: {len(pf.checked)} 项")
    for c in pf.checked:
        mark = {"OK": "✓", "WARN": "⚠", "FAIL": "✗"}.get(c["result"], "·")
        print(f"  [{mark}] 维度 {c['dimension']}: {c['result']}  {c['detail']}")
    if pf.issues:
        print(f"\n发现问题: {len(pf.issues)} 个")
        for i in sorted(pf.issues, key=lambda x: severity_rank(x["severity"])):
            loc = f" @ {i['file']}" + (f":{i['line']}" if i["line"] else "")
            print(f"  [{i['severity']}] (维度 {i['dimension']}) {i['message']}{loc}")
    else:
        print("\n未发现问题。")
    print(f"\n裁决: {verdict} — {reason}")
    print("====================================")
    return 1 if verdict == "no-ship" else (2 if verdict == "ship-with-warnings" else 0)


if __name__ == "__main__":
    sys.exit(main())
