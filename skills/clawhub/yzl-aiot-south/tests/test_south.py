#!/usr/bin/env python3
"""南向离线自测：起本地 mock TCP 服务器，跑 lib/south_client.py 的所有方法。

运行：python tests/test_south.py
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "lib"))
sys.path.insert(0, HERE)

from mock_south import MockSouth  # noqa: E402
from south_client import SouthDevice  # noqa: E402

PASS = 0
FAIL = 0


def check(name, cond, extra=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  ✅", name)
    else:
        FAIL += 1
        print("  ❌", name, extra)


def main():
    srv = MockSouth()
    srv.start()
    d = SouthDevice("DEV-1", "pw", host="127.0.0.1", port=srv.port)
    d.connect()
    try:
        check("lgn", d.login().get("result") == "SESSION-1")
        check("facs", d.report(wd="25.3") is not None)
        check("facs args", srv.frames[-1]["data"][0]["args"] == ["wd", "25.3"])
        d.heartbeat()
        check("hear args", srv.frames[-1]["data"][0]["args"] == [])
        check("get_time", d.get_time() == "2026-11-04 01:05:14")
        d.order_conf("tra-1")
        check("order_conf", srv.frames[-1]["data"][0]["args"] == ["tra-1"])
        d.order_reply("tra-1", sw="1")
        check("facs_reply", srv.frames[-1]["data"][0]["args"] == ["tra-1", "DEV-1", "sw", "1"])
        d.backfill([{"ts": 1792714948, "values": {"kk1": "11"}},
                    {"ts": 1792716748, "values": {"kk1": "12"}}])
        check("facs_his 时间戳为数字", srv.frames[-1]["data"][0]["args"][0] == 1792714948)
        check("gfinfo", d.ota_info("fw_1")["result"]["version"] == "1.0")
        check("gfcet", d.ota_get("fw_1", 0)["result"]["no"] == 0)

        # 平台下行 order → 设备确认 + 回执
        srv.push_order("tra-9", ["DEV-1", "sw", "1"])
        msg = d.recv(timeout=3)
        check("收到 order", msg.get("top") == "order" and msg["data"][0]["tra"] == "tra-9")
        d.order_conf("tra-9")
        d.order_reply("tra-9", sw="1")
        check("order_conf 已发", srv.frames[-2]["data"][0]["func"] == "order_conf")
        check("facs_reply 已发", srv.frames[-1]["data"][0]["func"] == "facs_reply")
    finally:
        d.close()

    print("\n结果: %d passed, %d failed" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
