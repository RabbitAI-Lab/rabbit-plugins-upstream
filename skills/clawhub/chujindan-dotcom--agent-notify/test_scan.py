#!/usr/bin/env python3
"""状态判定的边界用例。跑法：python3 test_scan.py

只测 _scan/_parse 这层纯逻辑，不起网络。全流程见 `notify.py selftest`。
"""
import importlib.util, json, os, tempfile, time

spec = importlib.util.spec_from_file_location(
    "n", os.path.join(os.path.dirname(os.path.abspath(__file__)), "notify.py"))
n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(n)

D = tempfile.mkdtemp()
P = os.path.join(D, "s.jsonl")
PAT = os.path.join(D, "*.jsonl")

USER = {"type": "user", "message": {"role": "user",
        "content": [{"type": "text", "text": "跑长任务"}]}}
BUSY = {"type": "assistant", "message": {"role": "assistant",
        "stop_reason": "tool_use", "content": [{"type": "tool_use"}]}}
DONE = {"type": "assistant", "message": {"role": "assistant",
        "stop_reason": "end_turn", "content": [{"type": "text", "text": "好了"}]}}
SUB = {"type": "assistant", "isSidechain": True, "message": {"role": "assistant",
       "stop_reason": "end_turn", "content": [{"type": "text", "text": "子agent说完了"}]}}


def write(rows):
    with open(P, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def scan(st):
    return n._scan(PAT, n._parse_claude, st, "claude-code")


def main():
    write([USER, BUSY]); st = {}
    assert scan(st) == [], "在干活时不该推送"

    old = time.time() - 11 * 60
    os.utime(P, (old, old))
    ev = scan(st)
    assert len(ev) == 1 and ev[0]["status"] == "stuck", ev
    assert "11 分钟" in ev[0]["detail"], ev
    assert scan(st) == [], "同一个卡死状态重复推送了"

    write([USER, BUSY, DONE])
    ev = scan(st)
    assert len(ev) == 1 and ev[0]["status"] == "done", ev
    assert ev[0]["task"] == "跑长任务" and ev[0]["time"], ev
    assert scan(st) == [], "done 重复推送了"

    # 播报原文：模板对得上，且 status/时间都已转成能念的中文
    t = ev[0]["text"]
    assert t.startswith("对了，你要我监测的") and t.endswith("，别忘了哦"), t
    assert "Claude Code" in t and "跑长任务" in t, t
    assert "已完成" in t and "done" not in t, f"status 没翻成中文: {t}"
    assert "点" in t and "T" not in t, f"时间没转成口语: {t}"

    # 子 agent 的 end_turn 不能被当成主线完成，否则每个 subagent 结束都播一次
    write([USER, BUSY, SUB])
    assert scan({}) == [], "子agent(isSidechain)的记录污染了主线判断"

    # 陈年老会话不该被翻出来重播
    old = time.time() - 7 * 3600
    write([USER, BUSY, DONE]); os.utime(P, (old, old))
    assert scan({}) == [], "扫到了超出活跃窗口的老会话"

    # 口语时间的几个边界：整点 / 零点 / 正午 / 下午
    from datetime import datetime as DT
    cases = {
        DT(2026, 9, 8, 0, 0): "凌晨12点整",
        DT(2026, 9, 8, 3, 5): "凌晨3点05分",
        DT(2026, 9, 8, 11, 9): "上午11点09分",
        DT(2026, 9, 8, 12, 30): "中午12点30分",
        DT(2026, 9, 8, 15, 0): "下午3点整",
        DT(2026, 9, 8, 21, 7): "晚上9点07分",
    }
    for dt, want in cases.items():
        got = n._spoken_time(dt)
        assert got == want, f"{dt} → {got}，期望 {want}"

    # 回归：上一轮 end_turn 之后用户又发了新消息，但模型还没写出第一条
    # assistant 记录。此时"最后一条 assistant"仍停在上一轮的 end_turn 上，
    # 而任务名已换成新问题——旧算法会抢先误播一句"该任务已完成"。
    # 真实 transcript 上复现过，窗口长达 35 秒，5 秒轮询必然命中。
    NEW_Q = {"type": "user", "message": {"role": "user",
             "content": [{"type": "text", "text": "新的问题"}]}}
    write([USER, BUSY, DONE, NEW_Q])
    state, task = n._parse_claude(P)
    assert state == "busy", f"新一轮刚开始却判成 {state}（旧 bug 回来了）"
    assert task == "新的问题", task
    assert scan({}) == [], "新一轮刚开始就误播了完成"

    # tool_result 也是 user 记录：工具刚回包 = 模型马上要接着干 = busy
    TR = {"type": "user", "message": {"role": "user",
          "content": [{"type": "tool_result", "content": "ok"}]}}
    write([USER, BUSY, DONE, NEW_Q, BUSY, TR])
    state, task = n._parse_claude(P)
    assert state == "busy", f"工具回包后判成 {state}"
    assert task == "新的问题", f"tool_result 被当成任务名了: {task}"

    # 回归：end_turn 之后文件被追加元数据（mtime 变了但判定没变），
    # 不能重复播报同一条"完成"。实测日志里连播过两次"播放了 已完成"。
    write([USER, BUSY, DONE]); st_dup = {}
    ev = scan(st_dup)
    assert len(ev) == 1, ev
    for _ in range(3):
        os.utime(P, None)                      # 模拟元数据追加，只动 mtime
        assert scan(st_dup) == [], "mtime 一变就重播了同一条完成"

    # 回归：斜杠命令输出、system-reminder 不是人说的话，不能当任务名念出来
    # 按标签形状识别，不是维护一张标签名单——名单永远追不上：刚加完
    # <local-command-stdout>，下一秒就冒出 <local-command-caveat>（实测）。
    assert n._is_user_speech("怎么写 <div> 标签"), "误伤了真人说的话"
    # harness 标签一律 ASCII 小写；没见过的新标签也该被挡
    assert not n._is_user_speech("<brand-new-harness-tag>x"), "新标签没被挡住"
    # 反过来，中文尖括号更可能是真人在说话，不该误伤
    assert n._is_user_speech("<标签>这句是我说的"), "误伤了中文内容"
    for junk in ("<local-command-stdout>Set effort level to high",
                 "<local-command-caveat>Caveat: The messages below",
                 "<system-reminder>foo</system-reminder>",
                 "<bash-input> curl http://x",
                 "<command-name>/rename</command-name>"):
        JUNK = {"type": "user", "message": {"role": "user",
                "content": [{"type": "text", "text": junk}]}}
        write([USER, JUNK, BUSY, DONE])
        _, task = n._parse_claude(P)
        assert task == "跑长任务", f"垃圾被当成任务名了: {task!r}"

    # 冷启动基线：seed 那一轮不该产出任何事件，但必须把状态记进 prev，
    # 否则守护进程一启动就把活跃窗口里的老会话全念一遍。
    write([USER, BUSY, DONE])
    st_seed = {}
    assert n._scan(PAT, n._parse_claude, st_seed, "claude-code", seed=True) == [], \
        "seed 轮不该推送"
    assert st_seed, "seed 轮没记录基线，下一轮会重复推"
    assert n._scan(PAT, n._parse_claude, st_seed, "claude-code") == [], \
        "基线建完后同一状态又推了一次"

    print("✓ test_scan 全部通过（含播报文案、口语时间边界、冷启动基线、新轮次不误播、不重播、任务名过滤）")


if __name__ == "__main__":
    main()
