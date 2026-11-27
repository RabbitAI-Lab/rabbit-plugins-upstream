#!/usr/bin/env python3
"""YZL-AIoT 南向调试工具（yzl-aiot-south）v1.3.0

面向设备端联调：打印标准帧、直连设备服务器做 lgn/facs 探测、检查固件工程。
底层用同目录 `lib/south_client.py`（标准库实现），不依赖第三方包。

⚠️ 南向链路（TCP 41032 / UDP 40501 / MQTT 1883）为明文，无 TLS；
   仅用于内网 / APN / VPN 环境排障，不要在公网明文发送设备密码。
"""

import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "lib"))

from south_client import SouthDevice, SouthError  # noqa: E402

LOCAL_VERSION = "1.3.0"
SKILL_SLUG = "yzl-aiot-south"
CLAWHUB_REGISTRY = "https://clawhub.ai"
VERSION_CACHE_FILE = os.path.join(HERE, ".version_cache.json")
VERSION_CACHE_TTL = 12 * 3600

HELP = """YZL-AIoT 南向工具 v%s（aiot.yzlkj.com 设备端）

用法:
  python tool.py <命令> [参数]

命令:
  frames                         打印 lgn / facs / hear / order_conf / facs_reply 标准帧
  probe <设备ID> <密码> [--host H] [--port 41032] [--report key=value]
                                 连接设备服务器，发 lgn，可选发一条 facs
  report <设备ID> <密码> <key> <value> [--host H]
                                 登录后上报一个设施值
  check <固件目录>               检查工程是否接好 SDK（文件 + 回调 + 主循环）
  check-update                   检查技能版本（ClawHub）
  help / version

环境:
  ciot.yzlkj.com（测试）、siot.yzlkj.com（生产）；TCP 41032 / UDP 40501

示例:
  python tool.py frames
  python tool.py probe WANCD1-0000000007 123456 --report wd=25.3
  python tool.py check F:\\proj\\my_firmware

⚠️ 南向不适用北向 REST 的用户配额；上报节奏按 heartbeat_sec / keepalive_sec 设计。
""" % LOCAL_VERSION


def cmd_frames():
    dev = "WANCD1-0000000007"
    d = SouthDevice(dev, "PASSWORD")
    print("== TCP 41032（一行一帧，\\n 结尾）==")
    print("lgn        :", d.frame("lgn", ["PASSWORD"], "L1"))
    print("facs       :", d.frame("facs", ["wd", "25.3"], "F1"))
    print("hear       :", d.frame("hear", [], "H1"))
    print("order_conf :", d.frame("order_conf", ["T1"], "C1"))
    print("facs_reply :", d.frame("facs_reply", ["T1", dev, "sw", "1"], "F2"))
    print()
    print("== MQTT 1883（上行省略 top）==")
    print("up         :", json.dumps({"ter": dev, "data": [{"func": "facs", "args": ["kk1", "1"], "fid": "F1"}]},
                                    ensure_ascii=False, separators=(",", ":")))
    print()
    print("说明：lgn 成功后返回会话 token；未登录发业务返回 code=4；下行 tra 必须原样回传。")


def cmd_probe(dev_id, password, host, port, report=None):
    d = SouthDevice(dev_id, password, host=host, port=port, mode="tcp")
    print("→ %s:%s lgn %s" % (host, port, dev_id))
    try:
        d.connect()
        d.login()
        print("✅ 登录成功")
        if report:
            key, _, value = report.partition("=")
            if not key or not value:
                print("❌ --report 需要 key=value")
                return 1
            d.report(**{key: value})
            print("✅ 上报成功:", key, value)
        return 0
    except SouthError as e:
        print("❌ %s" % e)
        print("   检查：域名是否对应环境（ciot 测试 / siot 生产）、端口 41032、设备密码")
        return 1
    except OSError as e:
        print("❌ 连接失败：%s" % e)
        return 3
    finally:
        d.close()


REQUIRED_FILES = ("aiot_sdk.c", "aiot.h", "aiot_types.h")
CALLBACKS = ("aiot_client_connected", "aiot_client_rx", "aiot_client_poll", "aiot_client_disconnected")


def cmd_check(path):
    if not os.path.isdir(path):
        print("❌ 目录不存在：%s" % path)
        return 2
    files = []
    for root, _dirs, names in os.walk(path):
        if "__pycache__" in root:
            continue
        files.extend(names)
    print("目录：%s（%d 个文件）" % (path, len(files)))
    ok = True
    for f in REQUIRED_FILES:
        hit = f in files
        print(("✅" if hit else "❌"), "文件", f)
        ok = ok and hit
    texts = []
    for root, _dirs, names in os.walk(path):
        for n in names:
            if n.endswith((".c", ".h")):
                try:
                    with open(os.path.join(root, n), encoding="utf-8", errors="ignore") as fh:
                        texts.append(fh.read())
                except Exception:
                    pass
    blob = "\n".join(texts)
    for cb in CALLBACKS:
        hit = cb in blob
        print(("✅" if hit else "❌"), "回调", cb + "()")
        ok = ok and hit
    print(("✅" if "keepalive_sec" in blob else "⚠️"), "keepalive_sec 配置")
    print("\n结论：" + ("工程结构完整，可编译联调" if ok else "有缺失，按上面 ❌ 补齐"))
    return 0 if ok else 1


def _parse_version(text):
    parts = []
    for p in str(text).split("."):
        try:
            parts.append(int(p))
        except ValueError:
            parts.append(0)
    return tuple(parts)


def cmd_check_update():
    now = time.time()
    try:
        with open(VERSION_CACHE_FILE, encoding="utf-8") as f:
            cache = json.load(f)
    except Exception:
        cache = None
    if isinstance(cache, dict) and now - cache.get("cached_at", 0) < VERSION_CACHE_TTL:
        info = cache.get("result", {})
    else:
        info = {"local_version": LOCAL_VERSION, "latest_version": None, "error": None}
        try:
            req = urllib.request.Request("%s/api/v1/skills/%s" % (CLAWHUB_REGISTRY, SKILL_SLUG),
                                         headers={"User-Agent": "yzl-aiot-south/%s" % LOCAL_VERSION})
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            info["latest_version"] = (data.get("latestVersion") or {}).get("version")
        except Exception as e:
            info["error"] = str(e)
        try:
            with open(VERSION_CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump({"result": info, "cached_at": now}, f, ensure_ascii=False)
        except Exception:
            pass
    print("📡 %s：本地 v%s，远程 %s" % (SKILL_SLUG, info.get("local_version"),
                                   ("v" + info["latest_version"]) if info.get("latest_version") else "未发布/查询失败"))


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("help", "-h", "--help"):
        print(HELP)
        return 0
    cmd = args[0]
    if cmd == "version":
        print("yzl-aiot-south v%s" % LOCAL_VERSION)
        return 0
    if cmd == "frames":
        cmd_frames()
        return 0
    if cmd == "check-update":
        cmd_check_update()
        return 0
    if cmd == "probe":
        if len(args) < 3:
            print("用法: python tool.py probe <设备ID> <密码> [--host H] [--port 41032] [--report key=value]")
            return 2
        host, port, report = "ciot.yzlkj.com", 41032, None
        rest = args[3:]
        i = 0
        while i < len(rest):
            if rest[i] == "--host" and i + 1 < len(rest):
                host = rest[i + 1]; i += 2
            elif rest[i] == "--port" and i + 1 < len(rest):
                port = int(rest[i + 1]); i += 2
            elif rest[i] == "--report" and i + 1 < len(rest):
                report = rest[i + 1]; i += 2
            else:
                i += 1
        return cmd_probe(args[1], args[2], host, port, report)
    if cmd == "report":
        if len(args) < 5:
            print("用法: python tool.py report <设备ID> <密码> <key> <value> [--host H]")
            return 2
        host = "ciot.yzlkj.com"
        if "--host" in args:
            idx = args.index("--host")
            if idx + 1 < len(args):
                host = args[idx + 1]
        return cmd_probe(args[1], args[2], host, 41032, "%s=%s" % (args[3], args[4]))
    if cmd == "check":
        if len(args) < 2:
            print("用法: python tool.py check <固件目录>")
            return 2
        return cmd_check(args[1])
    print("❌ 未知命令: %s" % cmd)
    print(HELP)
    return 2


if __name__ == "__main__":
    sys.exit(main())
