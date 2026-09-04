#!/usr/bin/env python3
"""端到端冒烟测试。起 server 前先跑一遍能省很多调试时间。

用法:先 cp data/session.example.json data/session.json,起 server,再跑这个。
"""
import json
import os
import sys
import urllib.error
import urllib.request

import console  # noqa: F401  — 修 Windows GBK 控制台

BASE = os.environ.get("MI_BASE", "http://127.0.0.1:8787")

ANSWERS = [
    ("q1", "当时线上订单查询 p99 到了 800ms,大促前压测发现的。我测了本地缓存、"
           "Redis、多级缓存三种方案,最后选 Redis,因为服务有 4 个实例。", "voice", 96),
    ("q2", "压测环境测的,5000 QPS 打了十分钟,用 wrk。上线后也看了一周真实流量。",
     "text", None),
    ("q3", "代码是我一个人写的,方案设计过了组内评审,上线是 mentor 陪着做的。",
     "voice", 74),
    ("q4", "第一版忘了处理缓存穿透,压测时打到库上了。加了空值缓存和布隆过滤器。",
     "text", None),
    ("q5", "4 个实例各自持有本地缓存,订单状态更新后其他 3 个实例还是旧值,"
           "用户刷新可能看到已支付又变回待支付。", "voice", 112),
]


def post(payload):
    req = urllib.request.Request(
        BASE + "/api/answer",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, json.load(e)


def main():
    try:
        with urllib.request.urlopen(BASE + "/api/session", timeout=5) as r:
            session = json.load(r)
    except OSError as e:
        print(f"✗ 连不上 {BASE} —— server 起了吗?({e})")
        return 1

    print(f"✓ session: {session['total']} 题,已答 {len(session['answered'])}")

    todo = [a for a in ANSWERS if a[0] not in session["answered"]]
    if not todo:
        print("  所有题都答过了,没得测。重置:cp data/session.example.json data/session.json")
        return 0

    for qid, text, mode, dur in todo:
        payload = {"qid": qid, "text": text, "input_mode": mode}
        if dur is not None:
            payload["duration_sec"] = dur
        status, body = post(payload)
        if status != 200:
            print(f"✗ {qid} 提交失败 [{status}]: {body}")
            return 1
        flag = "  ← all_done" if body.get("all_done") else ""
        print(f"✓ {qid} [{mode}] {body['answered']}/{body['total']}{flag}")
        if body.get("all_done"):
            print(f"  message: {body['message']}")

    # 落盘校验:中文有没有被写坏
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "data", "session.json")
    with open(path, encoding="utf-8") as f:
        s = json.load(f)
    print(f"\n✓ status = {s['status']}")
    modes = [a.get("input_mode") for a in s["answers"]]
    print(f"✓ 落盘 {len(s['answers'])} 条,voice={modes.count('voice')} "
          f"text={modes.count('text')}")
    first = s["answers"][0]["text"]
    assert "p99" in first and "缓存" in first, "中文落盘损坏!"
    print(f"✓ 中文完好:{first[:24]}…")
    return 0


if __name__ == "__main__":
    sys.exit(main())
