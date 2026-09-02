#!/usr/bin/env python3
"""等用户在网页上答完题。

给 agent 用的:每次最多阻塞约 90 秒,没等到就带着进度返回,让 agent 再调一次。
这样不会撞上单条命令的超时上限,过程里还能看到进度。

退出码:
  0  收集完成(status == collected)—— 可以打分了
  2  还没完,agent 应该再调一次
  3  出错(session 不存在等)
"""

import json
import os
import sys
import time

import console  # noqa: F401  — 修 Windows GBK 控制台

ROOT = os.path.dirname(os.path.abspath(__file__))
SESSION_PATH = os.path.join(ROOT, "data", "session.json")

MAX_WAIT = 90.0
POLL = 2.0


def read_session():
    """server 用的是原子替换,但读到中间态还是兜一下。"""
    for _ in range(3):
        try:
            with open(SESSION_PATH, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            time.sleep(0.2)
    return None


def main():
    if not os.path.exists(SESSION_PATH):
        print("找不到 data/session.json —— 先生成题目再等。")
        return 3

    start = time.monotonic()
    last_n = -1

    while True:
        s = read_session()
        if s is None:
            print("session.json 读不出来(可能正在写),稍后重试。")
            return 2

        answers = s.get("answers", [])
        total = len(s.get("questions", []))
        n = len(answers)

        if s.get("status") == "collected":
            modes = [a.get("input_mode", "text") for a in answers]
            n_voice = modes.count("voice")
            print(f"✓ 全部 {n}/{total} 题已收集完成。")
            if n_voice:
                print(f"  其中 {n_voice} 题是语音输入。")
            print("  可以打分了。")
            return 0

        if n != last_n:  # 有新进展就打一行,方便用户看到在动
            print(f"  已答 {n}/{total} …")
            last_n = n

        if time.monotonic() - start >= MAX_WAIT:
            print(f"仍在等待:{n}/{total} 题已答。继续等下一轮。")
            return 2

        time.sleep(POLL)


if __name__ == "__main__":
    sys.exit(main())
