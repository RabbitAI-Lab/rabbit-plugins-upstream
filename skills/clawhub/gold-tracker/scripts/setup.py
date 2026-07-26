#!/usr/bin/env python3
"""
黄金追踪 - 环境初始化脚本
安装技能后运行此脚本完成环境搭建。
零第三方依赖。
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TZ_BEIJING = timezone(timedelta(hours=8))

REQUIRED_DIRS = ["scripts", "logs", "archive", "alerts", ".cache"]
REQUIRED_SCRIPTS = [
    "fetch.py", "validate.py", "normalize.py",
    "summary.py", "alert_manager.py", "archive_manager.py",
]
REQUIRED_FILES = ["config.yaml", "SKILL.md", "skill.yaml"]

errors = []
warnings = []
steps_done = 0


def ok(msg):
    global steps_done
    steps_done += 1
    print(f"  [✓] {msg}")


def fail(msg):
    errors.append(msg)
    print(f"  [✗] {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  [!] {msg}")


def check_python():
    print("\n[1/5] 检查 Python 环境...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        fail(f"Python {version.major}.{version.minor} 不满足要求 (>=3.8)")
        return False
    ok(f"Python {version.major}.{version.minor}.{version.micro}")
    return True


def create_dirs():
    print("\n[2/5] 创建目录结构...")
    for d in REQUIRED_DIRS:
        dir_path = ROOT / d
        if dir_path.exists():
            ok(f"{d}/ 已存在")
        else:
            dir_path.mkdir(parents=True, exist_ok=True)
            ok(f"{d}/ 已创建")
    return True


def check_files():
    print("\n[3/5] 检查核心文件...")
    all_present = True
    for f in REQUIRED_FILES:
        if (ROOT / f).exists():
            ok(f"{f}")
        else:
            fail(f"{f} 缺失")
            all_present = False

    for s in REQUIRED_SCRIPTS:
        script_path = ROOT / "scripts" / s
        if script_path.exists():
            if not os.access(script_path, os.X_OK):
                try:
                    script_path.chmod(0o755)
                    ok(f"scripts/{s} (已添加执行权限)")
                except Exception:
                    warn(f"scripts/{s} 无法设置执行权限")
            else:
                ok(f"scripts/{s}")
        else:
            fail(f"scripts/{s} 缺失")
            all_present = False

    return all_present


def init_state():
    print("\n[4/5] 初始化状态文件...")
    state_file = ROOT / "state.json"

    if state_file.exists():
        try:
            data = json.loads(state_file.read_text())
            if "current_price" in data and "last_update" in data:
                ok("state.json 已存在且有效，跳过初始化")
                return True
        except Exception:
            warn("state.json 存在但格式错误，将重新创建")

    now = datetime.now(TZ_BEIJING)
    initial_state = {
        "date": now.strftime("%Y-%m-%d"),
        "current_price": 0.0,
        "last_price": 0.0,
        "change_pct": 0.0,
        "change_abs": 0.0,
        "price_cny_per_gram": 0.0,
        "usd_cny": 0.0,
        "last_update": now.isoformat(),
        "sources": {},
        "key_data": {},
    }
    state_file.write_text(json.dumps(initial_state, indent=2, ensure_ascii=False))
    ok("state.json 已初始化（首次 fetch 后将填入真实数据）")
    return True


def run_health_check():
    print("\n[5/5] 运行健康检查...")
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate.py")],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            ok("validate.py 通过")
        else:
            warn("validate.py 报告错误（首次安装时部分警告正常）")
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    print(f"       {line}")
    except Exception as e:
        warn(f"无法运行 validate.py: {e}")

    return True


def print_summary():
    print("\n" + "=" * 56)
    if errors:
        print(f"初始化失败: {len(errors)} 个错误")
        for e in errors:
            print(f"  - {e}")
        print("\n请修复上述错误后重新运行: python3 scripts/setup.py")
        sys.exit(1)

    print(f"初始化完成! {steps_done} 步全部通过")
    if warnings:
        print(f"({len(warnings)} 个警告，不影响使用)")
    print("=" * 56)
    print("\n下一步:")
    print("  1. 获取数据:  python3 scripts/fetch.py")
    print("  2. 检查提醒:  python3 scripts/alert_manager.py detect")
    print("  3. 生成简报:  python3 scripts/summary.py brief")
    print("  4. 完整流程参考 SKILL.md「运行流程」章节")
    print()


def main():
    print("=" * 56)
    print("黄金追踪 - 环境初始化")
    print(f"项目路径: {ROOT}")
    print("=" * 56)

    check_python()
    create_dirs()
    check_files()
    init_state()
    run_health_check()
    print_summary()


if __name__ == "__main__":
    main()
