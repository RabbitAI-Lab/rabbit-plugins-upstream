#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_env.py — 检查技能分发所需环境与登录态
用法: python check_env.py [--skill <技能目录>]
"""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

HOME_CONFIG_DIR = Path.home() / ".skill-distributor"


def which(name):
    return shutil.which(name) is not None


def check_git():
    if not which("git"):
        return "✗ git 未安装"
    ver = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
    name = subprocess.run(["git", "config", "--global", "user.name"], capture_output=True, text=True).stdout.strip()
    email = subprocess.run(["git", "config", "--global", "user.email"], capture_output=True, text=True).stdout.strip()
    parts = [f"✓ {ver}"]
    if name:
        parts.append(f"身份: {name}")
    if email:
        parts.append(f"<{email}>")
    if not (name and email):
        parts.append("⚠ 未配置 git 全局身份（发布前需在 config.json identity 填写或 git config 设置）")
    return " | ".join(parts)


def check_cli(name, login_hint):
    if which(name):
        return f"✓ {name} CLI 已安装"
    return f"✗ {name} CLI 未安装（{login_hint}）"


def check_secrets():
    results = []
    env_vars = ["GITHUB_TOKEN", "CLAWHUB_AUTH", "SKILLHUB_TOKEN", "MIRROR_URLS"]
    for v in env_vars:
        import os
        if os.environ.get(v):
            results.append(f"✓ 环境变量 {v} 已设置")
    if HOME_CONFIG_DIR.joinpath("secrets.json").exists():
        try:
            data = json.loads(HOME_CONFIG_DIR.joinpath("secrets.json").read_text(encoding="utf-8"))
            keys = [k for k, val in data.items() if val]
            results.append(f"✓ secrets.json 存在，含密钥: {', '.join(keys) if keys else '无'}")
        except Exception:
            results.append("⚠ secrets.json 存在但解析失败")
    if not any("已设置" in r or "存在" in r for r in results):
        results.append("⚠ 未检测到任何密钥（GITHUB_TOKEN 必须配置）")
    return "\n    ".join(results) if results else ""


def main():
    parser = argparse.ArgumentParser(description="检查技能分发环境")
    parser.add_argument("--skill", default="", help="技能目录（可选，用于检查 SKILL.md）")
    args = parser.parse_args()

    print("== skill-distributor 环境检查 ==")
    print(f"[git]      {check_git()}")
    print(f"[clawhub]  {check_cli('clawhub', 'npm install -g clawhub && clawhub login')}")
    print(f"[mcp-publisher] {check_cli('mcp-publisher', '安装后执行 mcp-publisher login github')}")
    print(f"[skillhub] {check_cli('skillhub', '按腾讯 SkillHub 官方 CLI 安装并登录')}")
    secrets = check_secrets()
    if secrets:
        print(f"[secrets]  {secrets}")

    if args.skill:
        skill_dir = Path(args.skill).resolve()
        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            print(f"[skill]    ✓ 技能包有效: {skill_dir}")
        else:
            print(f"[skill]    ✗ {skill_dir} 下缺少 SKILL.md")

    print("\n提示: 缺失项不影响其他平台发布；GITHUB_TOKEN 为必选项。")


if __name__ == "__main__":
    main()
