#!/usr/bin/env python3
"""
Stoic Coach 数据引擎
记录、统计、洞察、语录、导出——纯 Python 标准库实现，无第三方依赖。

用法：
  stoic.py log --exercise-id 1 --state-before 7 --state-after 4 \
      --insight "..." --tags 焦虑,工作 --duration 10
  stoic.py reflect --uncontrollable "..." --controllable "..." --context 绩效
  stoic.py map
  stoic.py morning --difficulty "..." --plan "..." [--principle "今日准则"]
  stoic.py evening --progress "..." --let-go "..." --next "..."
  stoic.py weekly [--days 7]
  stoic.py history [--limit N]
  stoic.py stats
  stoic.py insight
  stoic.py recommend [--mood 焦虑|愤怒|低落|反刍|疲惫|...]
  stoic.py daily
  stoic.py export --format md|json [--output FILE]
"""

import argparse
import json
import os
import sys
import uuid
from datetime import date, datetime, timedelta

# ---------------------------------------------------------------------------
# 常量与元数据
# ---------------------------------------------------------------------------

DATA_DIR = os.environ.get(
    "STOIC_COACH_DATA_DIR",
    os.path.join(os.path.expanduser("~"), ".stoic-coach"),
)
JOURNAL_FILE = os.path.join(DATA_DIR, "journal.jsonl")

MODULES = {
    1: "控制二分法",
    2: "四大美德",
    3: "正念与智慧模式",
    4: "热爱命运与全然接纳",
    5: "韧性训练",
}

EXERCISES = {
    1:  ("拆分担忧", 1), 2:  ("命运许可保留条款", 1),
    3:  ("耐受不确定性六问", 1), 4:  ("逃出猴子陷阱", 1),
    5:  ("价值观澄清", 2), 6:  ("美德自评", 2),
    7:  ("人际交往复盘", 2), 8:  ("识别愤怒苗头", 2),
    9:  ("择善而从（贤人模仿法）", 2), 10: ("撰写自己的沉思录", 2),
    11: ("斯多葛正念练习", 3), 12: ("冲动行为复盘", 3),
    13: ("智慧模式四要素自检", 3),
    14: ("全然接纳", 4), 15: ("背诵斯多葛语录", 4),
    16: ("辩证法双视角陈述", 4), 17: ("责任分类法", 4),
    18: ("拒绝接纳的成本核算", 4),
    19: ("自愿不适暴露", 5), 20: ("从高处着眼（认知距离法）", 5),
    21: ("适应不适练习", 5), 22: ("灾难化检验", 5),
    23: ("预设逆境", 5), 24: ("勿忘你终有一死（memento mori）", 5),
    25: ("放手练习", 5), 26: ("第二支箭（两层痛苦拆解）", 5),
}

# 情绪信号 → 练习映射（与 references/exercises.md 状态速查表一致）
MOOD_MAP = {
    "焦虑": [1, 3, 22, 23],
    "担忧": [1, 3, 22, 23],
    "愤怒": [8, 12],
    "烦躁": [8, 12],
    "低落": [24, 10, 5],
    "迷茫": [24, 10, 5],
    "抗拒": [14, 16, 18, 17],
    "不公平": [14, 16, 18, 17],
    "放不下": [25, 4],
    "冲动": [19, 21],
    "乱": [11, 26],
    "反刍": [26, 20, 1],
    "人际": [7, 17, 9],
    "习惯": [2, 13, 6],
    "疲惫": [],
    "低电量": [],
}

# 各模块的入门代表练习（用于覆盖度推荐）
MODULE_ENTRY = {1: 1, 2: 6, 3: 11, 4: 14, 5: 20}

QUOTES_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "references", "quotes.md"
)


def exercise_name(eid: int) -> str:
    return EXERCISES[eid][0] if eid in EXERCISES else f"练习{eid}"


def module_name(eid: int) -> str:
    mid = EXERCISES[eid][1] if eid in EXERCISES else 0
    return MODULES.get(mid, "未知模块")


# ---------------------------------------------------------------------------
# 存储层
# ---------------------------------------------------------------------------

def load_entries():
    if not os.path.exists(JOURNAL_FILE):
        return []
    entries = []
    with open(JOURNAL_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries


def save_entry(entry: dict) -> dict:
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(JOURNAL_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def load_practice_entries():
    """只取练习记录（无 type 或 type=practice；过滤 reflection/morning/evening）。"""
    return [e for e in load_entries() if e.get("type", "practice") == "practice"]


def load_by_type(entry_type: str):
    """按类型取记录：practice / reflection / morning / evening。"""
    return [e for e in load_entries() if e.get("type", "practice") == entry_type]


def load_reflections():
    """只取困境地图的看清记录。"""
    return [e for e in load_entries() if e.get("type") == "reflection"]


# ---------------------------------------------------------------------------
# 命令实现
# ---------------------------------------------------------------------------

def cmd_log(args):
    eid = args.exercise_id
    if eid not in EXERCISES:
        print(f"❌ 无效的练习编号 {eid}（有效范围 1-{len(EXERCISES)}）")
        return 1
    entry = {
        "id": uuid.uuid4().hex[:8],
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "date": date.today().isoformat(),
        "exercise_id": eid,
        "exercise_name": exercise_name(eid),
        "module": module_name(eid),
        "state_before": args.state_before,
        "state_after": args.state_after,
        "insight": args.insight or "",
        "tags": [t.strip() for t in (args.tags or "").split(",") if t.strip()],
        "duration_min": args.duration,
    }
    save_entry(entry)
    print(f"✅ 已记录：[{entry['module']}] {entry['exercise_name']}")
    if entry["state_before"] is not None and entry["state_after"] is not None:
        improved = entry["state_before"] - entry["state_after"]
        change = f"（不适程度改善 {improved:+d} 分）" if improved else "（持平）"
        print(f"   状态 {entry['state_before']} → {entry['state_after']} {change}")
    if entry["insight"]:
        print(f"   心得：{entry['insight']}")
    return 0


def cmd_reflect(args):
    if not args.uncontrollable and not args.controllable:
        print("❌ 至少要有一条不可控或可控的记录（--uncontrollable / --controllable）")
        return 1
    entry = {
        "id": uuid.uuid4().hex[:8],
        "type": "reflection",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "date": date.today().isoformat(),
        "uncontrollable": args.uncontrollable or "",
        "controllable": args.controllable or "",
        "context": args.context or "",
    }
    if args.exercise:
        if args.exercise not in EXERCISES:
            print(f"⚠️ 练习编号 {args.exercise} 不在 1-{len(EXERCISES)} 范围内，已忽略来源关联。")
        else:
            entry["source_exercise"] = exercise_name(args.exercise)
    save_entry(entry)
    print("✅ 已看清，并存档：")
    if entry["uncontrollable"]:
        print(f"   不可控：{entry['uncontrollable']}")
    if entry["controllable"]:
        print(f"   可控：{entry['controllable']}")
    if entry["context"]:
        print(f"   场景：{entry['context']}")
    if entry.get("source_exercise"):
        print(f"   来自练习：{entry['source_exercise']}")
    return 0


def cmd_map(_args):
    reflections = load_reflections()
    if not reflections:
        print("🗺️ 还没有「看清」的记录。")
        print("   下次练习收尾时，试着说出这次看清的一件不可控，和一个对应的小动作。")
        return 0
    uns = [r for r in reflections if r.get("uncontrollable")]
    cs = [r for r in reflections if r.get("controllable")]
    print(f"🗺️ 你的困境地图（{len(reflections)} 次看清）\n" + "─" * 40)
    print(f"\n【不可控的事】{len(uns)} 条——看清它们，就不再替它们负责：")
    for r in reversed(uns):
        ctx = f" · {r['context']}" if r.get("context") else ""
        print(f"  · {r['uncontrollable']}（{r['date']}{ctx}）")
    print(f"\n【可控的动作】{len(cs)} 条——大小不重要，重要的是真的做：")
    for r in reversed(cs):
        ctx = f" · {r['context']}" if r.get("context") else ""
        print(f"  · {r['controllable']}（{r['date']}{ctx}）")
    if not cs:
        print("  （还没有。下次收尾时，为一件事找一个你能做的小动作。）")
    print("\n（不可控不是失败，看清它就是进步；可控不在大小，在于真的去做。）")
    return 0


def cmd_history(args):
    entries = load_practice_entries()
    if not entries:
        print("📚 还没有任何练习记录。第一次练习从现在开始。")
        return 0
    entries = entries[-args.limit:]
    print(f"📖 最近 {len(entries)} 条记录：\n")
    for e in reversed(entries):
        change = ""
        if e.get("state_before") is not None and e.get("state_after") is not None:
            d = e["state_before"] - e["state_after"]  # 正数=不适改善
            change = f"｜不适 {e['state_before']}→{e['state_after']}（改善{d:+d}）" if d else f"｜不适 {e['state_before']}→{e['state_after']}"
        print(f"· {e['date']} [{e['module']}] {e['exercise_name']}{change}")
        if e.get("insight"):
            print(f"  └ “{e['insight']}”")
    return 0


def cmd_stats(_args):
    entries = load_practice_entries()
    if not entries:
        print("📊 还没有数据。练一次，再来找我。")
        return 0

    dates = sorted({e["date"] for e in entries})
    # 连续天数（截至今天或最近一次练习）
    streak, cursor = 0, date.today()
    ds = set(dates)
    if date.today().isoformat() not in ds:  # 今天没练，从最近一天起算
        latest = datetime.strptime(dates[-1], "%Y-%m-%d").date()
        cursor = latest
    while cursor.isoformat() in ds:
        streak += 1
        cursor -= timedelta(days=1)

    mod_count = {}
    ex_count = {}
    for e in entries:
        mod_count[e["module"]] = mod_count.get(e["module"], 0) + 1
        ex_count[e["exercise_name"]] = ex_count.get(e["exercise_name"], 0) + 1

    # 正数 = 不适程度下降（改善）
    deltas = [e["state_before"] - e["state_after"] for e in entries
              if e.get("state_before") is not None and e.get("state_after") is not None]

    print("📊 练习总览\n" + "─" * 36)
    print(f"总练习次数：{len(entries)} 次")
    print(f"覆盖天数：{len(dates)} 天（首次 {dates[0]}，最近 {dates[-1]}）")
    print(f"连续练习：{streak} 天")
    if deltas:
        avg = sum(deltas) / len(deltas)
        print(f"不适改善：平均 {avg:+.1f} 分（{len(deltas)} 次有前后对比）")
        print(f"练后感觉更好：{sum(1 for d in deltas if d > 0)}/{len(deltas)} 次")
    print(f"涉及练习：{len(ex_count)} 种 / {len(EXERCISES)} 种")

    print("\n模块分布：")
    for m in sorted(mod_count, key=mod_count.get, reverse=True):
        bar = "█" * mod_count[m]
        print(f"  {m}：{bar} {mod_count[m]}")

    top = sorted(ex_count.items(), key=lambda x: -x[1])[:3]
    if top:
        print("\n最常练：")
        for name, n in top:
            print(f"  · {name}（{n} 次）")

    reflections = load_reflections()
    if reflections:
        print(f"\n看清记录：{len(reflections)} 条（用 map 查看你的困境地图）")
    return 0


def cmd_insight(_args):
    entries = load_practice_entries()
    reflections = load_reflections()
    if len(entries) < 2 and len(reflections) < 2:
        print("🔍 记录还太少（至少 2 条才能看出模式）。多练几次，我再帮你照镜子。")
        return 0
    if not entries:
        print("🔍 看清记录已有，练习记录还太少——练几次，我再帮你照镜子。")
        return 0

    print("🔍 自我洞察报告\n" + "═" * 40)
    dates = sorted({e["date"] for e in entries})
    ds = set(dates)

    # 连续天数
    streak, cursor = 0, date.today()
    if date.today().isoformat() not in ds:
        cursor = datetime.strptime(dates[-1], "%Y-%m-%d").date()
    while cursor.isoformat() in ds:
        streak += 1
        cursor -= timedelta(days=1)

    # 模块分布
    mod_count = {}
    for e in entries:
        mod_count[e["module"]] = mod_count.get(e["module"], 0) + 1
    total = len(entries)
    dominant = max(mod_count, key=mod_count.get)
    dom_pct = mod_count[dominant] / total * 100

    # 练习有效性（正数 = 改善）
    eff = {}
    for e in entries:
        if e.get("state_before") is None or e.get("state_after") is None:
            continue
        eff.setdefault(e["exercise_name"], []).append(
            e["state_before"] - e["state_after"])
    best = max(
        ((n, sum(v) / len(v), len(v)) for n, v in eff.items() if len(v) >= 1),
        key=lambda x: x[1], default=None)

    # 近 7 天 vs 之前 7 天
    today = date.today()
    recent = [e for e in entries
              if (today - datetime.strptime(e["date"], "%Y-%m-%d").date()).days <= 7]
    prev = [e for e in entries
            if 7 < (today - datetime.strptime(e["date"], "%Y-%m-%d").date()).days <= 14]

    # 被忽视的模块
    untouched = [m for m in MODULES.values() if m not in mod_count]

    # 标签
    tags = {}
    for e in entries:
        for t in e.get("tags", []):
            tags[t] = tags.get(t, 0) + 1
    top_tags = sorted(tags.items(), key=lambda x: -x[1])[:3]

    print(f"**坚持**：共 {total} 次练习、{len(dates)} 天，"
          f"{'当前连续 ' + str(streak) + ' 天' if streak > 0 else '最近一次 ' + dates[-1]}。")

    if len(mod_count) == 1:
        only = next(iter(mod_count))
        print(f"\n**你的模式**：目前只接触过「{only}」一个模块——"
              f"这是入口，不是全部。")
    else:
        print(f"\n**你的模式**：{dom_pct:.0f}% 的练习集中在「{dominant}」——"
              f"它似乎是你最常面对的课题。")

    if best and best[1] > 0:
        print(f"**最有效的练习**：「{best[0]}」——平均改善 {best[1]:+.1f} 分"
              f"（{best[2]} 次）。它的方法值得常用。")

    if top_tags:
        tag_str = "、".join(f"{t}（{n}次）" for t, n in top_tags)
        print(f"**高频标签**：{tag_str}。这些词是你生活的常客。")

    if untouched:
        print(f"**尚未探索**：{('、'.join(untouched))}。好奇的话，可以挑一个试试。")

    if recent or prev:
        trend = ""
        if len(recent) > len(prev) and prev:
            trend = f"近 7 天 {len(recent)} 次，比之前 7 天（{len(prev)} 次）更勤了。"
        elif prev and len(recent) < len(prev):
            trend = f"近 7 天 {len(recent)} 次，比之前 7 天（{len(prev)} 次）松了一些——没关系，回来就好。"
        elif recent:
            trend = f"近 7 天 {len(recent)} 次。"
        if trend:
            print(f"**节奏**：{trend}")

    # 困境地图（看清了什么）
    if reflections:
        n_un = sum(1 for r in reflections if r.get("uncontrollable"))
        n_c = sum(1 for r in reflections if r.get("controllable"))
        print(f"\n**困境地图**：你已经看清 {n_un} 件不可控的事，"
              f"找到了 {n_c} 个可控抓手。")
        if n_un > 0 and n_c == 0:
            print("  看清了很多，抓手还在路上——下次收尾时，为其中一件找个你能做的小动作。")

    # 引用用户原话
    insights = [e for e in entries if e.get("insight")]
    if insights:
        print("\n**你自己写下的**：")
        shown = set()
        for e in reversed(insights):
            if e["exercise_name"] in shown:
                continue
            shown.add(e["exercise_name"])
            print(f"  「{e['insight']}」——{e['date']}，{e['exercise_name']}")
            if len(shown) >= 3:
                break

    print("\n（报告基于本地记录自动生成。数字只是镜子，镜子里的人是你。）")
    return 0


def cmd_recommend(args):
    entries = load_practice_entries()
    mood = (args.mood or "").strip()

    print("🎯 今日练习推荐\n" + "─" * 36)

    # 无历史：入门组合
    if not entries:
        print("还没有练习记录——从入门组合开始：\n")
        print("· 练习 1  拆分担忧（控制二分法）——焦虑的通用入口，约 10 分钟")
        print("· 练习 2  \"命运许可\"保留条款（控制二分法）——最轻的热身，约 1 分钟")
        print("\n原则：不要一次尝试所有练习，选 1~2 个最贴合当前状态的开始。")
        return 0

    done_ids = {e["exercise_id"] for e in entries}
    recent_ids = [e["exercise_id"] for e in entries[-3:]]
    done_modules = {EXERCISES[eid][1] for eid in done_ids if eid in EXERCISES}
    recs = []  # [(eid, reason), ...]

    # 1) 情绪信号映射
    if mood:
        eids = MOOD_MAP.get(mood)
        if eids is None:  # 子串模糊匹配
            for k, v in MOOD_MAP.items():
                if k in mood or mood in k:
                    eids = v
                    break
        if mood in ("疲惫", "低电量") or eids == []:
            print("⚡ 低电量状态——今天不进深水区。\n")
            print("· 微练习（三分钟版）：原话显形 / 两栏速记 / 感官着陆 / 呼吸锚")
            print("· 或者，做一件你已验证过\"享受当下\"的事：给两小时，不带任务。")
            print("\n力竭的人做不了深蹲。维持接触，就是今天的全部功课。")
            return 0
        if eids:
            for eid in eids:
                if eid not in recent_ids and len(recs) < 2:
                    recs.append((eid, f"匹配你说的「{mood}」"))

    # 2) 覆盖度：未探索模块的入门代表练习
    rec_eids = [r[0] for r in recs]
    for mid, entry_eid in MODULE_ENTRY.items():
        if mid not in done_modules and entry_eid not in rec_eids:
            recs.append((entry_eid, f"「{MODULES[mid]}」模块你还没探索过"))
            rec_eids.append(entry_eid)
            break

    # 3) 有效性：历史改善数据最好的练习
    if len(recs) < 2:
        eff = {}
        for e in entries:
            if e.get("state_before") is None or e.get("state_after") is None:
                continue
            eff.setdefault(e["exercise_id"], []).append(
                e["state_before"] - e["state_after"])
        ranked = sorted(((sum(v) / len(v), eid, len(v)) for eid, v in eff.items()),
                       reverse=True)
        for avg, eid, n in ranked:
            if eid not in rec_eids and eid not in recent_ids:
                recs.append((eid, f"历史数据显示它对你最有效"
                                  f"（平均改善 {avg:+.1f} 分，{n} 次）"))
                rec_eids.append(eid)
                break

    # 4) 兜底：经典不重复
    if len(recs) < 2:
        for eid in (1, 20, 14, 26):
            if eid not in rec_eids and eid not in recent_ids:
                recs.append((eid, "经典练习，值得一试"))
                break

    for eid, reason in recs[:3]:
        name, mid = EXERCISES[eid]
        new_tag = "" if eid in done_ids else "  ⭐ 新练习"
        print(f"· 练习 {eid}  {name}（{MODULES[mid]}）——{reason}{new_tag}")

    # 电量提示：最近不适分偏高时
    states = [e["state_before"] for e in entries[-3:]
              if e.get("state_before") is not None]
    if states and sum(states) / len(states) >= 7:
        print(f"\n⚡ 注意：最近不适分平均 {sum(states) / len(states):.0f}（偏高）。"
              f"深水区练习前先查电量——力竭不做深蹲，")
        print("   低电量优先微练习或先休息。明天再来，也算练。")

    print("\n（推荐基于本地记录生成。最终选哪个，你说了算。）")
    return 0


def cmd_daily(_args):
    quotes = []
    if os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and line[0].isdigit() and '"' in line:
                    quotes.append(line[line.find('"'):])
    if not quotes:
        print("（语录库暂时不在身边。记住：你无法控制发生的事，但可以控制如何应对。）")
        return 0
    idx = date.today().toordinal() % len(quotes)
    print(f"📜 今日一句（{date.today().isoformat()}）：\n\n  {quotes[idx]}\n")
    print("（同一天再来，还是这句；明天换新。）")
    return 0


def cmd_morning(args):
    if not args.difficulty and not args.plan:
        print("❌ 至少要预想一个困难（--difficulty）或一个预案（--plan）")
        return 1
    entry = {
        "id": uuid.uuid4().hex[:8],
        "type": "morning",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "date": date.today().isoformat(),
        "state_note": args.state_note or "",
        "difficulty": args.difficulty or "",
        "plan": args.plan or "",
        "principle": args.principle or "",
        "tags": [t.strip() for t in (args.tags or "").split(",") if t.strip()],
    }
    save_entry(entry)
    print("🌅 晨间预演已存档。出门前，你已经见过今天最坏的天气。")
    if entry["state_note"]:
        print(f"   状态：{entry['state_note']}")
    if entry["difficulty"]:
        print(f"   预想困难：{entry['difficulty']}")
    if entry["plan"]:
        print(f"   预案：{entry['plan']}")
    if entry["principle"]:
        print(f"   今日准则：{entry['principle']}")
    return 0


def cmd_evening(args):
    if not args.progress and not args.let_go and not args.next:
        print("❌ 至少要回答一问（--progress / --let-go / --next）")
        return 1
    entry = {
        "id": uuid.uuid4().hex[:8],
        "type": "evening",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "date": date.today().isoformat(),
        "progress": args.progress or "",
        "let_go": args.let_go or "",
        "next": args.next or "",
        "tags": [t.strip() for t in (args.tags or "").split(",") if t.strip()],
    }
    save_entry(entry)
    print("🌙 晚间复盘已存档。今天到此为止，剩下的交给明天。")
    if entry["progress"]:
        print(f"   今天推进了：{entry['progress']}")
    if entry["let_go"]:
        print(f"   可以放下：{entry['let_go']}")
    if entry["next"]:
        print(f"   明天接续：{entry['next']}")
    return 0


def cmd_weekly(args):
    today = date.today()
    start = today - timedelta(days=args.days - 1)
    week = [e for e in load_entries()
            if 0 <= (today - datetime.strptime(e["date"], "%Y-%m-%d").date()).days < args.days]
    practices = [e for e in week if e.get("type", "practice") == "practice"]
    reflections = [e for e in week if e.get("type") == "reflection"]
    mornings = [e for e in week if e.get("type") == "morning"]
    evenings = [e for e in week if e.get("type") == "evening"]

    print(f"📅 周回顾（最近 {args.days} 天：{start} ~ {today}）\n" + "─" * 36)
    if not week:
        print("这段时间还没有任何记录。")
        print("可以从一句 `morning` 开始——不用想好所有事，先预想一件今天可能遇到的困难。")
        return 0

    # 1) 练习次数与模块分布
    if practices:
        mod_count = {}
        for e in practices:
            mod_count[e["module"]] = mod_count.get(e["module"], 0) + 1
        dist = "、".join(f"{m}×{n}" for m, n in
                         sorted(mod_count.items(), key=lambda x: -x[1]))
        print(f"**练习**：{len(practices)} 次（{dist}）")
    else:
        print("**练习**：0 次。练习不是这周的主旋律，晨/晚例程也算见面。")

    # 2) 状态分数变化（正数=不适改善）
    deltas = [(e["state_before"], e["state_after"]) for e in practices
              if e.get("state_before") is not None and e.get("state_after") is not None]
    if deltas:
        avg_b = sum(d[0] for d in deltas) / len(deltas)
        avg_a = sum(d[1] for d in deltas) / len(deltas)
        print(f"**状态**：练习前不适平均 {avg_b:.1f} → 练习后 {avg_a:.1f}"
              f"（平均改善 {avg_b - avg_a:+.1f} 分，{len(deltas)} 次有对比）")

    # 3) 困境地图新增
    if reflections:
        n_un = sum(1 for r in reflections if r.get("uncontrollable"))
        n_c = sum(1 for r in reflections if r.get("controllable"))
        print(f"**看清**：新增 {len(reflections)} 次——{n_un} 件不可控、{n_c} 个可控抓手。")
    else:
        print("**看清**：0 次。下周挑一次练习，收尾时落一笔 reflect。")

    # 4) 高频标签
    tags = {}
    for e in practices + mornings + evenings:
        for t in e.get("tags", []):
            tags[t] = tags.get(t, 0) + 1
    if tags:
        top = sorted(tags.items(), key=lambda x: -x[1])[:3]
        print(f"**高频标签**：{'、'.join(f'{t}（{n}）' for t, n in top)}。")

    # 5) 本周最有效练习
    eff = {}
    for e in practices:
        if e.get("state_before") is None or e.get("state_after") is None:
            continue
        eff.setdefault(e["exercise_name"], []).append(e["state_before"] - e["state_after"])
    if eff:
        best = max(((n, sum(v) / len(v), len(v)) for n, v in eff.items()),
                   key=lambda x: x[1])
        if best[1] > 0:
            print(f"**最有效**：「{best[0]}」平均改善 {best[1]:+.1f} 分"
                  f"（{best[2]} 次）——值得常用。")

    # 6) 下周一个重点建议
    tips = []
    if len(practices) < 3 and not mornings and not evenings:
        tips.append("下周先跑晨/晚例程——每天一句 morning，也算见面")
    if not reflections and practices:
        tips.append("挑一次练习收尾时落一笔 reflect——看清和练习同样重要")
    if mornings and not evenings:
        tips.append("晨间预演有了，补一次晚间复盘，让一天有收束")
    if not tips:
        tips.append("节奏稳住了。状态平稳的话，挑战一个没探索过的模块")
    print(f"**下周一个重点**：{tips[0]}。")

    print("\n（周回顾只读不写。数字是镜子，下周的决定在你。）")
    return 0


def cmd_export(args):
    entries = load_practice_entries()
    reflections = load_reflections()
    mornings = load_by_type("morning")
    evenings = load_by_type("evening")
    if not entries and not reflections and not mornings and not evenings:
        print("📂 没有可导出的记录。")
        return 0
    fmt = args.format
    out = args.output or f"stoic-export-{date.today().isoformat()}.{fmt}"

    if fmt == "json":
        with open(out, "w", encoding="utf-8") as f:
            json.dump(load_entries(), f, ensure_ascii=False, indent=2)
    else:  # md
        lines = ["# 我的斯多葛练习档案", "",
                 f"导出时间：{datetime.now().isoformat(timespec='seconds')}",
                 f"共 {len(entries)} 条练习、{len(reflections)} 条看清、"
                 f"{len(mornings)} 次晨间预演、{len(evenings)} 次晚间复盘", ""]
        # 困境地图章节：先看地图，再看流水
        if reflections:
            uns = [r for r in reflections if r.get("uncontrollable")]
            cs = [r for r in reflections if r.get("controllable")]
            lines += ["## 困境地图", "",
                      f"看清不可控 {len(uns)} 件，找到可控抓手 {len(cs)} 个。", "",
                      "### 不可控的事（看清即放下）", ""]
            for r in reversed(uns):
                ctx = f"（{r['context']}）" if r.get("context") else ""
                lines.append(f"- {r['uncontrollable']}——{r['date']}{ctx}")
            lines += ["", "### 可控的动作（大小不重要，重要的是做）", ""]
            for r in reversed(cs):
                ctx = f"（{r['context']}）" if r.get("context") else ""
                lines.append(f"- {r['controllable']}——{r['date']}{ctx}")
            lines.append("")
        lines += ["## 练习记录", ""]
        for e in reversed(entries):
            lines.append(f"### {e['date']} · {e['exercise_name']}（{e['module']}）")
            if e.get("state_before") is not None:
                lines.append(f"- 状态：{e['state_before']} → {e['state_after']}")
            if e.get("duration_min"):
                lines.append(f"- 时长：{e['duration_min']} 分钟")
            if e.get("tags"):
                lines.append(f"- 标签：{'、'.join(e['tags'])}")
            if e.get("insight"):
                lines.append(f"- 心得：{e['insight']}")
            lines.append("")
        if mornings or evenings:
            flows = sorted(mornings + evenings,
                           key=lambda x: (x["date"], x.get("timestamp", "")))
            lines += ["## 日常例程", ""]
            for e in reversed(flows):
                if e["type"] == "morning":
                    lines.append(f"### {e['date']} · 晨间预演")
                    if e.get("state_note"):
                        lines.append(f"- 状态：{e['state_note']}")
                    if e.get("difficulty"):
                        lines.append(f"- 预想困难：{e['difficulty']}")
                    if e.get("plan"):
                        lines.append(f"- 预案：{e['plan']}")
                    if e.get("principle"):
                        lines.append(f"- 今日准则：{e['principle']}")
                else:
                    lines.append(f"### {e['date']} · 晚间复盘")
                    if e.get("progress"):
                        lines.append(f"- 今天推进了：{e['progress']}")
                    if e.get("let_go"):
                        lines.append(f"- 可以放下：{e['let_go']}")
                    if e.get("next"):
                        lines.append(f"- 明天接续：{e['next']}")
                if e.get("tags"):
                    lines.append(f"- 标签：{'、'.join(e['tags'])}")
                lines.append("")
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    print(f"✅ 已导出：{len(entries)} 条练习 + {len(reflections)} 条看清"
          f" + {len(mornings) + len(evenings)} 条例程 → {out}")
    return 0


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(prog="stoic", description="斯多葛教练数据引擎")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("log", help="记录一次练习")
    p.add_argument("--exercise-id", type=int, required=True, help="练习编号 1-26")
    p.add_argument("--state-before", type=int, default=None, help="练习前状态 0-10")
    p.add_argument("--state-after", type=int, default=None, help="练习后状态 0-10")
    p.add_argument("--insight", default="", help="一句话收获")
    p.add_argument("--tags", default="", help="标签，逗号分隔")
    p.add_argument("--duration", type=int, default=None, help="时长（分钟）")
    p.set_defaults(func=cmd_log)

    p = sub.add_parser("reflect", help="记录一次看清（不可控/可控）")
    p.add_argument("--uncontrollable", default=None, help="看清的一件不可控的事")
    p.add_argument("--controllable", default=None, help="找到的一个可控动作")
    p.add_argument("--context", default=None, help="场景标签，如：绩效、家庭、健康")
    p.add_argument("--exercise", type=int, default=None, help="来源练习编号（可选）")
    p.set_defaults(func=cmd_reflect)

    p = sub.add_parser("map", help="查看困境地图（看清的不可控/可控）")
    p.set_defaults(func=cmd_map)

    p = sub.add_parser("history", help="查看历史记录")
    p.add_argument("--limit", type=int, default=10)
    p.set_defaults(func=cmd_history)

    p = sub.add_parser("stats", help="统计总览")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("insight", help="生成自我洞察报告")
    p.set_defaults(func=cmd_insight)

    p = sub.add_parser("recommend", help="推荐下一个练习（基于历史记录+情绪信号）")
    p.add_argument("--mood", default=None,
                   help="当前情绪信号：焦虑/愤怒/低落/抗拒/放不下/反刍/疲惫…")
    p.set_defaults(func=cmd_recommend)

    p = sub.add_parser("daily", help="每日一句斯多葛语录")
    p.set_defaults(func=cmd_daily)

    p = sub.add_parser("morning", help="晨间预演：预想今日困难与预案（3 分钟轻例程）")
    p.add_argument("--state-note", default="", help="一句话状态")
    p.add_argument("--difficulty", default=None, help="今天可能遇到的困难")
    p.add_argument("--plan", default=None, help="对应的预案")
    p.add_argument("--principle", default="", help="今日守住的一句准则")
    p.add_argument("--tags", default="", help="标签，逗号分隔")
    p.set_defaults(func=cmd_morning)

    p = sub.add_parser("evening", help="晚间复盘：三问收尾（3 分钟轻例程）")
    p.add_argument("--progress", default=None, help="今天推进了什么")
    p.add_argument("--let-go", default=None, help="可以放下什么")
    p.add_argument("--next", default=None, help="明天接什么")
    p.add_argument("--tags", default="", help="标签，逗号分隔")
    p.set_defaults(func=cmd_evening)

    p = sub.add_parser("weekly", help="周回顾：本周练习/看清/例程聚合（只读）")
    p.add_argument("--days", type=int, default=7, help="回顾窗口天数（默认 7）")
    p.set_defaults(func=cmd_weekly)

    p = sub.add_parser("export", help="导出记录")
    p.add_argument("--format", choices=["md", "json"], default="md")
    p.add_argument("--output", default=None)
    p.set_defaults(func=cmd_export)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 0
    return args.func(args) or 0


if __name__ == "__main__":
    sys.exit(main())
