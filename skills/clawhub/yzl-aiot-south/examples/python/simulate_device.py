#!/usr/bin/env python3
"""南向示例（Python）：假设备模拟器（技能自带 lib/south_client.py）。

行为：
  1) TCP 连接 → lgn；
  2) 每 N 秒上报一次 facs（温度正弦变化）；
  3) 收到下行 order 时，自动 order_conf + facs_reply。

用法：
    set AIOT_DEVICE=WANCD1-0000000007
    set AIOT_DEVICE_PASSWORD=123456
    python simulate_device.py
    python simulate_device.py --host siot.yzlkj.com --interval 60
"""
import argparse
import math
import os
import sys
import threading
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lib"))

from south_client import SouthDevice, SouthError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default=os.environ.get("AIOT_HOST", "ciot.yzlkj.com"))
    ap.add_argument("--port", type=int, default=41032)
    ap.add_argument("--interval", type=float, default=float(os.environ.get("AIOT_REPORT_INTERVAL", "30")))
    args = ap.parse_args()

    dev = os.environ.get("AIOT_DEVICE", "")
    pwd = os.environ.get("AIOT_DEVICE_PASSWORD", "")
    if not dev or not pwd:
        print("请先设置 AIOT_DEVICE / AIOT_DEVICE_PASSWORD")
        return 2

    d = SouthDevice(dev, pwd, host=args.host, port=args.port)
    d.connect()
    d.login()
    print("已连接 %s:%s，设备 %s，每 %.0fs 上报一次" % (args.host, args.port, dev, args.interval))

    stop = threading.Event()

    def reporter():
        t0 = time.time()
        while not stop.is_set():
            value = "%.1f" % (25.0 + 3.0 * math.sin((time.time() - t0) / 30.0))
            try:
                d.report(wd=value)
                print("↑ facs wd=", value)
            except SouthError as e:
                print("上报失败:", e)
            time.sleep(args.interval)

    threading.Thread(target=reporter, daemon=True).start()

    def on_order(cmd, args_list):
        print("↓ order", cmd, args_list)
        return {"sw": str(args_list[-1])} if args_list else {"sw": "1"}

    try:
        d.serve_forever(on_order=on_order, heartbeat_every=60)
    except KeyboardInterrupt:
        print("\n退出")
    finally:
        stop.set()
        d.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
