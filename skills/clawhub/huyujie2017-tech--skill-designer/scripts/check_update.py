#!/usr/bin/env python3
"""
check_update.py — 检查 skill-designer 在 SkillHub 上是否有新版本

为什么需要这个脚本：
    SkillHub 官方**没有**供 CLI 消费的 per-skill 更新清单端点。
    `skillhub upgrade` 要求 config.json 的 update_url 返回一个含 `version` + `zip_url`
    的 JSON，而官方 API 只有：
      - GET /api/v1/skills/{slug}             → latestVersion.version（无 zip_url）
      - GET /api/v1/skills/{slug}/versions    → versions[]（无 zip_url）
    两者都不符合 CLI 的清单格式，所以 `skillhub upgrade` 对社区 skill 跑不通
    （会停在 "skip: missing update URL" 或直接报清单缺字段）。
    本脚本直接读官方 API 做版本比对，是**今天就能跑通**的自动更新检查路径。

用法：
    python scripts/check_update.py                 # 人类可读报告
    python scripts/check_update.py --json          # 机器可消费

退出码：
    0  检查成功（无论是否有新版本；看 JSON 的 has_update 字段）
    1  检查失败（网络不可达 / 响应非预期 / 本地版本读不出）

输出（--json）：
    {local_version, latest_version, has_update, homepage, install_cmd, changelog, checked_url}
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

try:
    from retry import read_text_robust
except ImportError:  # 单独运行时兜底
    def read_text_robust(path: Path) -> str:
        return path.read_text(encoding="utf-8-sig", errors="replace")

# ─── SkillHub 坐标（唯一事实源：skill 根目录的 config.json） ───
DEFAULT_CONFIG = {
    "slug": "high-quality-skill-guidance",
    "namespace": "user_4894573e",
    "homepage": "https://skillhub.cn/skills/user_4894573e/high-quality-skill-guidance",
}
API_TEMPLATE = "https://api.skillhub.cn/api/v1/skills/{slug}"
TIMEOUT = 15


def find_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_config(root: Path) -> dict:
    cfg_path = root / "config.json"
    cfg = dict(DEFAULT_CONFIG)
    if cfg_path.exists():
        try:
            cfg.update(json.loads(read_text_robust(cfg_path)))
        except json.JSONDecodeError:
            pass  # config.json 坏了就用默认值，不阻塞检查
    return cfg


def local_version(root: Path) -> str:
    """从 SKILL.md frontmatter 读 version（本 skill 的版本唯一事实源）。"""
    text = read_text_robust(root / "SKILL.md")
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("version:"):
            return s.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def fetch_latest(slug: str) -> dict:
    url = API_TEMPLATE.format(slug=slug)
    req = urllib.request.Request(url, headers={"User-Agent": "skill-designer/update-check"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"无法访问 SkillHub API（{url}）：{exc}") from exc
    except TimeoutError:
        raise RuntimeError(f"访问 SkillHub API 超时（{TIMEOUT}s）：{url}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"SkillHub API 返回的不是合法 JSON：{exc}") from exc
    latest = data.get("latestVersion") or {}
    version = str(latest.get("version") or "").strip()
    if not version:
        raise RuntimeError("SkillHub API 响应缺少 latestVersion.version（接口可能已变更）")
    return {"version": version, "changelog": str(latest.get("changelog") or "").strip(), "url": url}


def vtuple(v: str) -> tuple:
    """'2.15.0' → (2, 15, 0)；非数字段按 0 处理，保证比较不崩。"""
    parts = []
    for seg in str(v).split("."):
        num = "".join(ch for ch in seg if ch.isdigit())
        parts.append(int(num) if num else 0)
    return tuple(parts) if parts else (0,)


def newer(a: str, b: str) -> bool:
    """a 是否比 b 新（长度不齐补 0）。"""
    ta, tb = vtuple(a), vtuple(b)
    n = max(len(ta), len(tb))
    return ta + (0,) * (n - len(ta)) > tb + (0,) * (n - len(tb))


def main() -> int:
    ap = argparse.ArgumentParser(description="检查 skill-designer 在 SkillHub 上是否有新版本")
    ap.add_argument("--json", action="store_true", help="机器可消费输出")
    ap.add_argument("--root", default=None, help="skill-designer 根目录（默认自动推断）")
    args = ap.parse_args()

    root = Path(args.root).resolve() if args.root else find_root()
    cfg = load_config(root)
    ver_local = local_version(root)
    if not ver_local:
        msg = f"读不到本地版本：{root / 'SKILL.md'} 的 frontmatter 缺 version 字段"
        print(f"[check_update] 错误：{msg}", file=sys.stderr)
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False, indent=2))
        return 1

    try:
        latest = fetch_latest(cfg["slug"])
    except RuntimeError as exc:
        print(f"[check_update] 错误：{exc}", file=sys.stderr)
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 1

    has_update = newer(latest["version"], ver_local)
    install_cmd = (
        f"skillhub install {cfg['slug']} --namespace {cfg['namespace']} --dir ~/.workbuddy/skills"
    )
    payload = {
        "ok": True,
        "local_version": ver_local,
        "latest_version": latest["version"],
        "has_update": has_update,
        "homepage": cfg["homepage"],
        "install_cmd": install_cmd,
        "changelog": latest["changelog"],
        "checked_url": latest["url"],
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"[check_update] 本地版本 {ver_local} ｜ SkillHub 最新 {latest['version']}")
    if has_update:
        print(f"[check_update] ⬆️  有新版本可用。升级命令：\n  {install_cmd}")
        if latest["changelog"]:
            print(f"[check_update] 更新说明：{latest['changelog']}")
    else:
        print("[check_update] ✅ 已是最新（或本地版本更高，属开发态）。")
    print(f"[check_update] 主页：{cfg['homepage']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
