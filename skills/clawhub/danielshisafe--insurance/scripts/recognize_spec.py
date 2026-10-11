#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""产品说明书识别器（保险计划书分析大师·扩展准备，v2）
---------------------------------------------------------------
输入：extract.py 产出的 JSON（pdf/docx/xlsx 均支持）
输出：结构化识别结果（产品属性 + 文档类别 + 是否含示例利益演示）

v2 修正（基于德华安顾两份真实说明书）：
  - 产品名：优先「产品名称」标签 / 「（产品代码」前文字 / 含数字括号的名词短语；过滤"该产品为分红型保险产品"等套话。
  - 险种：排除「非万能型/非投连」否定词；万能仅认"万能型/万能保险"而非"万能险项下"。
  - 投保年龄/保险期间/交费期间：支持「投保范围：0至75周岁」「出生满30天至80周岁」「交费期间：1/3/5/10年」多值。
  - 年金专属：养老年金开始领取年龄、保证领取期间、领取方式。
  - 条款段落：优先抓真实「（三）保险责任」「（五）责任免除」段（而非末尾投保提示套话），遇下一标题截断。
  - 利益演示：识别是否为「示例」（如"30岁安先生…年交保费1万"），标注非个性化。
用法：
  python recognize_spec.py <extract.json> [--out recognition.json]
"""
import json, re, argparse, unicodedata

import json, re, argparse, unicodedata

def dedup_cjk(text):
    """去中文文本层伪影 + 还原康熙部首。

    ★ NFKC：部分 PDF 的 ToUnicode 把汉字映射成康熙部首（U+2F00–U+2FDF，
      如 ⾦ U+2FA6 代 金、⽣ U+2F63 代 生），不还原会让「现金价值」「终身寿险」
      等所有关键词匹配失败，识别结果静默缺项。顺序：先 NFKC 再去重。
    """
    if not text: return text
    text = unicodedata.normalize("NFKC", text)
    out = []
    for ch in text:
        if out and ch == out[-1] and ('\u4e00' <= ch <= '\u9fff'):
            continue
        out.append(ch)
    return ''.join(out)

# ★ 文本上限：xlsx 精算表动辄 2000+ 行（现金价值表/费率表），全量拼进文本后
#   各识别正则要在百万字上反复回溯，实测 2.7MB 输入耗时 2 分 40 秒（用户会以为卡死）。
#   产品名/条款/类别信息都在文档前部，截断到 30 万字对识别结果无影响但快一个数量级。
MAX_TEXT = 300_000


def build_text(data):
    parts = []
    total = 0
    done = [False]

    def add(s):
        nonlocal total
        if done[0] or not s:
            return
        s = str(s)
        parts.append(s)
        total += len(s)
        if total >= MAX_TEXT:
            done[0] = True

    if data.get("kind") == "pdf":
        for p in data["data"]["pages"]:
            add(p.get("text"))
            for tb in p.get("tables", []):
                for row in tb:
                    add(" ".join(str(c) for c in row))
    elif data.get("kind") == "docx":
        for s in data["data"].get("paragraphs", []):
            add(s)
        for tb in data["data"].get("tables", []):
            for row in tb:
                add(" ".join(str(c) for c in row))
    elif data.get("kind") == "xlsx":
        for name, rows in data["data"].get("sheets", {}).items():
            add(name)
            for row in rows:
                add(" ".join(str(c) for c in row))
    else:
        add(str(data))
    return "\n".join(parts)

NOISE = ["被保险人","投保人","合同","标准体","公司","所列","建议","保障计划",
         "本条款","本保险","责任","期间","金额","说明","声明","提示","保险产品","该产品"]
# ★ 营销/描述性套话：兜底正则只要求「…+险种词」，若不限定结尾就会把
#   「过1414万名客户提供保险服务」这类广告语当成产品名（真实踩过的坑）。
BOILER = ["服务", "提供", "客户", "客户", "万名", "需求", "以下", "如下", "详见",
          "包括", "分为", "是指", "本公司", "欢迎", "咨询", "联系", "扫码", "关注",
          "以上", "说明", "注释", "备注", "假设", "测算", "案例", "示例"]
# ★ 表格词/泛指词：命中这些说明候选不是产品名，而是演示表的列名或行文片段。
#   宁可返回 None（未知）也不要编造一个像产品名的字符串 —— 编造比留白危险得多。
TABLEWORD = ["基本", "当年度", "累计", "身故", "全残", "具体", "请以", "造成", "表中",
             "数据", "实际", "承保", "依据", "享有", "形式", "下列", "上述", "其他",
             "相关", "部分", "各项", "年度末", "年末", "年初", "保单年度", "现金价值",
             "红利", "保额", "保险费", "退保", "本产品", "该产品"]

def get_product_name(t):
    # 优先级1：命名产品型「品牌 + 产品词 + 8号 + 险种 +（分红型）」
    # 允许文本层在「号」前后插入空格（PDF 常见伪影）
    m = re.search(
        r"([\u4e00-\u9fff0-9（）()\s]{2,40}?\s*\d+\s*号\s*[\u4e00-\u9fff0-9（）()\s]{0,12}?"
        r"(?:终身寿险|养老年金保险|年金保险|两全保险|重大疾病保险|医疗保险|意外伤害保险)"
        r"\s*[（(]?\s*分红型\s*[）)]?)", t)
    if m:
        name = re.sub(r"\s+", "", m.group(1))          # 去除文本层空格
        name = re.sub(r"^产品说明书", "", name)          # 仅去前导「产品说明书」
        name = re.sub(r"^(关于|本产品|产品名称为|上表仅为|上表|下表|以下)\s*", "", name)
        name = name.strip("（( ")                       # 仅去前导括号/空格
        if name and not any(n in name for n in NOISE):
            return name
    # 优先级2：显式「产品名称」标签
    m = re.search(r"产品名称[：:为 ]{0,3}([^\n，,（(]{2,40}?)[\s，,（(]", t)
    if m and not any(n in m.group(1) for n in NOISE):
        return m.group(1).strip("（）() ")
    # 优先级3：（产品代码 前缀
    m = re.search(r"([\u4e00-\u9fff0-9（）()号]{4,40}?)\s*[（(]产品代码", t)
    if m:
        name = re.sub(r"(产品说明书|产品条款|产品费率表|条款费率表运营规则说明书)\s*$", "", m.group(1)).strip("（）() ")
        if name and not any(n in name for n in NOISE):
            return name
    # 优先级4：兜底候选（过滤公司与套话）
    # ★ 候选**止于险种词**（后面只允许跟「（分红型）」等形态词），
    #   不再允许险种词后再接 10 个任意汉字 —— 否则会把广告语一并吞进产品名。
    TYPE = (r"(?:养老年金保险|年金保险|终身寿险|定期寿险|两全保险|重大疾病保险|"
            r"医疗保险|意外伤害保险|护理保险|失能收入损失保险|保险)")
    # 险种词后允许跟最多 2 个括号后缀，用于保留「（福享版）（分红型）」这类版本/形态信息
    cands = re.findall(
        r"([\u4e00-\u9fff0-9]{2,30}?" + TYPE +
        r"(?:\s*[（(][^）)（(]{1,6}[）)]){0,2})", t)
    for c in cands:
        c = re.sub(r"\s+", "", c).strip("（）() ")
        if not c or any(n in c for n in NOISE):
            continue
        if any(b in c for b in BOILER) or any(b in c for b in TABLEWORD):
            continue
        return c
    return None

def detect_insurance_type(t):
    table = [
        ("终身寿险", ["终身寿险"]),
        ("定期寿险", ["定期寿险"]),
        ("年金保险", ["年金保险", "养老年金保险"]),
        ("两全保险", ["两全保险"]),
        ("重大疾病保险", ["重大疾病保险", "重疾"]),
        ("医疗保险", ["医疗保险"]),
        ("意外伤害保险", ["意外伤害保险", "意外险"]),
        ("分红型", ["分红型", "分红保险"]),
        ("万能型", ["万能型", "万能保险"]),
        ("投资连结", ["投资连结", "投连险"]),
    ]
    found = []
    for name, kws in table:
        for kw in kws:
            if kw in t and not re.search(r"非\s*" + re.escape(kw), t):
                found.append(name); break
    # 养老年金保险 -> 归纳为年金保险（已含），去重
    return list(dict.fromkeys(found))

def detect_age(t):
    out = []
    m = re.search(r"投保范围[：: ]?出生满\s*(\d+)\s*天[（(]含[）)]至\s*(\d+)\s*周岁", t)
    if m: out.append(f"出生满{m.group(1)}天至{m.group(2)}周岁")
    m = re.search(r"投保范围[：: ]?(\d+)\s*至\s*(\d+)\s*周岁", t)
    if m and not out: out.append(f"{m.group(1)}~{m.group(2)}周岁")
    m = re.search(r"投保年龄[：: ]?(\d+)\s*至\s*(\d+)\s*周岁", t)
    if m: out.append(f"{m.group(1)}~{m.group(2)}周岁")
    return out

def detect_period(t):
    if "保险期间" in t and "终身" in t: return "终身"
    m = re.search(r"保险期间[：: ]?\s*至\s*(\d+)\s*周岁", t)
    if m: return f"至{m.group(1)}周岁"
    m = re.search(r"保险期间[：: ]?\s*(\d+)\s*年", t)
    if m: return f"{m.group(1)}年"
    return None

def detect_payment(t):
    res = {}
    if "趸交" in t or "一次交清" in t: res["趸交"] = True
    if "期交" in t: res["期交"] = True
    if re.search(r"年交|年缴", t): res["年交"] = True
    if re.search(r"月交|月缴", t): res["月交"] = True
    m = re.search(r"交费期间[：: ]?\s*([^\n]{0,40})", t)
    if m:
        opts = re.findall(r"(\d+)\s*年", m.group(1))
        if opts: res["交费期间_可选年"] = [int(x) for x in opts]
    return res

def detect_annuity(t):
    if "养老年金" not in t: return {}
    res = {}
    # 开始领取年龄：取首次「养老年金开始领取(日/年龄)」段（限首计划，去重）
    m = re.search(r"养老年金开始领取(?:日|年龄)([\s\S]{0,200})", t)
    if m:
        ages = []
        for a in re.findall(r"年满\s*(\d+)\s*周岁", m.group(1)):
            if a not in ages: ages.append(a)
        if ages: res["开始领取年龄"] = "年满" + "/".join(ages) + "周岁可选"
    if "开始领取年龄" not in res:
        m = re.search(r"养老年金开始领取(?:日|年龄)[^\n]{0,80}?(\d+)\s*岁", t)
        if m: res["开始领取年龄"] = f"{m.group(1)}岁起"
    # 保证领取期间：优先「保证领取期间…按 N 个保单年度」，其次「保证领取N年」
    m = re.search(r"保证领取(?:期间)?[：: ]?(?:[^。\n]{0,100}?)(\d+)\s*个保单年度", t)
    if m:
        res["保证领取期间"] = f"{m.group(1)}年(按年领)"
    else:
        m = re.search(r"保证领取\s*(\d+)\s*年", t)
        if m: res["保证领取期间"] = f"{m.group(1)}年"
    if "按年领取或按月领取" in t or "按月领取" in t or "按年领取" in t:
        res["领取方式"] = "年领/月领可选"
    return res

def extract_section(t, start_kws, stop_kws, prefer=None, maxlen=500):
    # 找最靠前且(若指定 prefer)后文含 prefer 的起始点；截到首个 stop
    best = None
    for sk in start_kws:
        for m in re.finditer(re.escape(sk), t):
            seg = t[m.start():m.start()+maxlen]
            if prefer and prefer not in seg[:60]:
                continue
            best = m; break
        if best: break
    if not best: return None
    end = len(t)
    for st in stop_kws:
        mm = re.search(re.escape(st), t[best.start():best.start()+maxlen])
        if mm:
            end = best.start() + mm.start()
            break
    return t[best.start():end].strip()

def detect_demo(t):
    m = re.search(r"利益演示([\s\S]{0,700})", t)
    if not m:
        return {"含示例利益演示": False}
    seg = m.group(1)
    if "年交保费" not in seg and "趸交" not in seg:
        return {"含示例利益演示": False}
    am = re.search(r"(\d+)\s*岁\s*的?\s*\S{0,6}?(先生|女士)", seg)
    pm = re.search(r"年交保费\s*([\d,]+)\s*元", seg)
    if am and pm:
        return {"含示例利益演示": True,
                "示例": f"{am.group(1)}岁{am.group(2)}，年交保费{pm.group(1)}元"}
    if am:
        return {"含示例利益演示": True, "示例": f"{am.group(1)}岁{am.group(2)}（未解析到保费）"}
    if pm:
        return {"含示例利益演示": True, "示例": f"年交保费{pm.group(1)}元（未解析到示例人物）"}
    return {"含示例利益演示": True, "示例": "（含利益演示但格式未解析）"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json"); ap.add_argument("--out")
    args = ap.parse_args()
    data = json.load(open(args.json, encoding="utf-8"))
    raw = build_text(data)
    t = dedup_cjk(raw)

    rec = {}
    rec["文档类别(初判)"] = "产品说明书(描述性)" if ("投保范围" in t or "产品基本特征" in t) else "保险计划书(含利益演示)"
    rec["产品名称"] = get_product_name(t)
    rec["险种类型"] = detect_insurance_type(t)
    rec["投保年龄"] = detect_age(t)
    rec["保险期间"] = detect_period(t)
    rec["交费方式"] = detect_payment(t)
    rec["养老年金专属"] = detect_annuity(t)
    rec["红利方式"] = (["现金领取","累积生息","抵交保费","购买交清增额","进入万能账户"]
                       if "分红" in t else "非分红(普通型)")
    if "分红" in t:
        modes = []
        for kw, lab in [("现金领取","现金领取"),("累积生息","累积生息"),
                        ("抵交保费","抵交保费"),("交清增额","购买交清增额"),
                        ("万能账户","进入万能账户")]:
            if kw in t: modes.append(lab)
        rec["红利方式"] = modes
    resp = extract_section(t, ["保险责任"],
                           ["责任免除","（四）","（五）","（六）","三、利益演示","红利来源","特别红利","四、犹豫期"],
                           prefer="本合同")
    rec["保障责任(摘录)"] = (resp[:360] + "…") if resp else None
    excl = extract_section(t, ["责任免除"],
                           ["红利来源","特别红利","三、利益演示","（六）","（五）","四、犹豫期","保证领取"],
                           prefer="因下列")
    rec["责任免除(摘录)"] = (excl[:240] + "…") if excl else None
    rec["条款要点关键词"] = [k for k in ["犹豫期","宽限期","等待期","复效","现金价值","退保","保证领取"] if k in t]
    rec["利益演示"] = detect_demo(t)
    rec["IRR适用性说明"] = ("产品说明书无个性化保费/年龄，IRR 不可直接算；"
                           "如需测算请提供具体被保人年龄、性别、保费、交费期，或对应计划书/利益演示表。"
                           if rec["文档类别(初判)"].startswith("产品说明书") else
                           "可作个性化 IRR 测算。")

    print(json.dumps(rec, ensure_ascii=False, indent=2))
    if args.out:
        json.dump(rec, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("\n已写出:", args.out)

if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
