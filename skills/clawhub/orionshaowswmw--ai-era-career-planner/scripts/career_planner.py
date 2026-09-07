#!/usr/bin/env python3
"""career_planner.py — AI时代职业规划引擎 v2.0.0

确定性、离线、纯标准库。所有输出为 JSON（ensure_ascii=False），stdout 输出结果，
stderr 输出错误 JSON，exit code: 0=成功, 2=输入错误。

命令：
  holland  --answers '{"q1":"安静","q2":"事实","q3":"规则"}'
           8 种组合全量确定性映射（完整表见 references/assessment.md）。
  match    --answers '{"holland":"R","values":["成长性","自主性"],"anchor":"自主/独立型"}'
             [--city 北京] [--industry 互联网/IT] [--top 5]
           12 方向启发式匹配。fit = round(5×(0.4·holland+0.3·values+0.3·anchor))，
           缺失维度自动按可用维度重新归一化并标记 not_assessed。
           排序：fit 降序 → 薪资中值降序 → 名称升序（确定性）。
  salary   --city 北京 --industry 互联网/IT --occupation 后端开发工程师 --level entry
           | --list cities|industries|occupations|levels
  report   --data-file results.json [--out 报告.md]

诚实性硬规则（所有输出携带）：
  - assessment_type = "screening"：筛查/对话框架，不是认证测评
    （MBTI 重测一致性约 50-65%；霍兰德量表信度约 .91-.95）
  - fit 指数 = 启发式打分，非预测
  - 薪资 = 因子模型参考区间，非实时市场数据
"""
import argparse
import json
import os
import sys

_SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(_SKILL_ROOT, "data", "salary_database.json")

VALIDITY_NOTE = ("本结果为筛查性参考（screening），不是职业认证测评："
                 "MBTI 重测一致性约 50-65%，霍兰德量表信度约 .91-.95。"
                 "结果适合做对话素材与方向筛选，不能用于重大决策的唯一依据。")
FIT_NOTE = ("启发式打分（非预测）：fit = round(5×(0.4·holland + 0.3·values + 0.3·anchor))，"
            "子分：holland 命中=1.0/未命中=0.2；values 按交集/2；anchor 主锚=1.0/次锚=0.5/其他=0.0；"
            "缺失维度按可用维度重新归一化权重。")
SALARY_NOTE = "薪资为因子模型参考区间（人民币/月），非实时市场数据，以招聘平台实时数据为准。"

# ── 霍兰德 3 问 ────────────────────────────────────────────────────────────
Q_OPTIONS = {
    "q1": {"安静": "solo", "solo": "solo", "alone": "solo", "一个人": "solo",
           "一起": "together", "together": "together", "和很多人": "together"},
    "q2": {"事实": "facts", "facts": "facts", "数据": "facts", "具体的": "facts",
           "概念": "concepts", "concepts": "concepts", "抽象的": "concepts", "创意": "concepts"},
    "q3": {"规则": "rules", "rules": "rules", "流程": "rules",
           "自由": "freedom", "freedom": "freedom", "变化": "freedom"},
}
Q_LABELS = {
    "q1": ("一个人安静做事", "和很多人一起"),
    "q2": ("具体的事实和数据", "抽象的概念和创意"),
    "q3": ("规则和流程", "自由和变化"),
}

# 完整 8 组合确定性映射表（v1 只列了 5 条且含无效选项"说服"，v2 补全）
HOLLAND_TABLE = {
    ("solo", "facts", "rules"):       ("R", "现实型", "动手、操作、机械", "工程师、机械师、技师", ""),
    ("solo", "facts", "freedom"):     ("R", "现实型", "动手、操作、机械", "工程师、独立开发者、技术顾问",
                                       "偏好自由的现实型：可关注弹性工作形态（独立开发、外包、技术顾问）"),
    ("solo", "concepts", "rules"):    ("I", "研究型", "研究、探索、分析", "科学家、分析师、研究员",
                                       "偏好规则的研究型：可关注结构化研究岗位（研究支持、合规分析、实验管理）"),
    ("solo", "concepts", "freedom"):  ("I/A", "研究型/艺术型（混合）", "研究+创意", "研究者、技术写作者、独立创作",
                                       "混合型：研究型与艺术型并重，适合研究与创作交叉的方向"),
    ("together", "facts", "rules"):   ("C", "常规型", "规整、组织、执行", "会计、行政、审计、运营", ""),
    ("together", "facts", "freedom"): ("E", "企业型", "领导、说服、管理", "销售、商务、创业者",
                                       "事实+自由组合常见于弹性商务岗位（销售、BD、市场开拓）"),
    ("together", "concepts", "rules"): ("S", "社会型", "助人、沟通、教育", "教师、培训、心理咨询",
                                       "概念+规则组合常见于结构化助人岗位（教学、培训、课程运营）"),
    ("together", "concepts", "freedom"): ("S", "社会型", "助人、沟通、教育", "教师、心理咨询师、社区工作者", ""),
}

VALUES = ["成就感", "人际关系", "自主性", "稳定性", "成长性"]
ANCHORS = ["技术/职能型", "管理型", "自主/独立型", "安全/稳定型",
           "创业型", "服务/奉献型", "纯粹挑战型", "生活方式型"]
VALID_CODES = {"R", "I", "A", "S", "E", "C", "I/A"}

# ── 12 方向表（ai_rating 均标注来源与日期；无量化数据的标"定性"）─────────────
DIRECTIONS = [
    {"name": "AI/算法", "holland": "I", "values": ["成长性", "成就感"],
     "anchors": ["技术/职能型", "纯粹挑战型"], "db_occupation": "算法工程师",
     "ai_rating": "强需求：AI Agent相关技术人才需求同比+244%、AI工程师+19.3%、供需比2.62（智联招聘《2026年人工智能产业人才发展报告》2026-07-21）；算法岗发布量2025-02同比+46.8%（新华社 2025-03-26）",
     "path": "机器学习基础 → 大模型/深度学习工程 → LeetCode+GitHub 项目作品集",
     "risk": "学历/项目门槛高；只做模型调用的执行型岗位最先被AI工具挤压"},
    {"name": "AI产品", "holland": "E", "values": ["成就感", "成长性"],
     "anchors": ["管理型", "创业型"], "db_occupation": "产品经理",
     "ai_rating": "强需求：AI产品经理岗位发布量+87.7%（智联招聘 2026-07-21）；节后AI PM需求约+129%、供需约5.1:1（智联数据/新浪财经 2026-03-31）",
     "path": "产品助理/实习 → 完整产品案例 → AI产品专项（Agent工作流、提示词工程）",
     "risk": "供给快速膨胀、初级PM竞争激烈；无AI实操经验者将被淘汰"},
    {"name": "数据分析", "holland": "C", "values": ["成就感", "稳定性"],
     "anchors": ["技术/职能型", "安全/稳定型"], "db_occupation": "数据分析师",
     "ai_rating": "稳中有变：数据标注/AI训练师岗位+30.3%（智联招聘 2026-07-21）；一线城市约72%企业已要求AI工具技能（新浪财经 2026-03-31）",
     "path": "SQL/Python+统计学 → BI工具(Tableau/PowerBI) → 行业数据项目",
     "risk": "基础取数/报表岗正被AI自动化替代，需向决策分析上移"},
    {"name": "后端开发", "holland": "R", "values": ["成就感", "自主性"],
     "anchors": ["技术/职能型", "自主/独立型"], "db_occupation": "后端开发工程师",
     "ai_rating": "结构性分化：AI应届生岗位+28.4%（智联2026-01~05，经苏州人社局 2026-07-03）；入门级岗位需求自2022-10持续下降（新浪财经 2026-03-31）",
     "path": "系统+数据库+一门语言 → 个人/开源项目 → 实习或社招",
     "risk": "入门岗位竞争加剧，无项目背书者难入行；CRUD型岗位收缩（定性）"},
    {"name": "金融分析", "holland": "C", "values": ["稳定性", "成就感"],
     "anchors": ["安全/稳定型", "技术/职能型"], "db_occupation": "金融分析师",
     "ai_rating": "定性：金融业AI工具采用率高，效率型分析工作受挤压，合规/风控方向相对稳定（行业观察，无量化数据）",
     "path": "财会/金融基础 → 基金从业/CFA等证书 → 行内轮岗积累",
     "risk": "初级建模与报告岗自动化程度高"},
    {"name": "医疗健康", "holland": "I", "values": ["成就感", "稳定性"],
     "anchors": ["服务/奉献型", "安全/稳定型"], "db_occupation": "医生",
     "ai_rating": "定性：AI辅助诊断与文书是增强而非替代，岗位稳定（行业观察，无量化数据）",
     "path": "医学教育+规培（学历门槛高）→ 专科方向",
     "risk": "AI处理病历文书，早期需建立独立临床判断力"},
    {"name": "教育培训", "holland": "S", "values": ["人际关系", "稳定性"],
     "anchors": ["服务/奉献型", "安全/稳定型"], "db_occupation": "教师",
     "ai_rating": "分化：教育培训类需求收缩（新浪财经 2026-03-31）；但AI讲师岗+112.4%、月薪约¥15,792（新华社 2025-03-26）",
     "path": "教师资格证 → 学科教学 或 AI应用教学方向",
     "risk": "传统学科培训需求下降，需转向AI素养/职业教育"},
    {"name": "营销/跨境", "holland": "E", "values": ["成就感", "自主性"],
     "anchors": ["创业型", "纯粹挑战型"], "db_occupation": "市场营销",
     "ai_rating": "承压：销售/商务类需求自2023-Q3下降（新浪财经 2026-03-31）；AI内容工具降低文案门槛（定性）",
     "path": "内容/投放实操 → 跨境平台经验 → AI营销工具链",
     "risk": "执行型文案/投放岗位被AI内容工具大幅挤压"},
    {"name": "UI/UX", "holland": "A", "values": ["自主性", "成就感"],
     "anchors": ["自主/独立型", "生活方式型"], "db_occupation": "UI/UX设计师",
     "ai_rating": "定性：AI生图工具压缩执行类UI需求，体验/交互设计价值上升（行业观察，无量化数据）",
     "path": "Figma+作品集 → 交互/体验专项 → AI产品界面垂直方向",
     "risk": "纯视觉执行岗需求下降"},
    {"name": "保险经纪", "holland": "S", "values": ["自主性", "成就感"],
     "anchors": ["自主/独立型", "创业型"], "db_occupation": "保险经纪人",
     "ai_rating": "定性：合规销售+长期服务，AI用于计划书生成与客户跟进（行业观察；28家机构名录见 data/insurance_broker_companies.json）",
     "path": "保险从业资格 → 机构培训 → 客户积累",
     "risk": "获客成本高；纯推销型模式难以为继"},
    {"name": "机械/新能源", "holland": "R", "values": ["稳定性", "成就感"],
     "anchors": ["技术/职能型", "安全/稳定型"], "db_occupation": "机械工程师",
     "ai_rating": "上升：新能源行业AI工程师岗位+38.2%、月薪约¥22,594（智联招聘 2026-07-21）；21%的AI应届需求来自高端装备/智能制造（苏州人社局 2026-07-03）",
     "path": "机械/自动化基础 → 新能源/智能制造方向 → 项目或认证",
     "risk": "传统机械岗增长慢，需绑定新能源/智能化"},
    {"name": "体制内", "holland": "C", "values": ["稳定性", "人际关系"],
     "anchors": ["安全/稳定型", "服务/奉献型"], "db_occupation": None,
     "salary_note": "体制内薪资因地区/职级差异大，因子模型无覆盖",
     "ai_rating": "定性：AI对体制内岗位冲击最小，但编制竞争加剧（行业观察，无量化数据）",
     "path": "省考/国考/事业编 → 笔试+面试长期准备",
     "risk": "竞争比高、周期长；薪资上限明确"},
]


def err(msg, extra=None, **kw):
    out = {"status": "error", "error": msg}
    if extra:
        out.update(extra)
    if kw:
        out.update(kw)
    print(json.dumps(out, ensure_ascii=False, indent=2), file=sys.stderr)
    sys.exit(2)


def load_json_arg(raw, what):
    try:
        v = json.loads(raw)
    except json.JSONDecodeError as e:
        err(f"{what} 不是合法 JSON: {e}")
    if not isinstance(v, dict):
        err(f"{what} 必须是 JSON 对象")
    return v


def norm_holland_answer(key, val):
    if val is None:
        return None
    if not isinstance(val, str):
        err(f"holland 答案 {key} 必须是字符串",
            valid_options=sorted(set(Q_OPTIONS[key]) | {"(留空)"})[:10])
    v = Q_OPTIONS[key].get(val.strip())
    if v is None:
        err(f"holland 答案 {key} 无效: {val!r}",
            valid_options=sorted(set(Q_OPTIONS[key]) | {"(留空)"}))
    return v


def compute_holland(answers):
    got = {}
    for key in ("q1", "q2", "q3"):
        v = norm_holland_answer(key, answers.get(key))
        if v is not None:
            got[key] = v
    missing = [k for k in ("q1", "q2", "q3") if k not in got]
    return got, missing


def cmd_holland(args):
    answers = load_json_arg(args.answers, "--answers")
    unknown = set(answers) - {"q1", "q2", "q3"}
    if unknown:
        err(f"未知字段: {sorted(unknown)}", valid_options=["q1", "q2", "q3"])
    got, missing = compute_holland(answers)
    if missing:
        err("缺少答案: " + ", ".join(missing) + "（三问都必须回答才能给出代码）",
            questions={k: list(Q_LABELS[k]) for k in missing})
    code, label, keywords, typical, note = HOLLAND_TABLE[(got["q1"], got["q2"], got["q3"])]
    result = {
        "command": "holland", "status": "ok",
        "code": code, "label": label, "keywords": keywords, "typical_jobs": typical,
        "answers": got,
        "assessment_type": "screening",
        "note": note or "无附加说明",
        "validity_note": VALIDITY_NOTE,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0)


def load_db():
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        err(f"无法读取薪资数据库 {DB_FILE}: {e}")


def lookup_salary(db, city, industry, occupation):
    for r in db["records"]:
        if r["city"] == city and r["industry"] == industry and r["occupation"] == occupation:
            return r
    return None


def dir_salary(db, d, city, industry, level):
    occ = d.get("db_occupation")
    if occ is None:
        return None, d.get("salary_note", "该方向无因子模型覆盖")
    if not city:
        return None, "未提供 --city，无法给出参考区间"
    if not industry:
        return None, "未提供 --industry，无法给出参考区间"
    rec = None
    for r in db["records"]:
        if (r["city"] == city and r["industry"] == industry
                and r["occupation"] == occ and r["level"] == level):
            rec = r
            break
    if rec is None:
        return None, f"{city}/{industry}/{occ}/{level} 不在因子模型覆盖内"
    return f"{rec['salary_min']}-{rec['salary_max']} 元/月（{level}）", SALARY_NOTE


def parse_match_answers(answers):
    unknown = set(answers) - {"holland", "holland_answers", "values", "anchor"}
    if unknown:
        err(f"未知字段: {sorted(unknown)}",
            valid_options=["holland", "holland_answers", "values", "anchor"])
    holland = None
    if "holland_answers" in answers:
        ha = answers["holland_answers"]
        if not isinstance(ha, dict):
            err("holland_answers 必须是对象")
        got, missing = compute_holland(ha)
        if missing:
            err("holland_answers 缺少: " + ", ".join(missing))
        holland = HOLLAND_TABLE[(got["q1"], got["q2"], got["q3"])][0]
    if "holland" in answers and answers["holland"] is not None:
        h = answers["holland"]
        if not isinstance(h, str) or h.strip() not in VALID_CODES:
            err(f"holland 代码无效: {h!r}", valid_options=sorted(VALID_CODES))
        holland = h.strip()
    values = None
    if answers.get("values") is not None:
        v = answers["values"]
        if not isinstance(v, list) or len(v) != 2:
            err("values 必须是恰好 2 项的列表（从 5 项价值观中选出最看重的 2 项）",
                valid_options=VALUES)
        norm = []
        for x in v:
            if x not in VALUES:
                err(f"values 无效项: {x!r}", valid_options=VALUES)
            norm.append(x)
        if len(set(norm)) != 2:
            err("values 两项必须不同")
        values = norm
    anchor = None
    if answers.get("anchor") is not None:
        a = answers["anchor"]
        if not isinstance(a, str) or a not in ANCHORS:
            err(f"anchor 无效: {a!r}", valid_options=ANCHORS)
        anchor = a
    if holland is None and values is None and anchor is None:
        err("至少提供 holland / values / anchor 之一（或 holland_answers）")
    return holland, values, anchor


def score_direction(d, holland, values, anchor):
    sub = {}
    if holland is not None:
        user_codes = holland.split("/")
        sub["holland"] = 1.0 if d["holland"] in user_codes else 0.2
    if values is not None:
        sub["values"] = round(len(set(values) & set(d["values"])) / 2, 2)
    if anchor is not None:
        if anchor == d["anchors"][0]:
            sub["anchor"] = 1.0
        elif anchor == d["anchors"][1]:
            sub["anchor"] = 0.5
        else:
            sub["anchor"] = 0.0
    return sub


def cmd_match(args):
    answers = load_json_arg(args.answers, "--answers")
    holland, values, anchor = parse_match_answers(answers)
    db = load_db()
    if args.level not in db["levels"]:
        err(f"--level 无效: {args.level!r}", valid_options=db["levels"])
    base_w = {"holland": 0.4, "values": 0.3, "anchor": 0.3}
    present = [k for k, v in (("holland", holland), ("values", values), ("anchor", anchor)) if v is not None]
    wsum = sum(base_w[k] for k in present)
    weights = {k: base_w[k] / wsum for k in present}
    not_assessed = [k for k in ("holland", "values", "anchor") if k not in present]

    scored = []
    for d in DIRECTIONS:
        sub = score_direction(d, holland, values, anchor)
        fit = round(5 * sum(sub[k] * weights[k] for k in sub))
        salary, salary_note = dir_salary(db, d, args.city, args.industry, args.level)
        median = None
        if salary:
            lo_hi = salary.split(" 元/月")[0].split("-")
            if len(lo_hi) == 2 and lo_hi[0].strip().isdigit() and lo_hi[1].strip().isdigit():
                median = (int(lo_hi[0]) + int(lo_hi[1])) / 2
        scored.append({
            "name": d["name"], "fit_index": fit, "sub_scores": sub,
            "ai_rating": d["ai_rating"], "path": d["path"], "risk": d["risk"],
            "salary": salary, "salary_note": salary_note,
            "_median": median if median is not None else float("-inf"),
        })
    scored.sort(key=lambda s: (-s["fit_index"], -s["_median"], s["name"]))
    for s in scored:
        s.pop("_median", None)

    top_n = args.top if args.top and args.top > 0 else 5
    recs = [{
        "title": s["name"], "score": s["fit_index"],
        "reason": _reason(s),
        "ai_rating": s["ai_rating"], "salary": s["salary"] or "暂无参考区间",
        "salary_note": s["salary_note"], "path": s["path"], "risk": s["risk"],
    } for s in scored[:top_n]]
    result = {
        "command": "match", "status": "ok",
        "assessment_type": "screening",
        "validity_note": VALIDITY_NOTE,
        "scoring_note": FIT_NOTE,
        "inputs": {"holland": holland, "values": values, "anchor": anchor},
        "not_assessed": not_assessed,
        "weights_used": {k: round(v, 3) for k, v in weights.items()},
        "city": args.city, "industry": args.industry,
        "recommendations": recs,
        "full_ranking": [{"name": s["name"], "fit_index": s["fit_index"],
                          "sub_scores": s["sub_scores"], "salary": s["salary"]} for s in scored],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0)


def _reason(s):
    parts = []
    sub = s["sub_scores"]
    if sub.get("holland") == 1.0:
        parts.append("霍兰德命中")
    if sub.get("values") == 1.0:
        parts.append("价值观完全匹配")
    elif sub.get("values") == 0.5:
        parts.append("价值观部分匹配")
    if sub.get("anchor") == 1.0:
        parts.append("职业锚主锚命中")
    elif sub.get("anchor") == 0.5:
        parts.append("职业锚次锚命中")
    return "；".join(parts) if parts else "启发式弱匹配（可用维度未命中）"


def cmd_salary(args):
    db = load_db()
    if args.list:
        mapping = {
            "cities": sorted({r["city"] for r in db["records"]}),
            "industries": db["industries"],
            "occupations": sorted({r["occupation"] for r in db["records"]}),
            "levels": db["levels"],
        }
        if args.list not in mapping:
            err(f"--list 无效: {args.list!r}", valid_options=list(mapping))
        print(json.dumps({"command": "salary-list", "status": "ok",
                          args.list: mapping[args.list]}, ensure_ascii=False, indent=2))
        sys.exit(0)
    missing = [k for k, v in (("--city", args.city), ("--industry", args.industry),
                              ("--occupation", args.occupation), ("--level", args.level)) if not v]
    if missing:
        err("缺少参数: " + ", ".join(missing))
    city, ind, occ, lvl = args.city, args.industry, args.occupation, args.level
    ok_city = city in {r["city"] for r in db["records"]}
    ok_ind = ind in db["industries"]
    ok_occ = occ in {r["occupation"] for r in db["records"]}
    ok_lvl = lvl in db["levels"]
    invalid = {}
    if not ok_city:
        invalid["city"] = sorted({r["city"] for r in db["records"]})
    if not ok_ind:
        invalid["industry"] = db["industries"]
    if not ok_occ:
        invalid["occupation"] = sorted({r["occupation"] for r in db["records"]})
    if not ok_lvl:
        invalid["level"] = db["levels"]
    if invalid:
        bad = "; ".join(f"{flag}={val!r}" for flag, val, key in
                        (("--city", city, "city"), ("--industry", ind, "industry"),
                         ("--occupation", occ, "occupation"), ("--level", lvl, "level"))
                        if key in invalid)
        err("无效取值: " + bad, valid_options=invalid)
    rec = None
    for r in db["records"]:
        if r["city"] == city and r["industry"] == ind and r["occupation"] == occ and r["level"] == lvl:
            rec = r
            break
    if rec is None:
        err(f"该组合无记录: {city}/{ind}/{occ}/{lvl}（城市×行业组合在模型中部分覆盖，可用 --list 查看取值）")
    result = {
        "command": "salary", "status": "ok",
        "city": city, "industry": ind, "occupation": occ, "level": lvl,
        "level_label": db["level_labels"].get(lvl, lvl),
        "salary_min": rec["salary_min"], "salary_max": rec["salary_max"],
        "salary_unit": rec["salary_unit"],
        "provenance": "因子模型参考区间（非实时市场数据）",
        "note": SALARY_NOTE,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0)


def cmd_report(args):
    try:
        with open(args.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except OSError as e:
        err(f"无法读取 --data-file: {e}")
    except json.JSONDecodeError as e:
        err(f"--data-file 不是合法 JSON: {e}")
    if not isinstance(data, dict):
        err("--data-file 顶层必须是 JSON 对象")

    errors = []
    recs = data.get("recommendations")
    if not isinstance(recs, list) or not recs:
        errors.append("recommendations 必须是非空数组（可用 career_planner.py match 的输出填充）")
    else:
        for i, r in enumerate(recs):
            if not isinstance(r, dict) or not r.get("title"):
                errors.append(f"recommendations[{i}] 必须是含 title 的对象")
                break
    ai = data.get("ai_guide")
    if ai is not None and not isinstance(ai, dict):
        errors.append("ai_guide 必须是对象")
    acts = data.get("actions")
    if acts is not None and not isinstance(acts, dict):
        errors.append("actions 必须是对象")
    if errors:
        err("data-file 校验失败: " + " | ".join(errors))

    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    star = chr(9733)
    lines = [
        "# 个性化职业规划报告", "",
        f"> 生成日期：{today}　|　引擎：ai-era-career-planner v2.0.0", "",
        "## ⚠️ 重要声明（先读这里）", "",
        f"> 1. 测评性质：**{data.get('assessment_type', 'screening')}（筛查性参考）**，不是职业认证测评。"
        "MBTI 重测一致性约 50-65%，霍兰德量表信度约 .91-.95。",
        "> 2. 适合指数为**启发式打分，非预测**（权重：霍兰德0.4 / 价值观0.3 / 职业锚0.3，详见 references/assessment.md）。",
        "> 3. 薪资为**因子模型参考区间**（人民币/月），非实时市场数据，以招聘平台实时数据为准。",
        "> 4. 文中标注\"定性\"的判断为方向性观察，不是统计结论。",
        "", "---", "",
        "## 基础档案", "",
        f"- 昵称：{data.get('nickname', '未提供')}",
        f"- 当前阶段：{data.get('stage', '未提供')}",
        f"- 霍兰德代码：{data.get('holland', '未测评')}",
        f"- MBTI类型：{data.get('mbti', '未测评')}",
        f"- 职业锚：{data.get('anchor', '未测评')}",
        f"- 核心价值观：{'、'.join(data['values']) if isinstance(data.get('values'), list) else data.get('values', '未明确')}",
        f"- 城市：{data.get('city', '未提供')}",
        f"- 行业：{data.get('industry', '未提供')}",
        "", "---", "",
        "## 职业方向推荐", "",
    ]
    for i, r in enumerate(data["recommendations"], 1):
        sc = r.get("score", 3)
        sc = max(0, min(5, int(sc))) if isinstance(sc, (int, float)) else 3
        lines.append(f"### {i}. 【{r['title']}】 适合指数：{star * sc}{'☆' * (5 - sc)}")
        for k, label in (("reason", "推荐理由"), ("ai_rating", "AI评级"),
                         ("salary", "薪资参考"), ("salary_note", "薪资说明"),
                         ("path", "入门路径"), ("expectation", "3年预期"), ("risk", "潜在风险")):
            if r.get(k):
                lines.append(f"- **{label}**：{r[k]}")
        lines.append("")
    lines += ["## AI时代生存指南", ""]
    ai = data.get("ai_guide", {})
    lines.append(f"- 核心技能：{ai.get('skills', '详见推荐方向')}")
    lines.append(f"- 必学AI工具：{ai.get('tools', '暂无')}")
    lines.append(f"- 建议认证：{ai.get('cert', '暂无')}")
    lines += ["", "## 下一步行动清单", ""]
    acts = data.get("actions", {})
    lines.append(f"- 今天：{acts.get('today', '暂无')}")
    lines.append(f"- 1个月内：{acts.get('1month', '暂无')}")
    lines.append(f"- 3个月内：{acts.get('3months', '暂无')}")
    lines.append(f"- 1年内：{acts.get('1year', '暂无')}")
    lines += ["", "---", "", f"由 ai-era-career-planner v2.0.0 生成（{today}）"]
    md = "\n".join(lines)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(json.dumps({"command": "report", "status": "ok", "out": args.out,
                          "bytes": len(md.encode("utf-8"))}, ensure_ascii=False, indent=2))
    else:
        print(md)
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(prog="career_planner.py", description="AI时代职业规划引擎 v2.0.0（离线、确定性、JSON 输出）")
    sub = p.add_subparsers(dest="command", required=True)

    ph = sub.add_parser("holland", help="霍兰德 3 问 → 确定性代码")
    ph.add_argument("--answers", required=True, help='JSON: {"q1":...,"q2":...,"q3":...}')
    ph.set_defaults(fn=cmd_holland)

    pm = sub.add_parser("match", help="12 方向启发式匹配")
    pm.add_argument("--answers", required=True,
                    help='JSON: {"holland"|"holland_answers","values","anchor"}（至少一项）')
    pm.add_argument("--city", default=None)
    pm.add_argument("--industry", default=None)
    pm.add_argument("--level", default="entry", help="entry|mid|senior|expert（默认 entry）")
    pm.add_argument("--top", type=int, default=5)
    pm.set_defaults(fn=cmd_match)

    ps = sub.add_parser("salary", help="薪资参考区间查询")
    ps.add_argument("--city")
    ps.add_argument("--industry")
    ps.add_argument("--occupation")
    ps.add_argument("--level")
    ps.add_argument("--list", default=None, help="cities|industries|occupations|levels")
    ps.set_defaults(fn=cmd_salary)

    pr = sub.add_parser("report", help="生成 Markdown 报告")
    pr.add_argument("--data-file", required=True)
    pr.add_argument("--out", default=None, help="输出 .md 路径（缺省打印到 stdout）")
    pr.set_defaults(fn=cmd_report)

    args = p.parse_args()
    try:
        args.fn(args)
    except SystemExit:
        raise
    except Exception as e:  # 兜底：任何未预期异常也以 exit 2 + JSON 报告
        err(f"未预期错误: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
