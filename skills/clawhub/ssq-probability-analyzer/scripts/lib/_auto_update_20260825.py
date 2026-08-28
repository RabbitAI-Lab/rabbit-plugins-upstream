# -*- coding: utf-8 -*-
"""2026-08-25 自动化: 补录 2026097 开奖 + 写入 2026098 专家推荐"""
import json, io, os

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------- 1. 补录 2026097 开奖 (官方 cwl.gov.cn 664922 / 中彩网 / 广西福彩 三方一致) ----------
HP = os.path.join(BASE, 'ssq_history.json')
hist = json.load(open(HP, 'r', encoding='utf-8'))
periods = {r['period'] for r in hist}
NEW_DRAW = {
    "period": "2026097",
    "date": "2026-08-23",
    "front": [5, 16, 24, 26, 29, 30],
    "back": [2],
    "open_time": "2026-08-23 21:15:00",
}
if NEW_DRAW['period'] not in periods:
    hist.append(NEW_DRAW)
    hist.sort(key=lambda r: r['period'])
    json.dump(hist, open(HP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"[HISTORY] 已补录 {NEW_DRAW['period']}, 总期数={len(hist)}")
else:
    print(f"[HISTORY] {NEW_DRAW['period']} 已存在, 跳过")
print(f"[HISTORY] 最后一期: {hist[-1]['period']} {hist[-1]['date']} "
      f"红{hist[-1]['front']} 蓝{hist[-1]['back']}")

# ---------- 2. 2026098 专家推荐 (WebSearch 实时检索) ----------
SINA = "sports.sina.com.cn 2026-08-24 双色球名家第26098期推荐汇总"
YDNIU = "ydniu.com(一定牛) 2026-08-24/25 098期专家原创"
NOTE_E = "未核实观点, 无预测力(no_edge)"


def sina9(name, front, back):
    return {
        "expert": name,
        "platform": "新浪体育(sports.sina.com.cn)",
        "type": "媒体名家",
        "front": front,
        "back": back,
        "kind": "复式9+3(红9:%s; 蓝3:%s)" % (
            " ".join("%02d" % x for x in front), " ".join("%02d" % x for x in back)),
        "source": SINA,
        "note": NOTE_E,
    }


experts = [
    sina9("老牛",   [1, 4, 5, 8, 24, 26, 29, 30, 33],   [7, 11, 13]),
    sina9("马德文", [7, 11, 13, 14, 16, 19, 20, 30, 32], [2, 3, 9]),
    sina9("艾卫群", [4, 13, 14, 17, 19, 21, 26, 27, 32], [1, 12, 14]),
    sina9("王志升", [3, 12, 15, 17, 19, 22, 23, 24, 26], [6, 11, 14]),
    sina9("爱狄娜", [4, 6, 9, 12, 17, 22, 25, 29, 30],  [5, 8, 9]),
    sina9("万秋天", [3, 4, 6, 12, 14, 17, 18, 29, 30],  [1, 7, 14]),
    sina9("董翔骐", [2, 3, 14, 15, 17, 23, 26, 31, 33], [5, 12, 13]),
    sina9("靳红生", [2, 14, 18, 19, 21, 25, 26, 27, 31], [3, 6, 7]),
    sina9("郑容杰", [1, 3, 6, 7, 16, 22, 26, 31, 33],   [2, 8, 9]),
    sina9("孟少奇", [1, 3, 8, 9, 14, 20, 24, 30, 31],   [2, 3, 12]),
    sina9("薛高林", [9, 11, 15, 16, 17, 22, 26, 27, 33], [10, 12, 14]),
    sina9("白琪峰", [2, 6, 8, 10, 11, 13, 15, 19, 24],  [7, 9, 16]),
    {
        "expert": "年轻人",
        "platform": "一定牛(ydniu.com)",
        "type": "站内专家",
        "front": [4, 6, 7, 10, 12, 17, 21, 26, 30, 33],
        "back": [2, 10, 15],
        "kind": "复式红10+蓝3(单挑一注 06 07 12 21 26 33 + 02)",
        "source": YDNIU + " [年轻人]奇偶走势分析",
        "note": NOTE_E,
    },
    {
        "expert": "小老虎",
        "platform": "一定牛(ydniu.com)",
        "type": "站内专家",
        "front": [1, 4, 16, 19, 23, 25, 27, 28],
        "back": [4, 5, 12],
        "kind": "精选红8+围蓝3(单挑一注 01 04 19 23 27 28 + 05)",
        "source": YDNIU + " [小老虎]龙头点评分析",
        "note": NOTE_E,
    },
]

payload = {
    "_meta": {
        "target_period": "2026098",
        "last_updated": "2026-08-25 10:05",
        "auto_scraped": True,
        "source": "WebSearch实时检索(新浪体育sports.sina.com.cn 第26098期名家推荐汇总 / "
                  "新浪彩票lotto.sina.cn 098期孟少奇·董翔骐原创 / "
                  "一定牛ydniu.com 098期年轻人·小老虎原创, 检索于2026-08-25)",
        "note": "诚信说明: 专家推荐号由WebSearch实时检索公开来源, 未经核实, 质量参差。"
                "双色球近似完全随机, 任一6+1组合中奖概率恒为1/17,721,088, "
                "专家推荐无预测力(no_edge), 仅作描述性/逆向信号, "
                "绝不可据其认为某号更可能中奖。",
        "last_draw_ref": "上期2026097开奖: 红05 16 24 26 29 30 + 蓝02 (专家分析基线)",
        "consensus_hint": "新浪名家汇总统计: 红球龙头热点03/04, 凤尾热点30/33, "
                          "蓝球热点07/09, 名家最热一注03 14 17 26 30 33+07 "
                          "(仅为专家群体注意力分布, 非中奖概率)",
    },
    "experts": experts,
}

EP = os.path.join(BASE, 'ssq_expert_picks.json')
json.dump(payload, open(EP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"[EXPERTS] 已写入 {EP}")
print(f"[EXPERTS] target_period=2026098, 专家数={len(experts)}")

# 校验号码范围
bad = []
for e in experts:
    if not all(1 <= x <= 33 for x in e['front']):
        bad.append((e['expert'], 'front'))
    if not all(1 <= x <= 16 for x in e['back']):
        bad.append((e['expert'], 'back'))
    if len(set(e['front'])) != len(e['front']):
        bad.append((e['expert'], 'front-dup'))
print("[VALIDATE] 号码范围/去重校验:", "全部通过" if not bad else f"异常 {bad}")
