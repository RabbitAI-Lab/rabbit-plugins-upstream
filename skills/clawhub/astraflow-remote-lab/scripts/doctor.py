#!/usr/bin/env python3
"""运行星图 AstraFlow 桌面沙箱的环境与前置条件综合自检。"""

import os
import shutil
import sys
from urllib.parse import urlparse


def check_python_runtime():
    v = sys.version_info
    print(f"[INFO] 当前 Python 运行时：{v.major}.{v.minor}.{v.micro}")
    if v.major < 3 or (v.major == 3 and v.minor < 8):
        print("[FAIL] 需要 Python 3.8+，请升级你的 Python 运行时。")
        return False
    print("[OK] Python 运行时版本满足要求（>=3.8）。")
    return True


def check_sdk():
    try:
        import ucloud_sandbox
        ver = getattr(ucloud_sandbox, "__version__", "已安装")
        print(f"[OK] Python SDK 'ucloud-sandbox' 已就绪（版本：{ver}）。")
        return True
    except ImportError:
        print("[FAIL] 缺少 Python SDK 'ucloud-sandbox'。")
        print("       请使用以下命令安装：pip install \"ucloud-sandbox>=1.5.0\"")
        return False


def check_credentials():
    key = os.environ.get("UCLOUD_SANDBOX_API_KEY")
    reg = os.environ.get("UCLOUD_SANDBOX_REGION", "us-ca（默认）")
    if not key:
        print("[WARN] 环境变量 UCLOUD_SANDBOX_API_KEY 未配置。")
        print("请在 AstraFlow Key Management 页面创建并复制你的专属 Key：")
        print("    🔑 https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl")
        print("       安全注入：export UCLOUD_SANDBOX_API_KEY=\"<你的-api-key>\"")
        return False

    print(f"[OK] UCLOUD_SANDBOX_API_KEY 已配置。（目标地域：{reg}）")
    return True


def main():
    print("=== 星图 AstraFlow 桌面沙箱环境自检 ===\n")
    s1 = check_python_runtime()
    s2 = check_sdk()
    s3 = check_credentials()
    print("\n====================================================")
    if s1 and s2 and s3:
        print("🎉 环境校验通过，可以启动沙箱。")
    else:
        print("⚠️  校验未完成，请处理上述缺失项。")


if __name__ == "__main__":
    main()
