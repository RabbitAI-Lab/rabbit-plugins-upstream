#!/usr/bin/env python3
"""南向示例（Python）：登录 + 上报，使用技能自带 lib/south_client.py。

用法：
    set AIOT_DEVICE=WANCD1-0000000007
    set AIOT_DEVICE_PASSWORD=123456
    python probe.py
    python probe.py --report wd=25.3 --host siot.yzlkj.com
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib"))

from south_client import SouthDevice, SouthError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default=os.environ.get("AIOT_HOST", "ciot.yzlkj.com"))
    ap.add_argument("--port", type=int, default=41032)
    ap.add_argument("--report", default=None, help="key=value")
    args = ap.parse_args()

    dev = os.environ.get("AIOT_DEVICE", "")
    pwd = os.environ.get("AIOT_DEVICE_PASSWORD", "")
    if not dev or not pwd:
        print("请先设置 AIOT_DEVICE / AIOT_DEVICE_PASSWORD")
        return 2

    d = SouthDevice(dev, pwd, host=args.host, port=args.port)
    print("→ %s:%s lgn %s" % (args.host, args.port, dev))
    try:
        d.connect()
        d.login()
        print("✅ 登录成功")
        if args.report:
            key, _, value = args.report.partition("=")
            d.report(**{key: value})
            print("✅ 上报成功:", key, value)
    except SouthError as e:
        print("❌", e)
        return 1
    finally:
        d.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
