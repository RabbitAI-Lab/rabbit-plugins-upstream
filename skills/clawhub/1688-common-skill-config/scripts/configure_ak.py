#!/usr/bin/env python3
"""
AK 管理器辅助脚本 — 1688-common-skill-config Skill 的工具脚本

命令:
  python3 configure_ak.py status          # 查看所有 AK 配置状态
  python3 configure_ak.py configure <AK>  # 配置 1688 Gateway AK
  python3 configure_ak.py verify          # 验证 1688 AK 是否有效
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


# Skill 安装路径搜索
SKILL_BASES = [
    Path.home() / ".openclaw" / "skills",
    Path.cwd(),
]


def find_skill_dir(skill_name: str) -> Path | None:
    """查找 Skill 根目录（包含 cli.py 的目录）"""
    for base in SKILL_BASES:
        d = base / skill_name
        if d.exists() and (d / "cli.py").exists():
            return d
    # 向上搜索 workspace
    p = Path.cwd()
    for _ in range(5):
        for sub in ["skills", ".qoder/skills"]:
            d = p / sub / skill_name
            if d.exists() and (d / "cli.py").exists():
                return d
        if p.parent == p:
            break
        p = p.parent
    return None


def find_scripts_dir(skill_name: str) -> Path | None:
    """查找 Skill 的 scripts 子目录"""
    skill_dir = find_skill_dir(skill_name)
    if skill_dir:
        scripts = skill_dir / "scripts"
        if scripts.exists():
            return scripts
    return None


def check_1688_ak() -> dict:
    """检查 1688 Gateway AK 配置状态"""
    result = {"type": "1688 Gateway AK", "configured": False, "detail": "", "skills": []}

    for name in ["1688-product-find", "1688-source-supplier"]:
        if find_skill_dir(name):
            result["skills"].append(name)

    scripts = find_scripts_dir("1688-product-find") or find_scripts_dir("1688-source-supplier")
    if scripts:
        sys.path.insert(0, str(scripts))
        try:
            from _const import AK_STORE_FILE
            if AK_STORE_FILE.exists():
                data = json.loads(AK_STORE_FILE.read_text(encoding="utf-8"))
                ak = data.get("ak", "")
                result["configured"] = bool(ak)
                result["detail"] = f"ak_store.json 存在，长度 {len(ak)} 字符"
            else:
                result["detail"] = "ak_store.json 不存在"
        except Exception as e:
            result["detail"] = f"读取异常: {e}"
        finally:
            sys.path.pop(0)
            for m in ["_const", "_auth", "ak_crypto"]:
                sys.modules.pop(m, None)
    else:
        result["detail"] = "未找到 Skill scripts 目录"

    return result


def check_env_ak(label: str, key1: str, key2: str = "") -> dict:
    """检查环境变量类型的 AK"""
    v1 = os.environ.get(key1, "")
    v2 = os.environ.get(key2, "") if key2 else "N/A"

    if v1 and (v2 or not key2):
        detail = f"{key1} 已设置（长度 {len(v1)}）"
        if key2:
            detail += f"，{key2} 已设置（长度 {len(v2)}）"
        return {"type": label, "configured": True, "detail": detail}
    else:
        missing = [k for k, v in [(key1, v1), (key2, v2)] if k and not v]
        return {"type": label, "configured": False, "detail": f"未设置: {', '.join(missing)}"}


def cmd_status():
    """打印所有 AK 的配置状态"""
    print("📋 AK 配置状态\n")
    print("| 类型 | 状态 | 说明 |")
    print("|------|------|------|")

    checks = [
        check_1688_ak(),
        check_env_ak("AlphaShop AK/SK", "ALPHASHOP_ACCESS_KEY", "ALPHASHOP_SECRET_KEY"),
        check_env_ak("CRM AK/SK", "CRM_AK", "CRM_SK"),
    ]

    for c in checks:
        s = "✅ 已配置" if c["configured"] else "❌ 未配置"
        print(f"| {c['type']} | {s} | {c['detail']} |")

    ak = checks[0]
    if ak["skills"]:
        print(f"\n1688 Gateway AK 覆盖: {', '.join(ak['skills'])}")


def cmd_configure(ak_value: str):
    """通过 cli.py configure 配置 1688 AK"""
    skill_dir = find_skill_dir("1688-product-find") or find_skill_dir("1688-source-supplier")
    if not skill_dir:
        print("❌ 未找到 1688-product-find 或 1688-source-supplier")
        return False

    r = subprocess.run(
        ["python3", "cli.py", "configure", ak_value],
        cwd=str(skill_dir), capture_output=True, text=True, timeout=30
    )
    if r.stdout:
        print(r.stdout.strip())
    if r.returncode != 0 and r.stderr:
        print(f"⚠️  {r.stderr.strip()}")
    return r.returncode == 0


def cmd_verify():
    """验证 1688 AK 是否可用"""
    skill_dir = find_skill_dir("1688-product-find") or find_skill_dir("1688-source-supplier")
    if not skill_dir:
        print("❌ 未找到 Skill 目录")
        return False

    r = subprocess.run(
        ["python3", "cli.py", "configure", "--status"],
        cwd=str(skill_dir), capture_output=True, text=True, timeout=30
    )
    if r.stdout:
        print(r.stdout.strip())
    return r.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="1688 AK 管理器")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="查看所有 AK 配置状态")

    cfg = sub.add_parser("configure", help="配置 1688 Gateway AK")
    cfg.add_argument("ak", help="AK 值（Base64 编码）")

    sub.add_parser("verify", help="验证 1688 AK 是否可用")

    args = parser.parse_args()

    if args.command == "status":
        cmd_status()
    elif args.command == "configure":
        ok = cmd_configure(args.ak)
        sys.exit(0 if ok else 1)
    elif args.command == "verify":
        ok = cmd_verify()
        sys.exit(0 if ok else 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
