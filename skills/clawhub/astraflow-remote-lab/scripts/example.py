#!/usr/bin/env python3
"""星图 AstraFlow 桌面沙箱的环境自检示例。"""

import os
import sys

def main():
    print("=== 星图 AstraFlow 桌面沙箱环境检查 ===")
    try:
        import ucloud_sandbox
        ver = getattr(ucloud_sandbox, "__version__", "已安装")
        print(f"[OK] Python SDK 'ucloud-sandbox' 已安装（版本 {ver}）。")
    except ImportError:
        print("[FAIL] 缺少 Python SDK 'ucloud-sandbox'，请执行：pip install ucloud-sandbox")

    key = os.environ.get("UCLOUD_SANDBOX_API_KEY")
    reg = os.environ.get("UCLOUD_SANDBOX_REGION", "us-ca（默认）")
    if not key:
        print("[WARN] UCLOUD_SANDBOX_API_KEY 未设置。")
        print("       请在 AstraFlow Key Management 页面获取后执行：")
        print("       export UCLOUD_SANDBOX_API_KEY=\"<你的-api-key>\"")
    else:
        # 不打印 key 长度或内容，避免泄露凭据元信息
        print(f"[OK] UCLOUD_SANDBOX_API_KEY 已配置（目标地域：{reg}）。")

if __name__ == "__main__":
    main()
