# -*- coding: utf-8 -*-
"""一键全量回归入口（R9 起）。

依次运行：计分引擎定向用例 → 集成测试 → 构建干跑 → 状态机干跑 → 多维量表干跑。
任一失败即停止并返回非 0 退出码。

用法：python tests/run_all.py
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SCRIPTS = [
    os.path.join("tests", "test_scoring_cases.py"),
    os.path.join("tests", "integration_test.py"),
    os.path.join("tests", "dryrun", "build_dryrun.py"),
    os.path.join("tests", "dryrun", "r7_dryrun.py"),
    os.path.join("tests", "dryrun", "r8_multidim.py"),
]

ENV = dict(os.environ)
ENV.setdefault("PYTHONIOENCODING", "utf-8")


def main():
    failed = []
    for rel in SCRIPTS:
        p = os.path.join(ROOT, rel)
        print(f"\n{'=' * 60}\n▶ {rel}\n{'=' * 60}")
        if not os.path.exists(p):
            print(f"  跳过（不存在）：{p}")
            continue
        proc = subprocess.run([sys.executable, p], cwd=ROOT, env=ENV)
        if proc.returncode != 0:
            failed.append(rel)
            print(f"\n✗ {rel} 失败（exit={proc.returncode}）")
            break
        print(f"✓ {rel} 通过")
    if failed:
        print(f"\n全量回归未通过：{failed}")
        sys.exit(1)
    print("\n全量回归 5/5 全部通过 ✓")


if __name__ == "__main__":
    main()
