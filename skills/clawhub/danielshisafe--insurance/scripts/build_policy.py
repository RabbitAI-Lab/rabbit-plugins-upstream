#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_policy.py - 保险计划书分析大师·说明书→IRR 自动链路。

输入：extract.py 产出的 JSON（产品说明书/计划书的表格抽取结果）。
输出：构造 irr.py 可直接消费的 policy JSON，并可选直接跑出逐年 IRR。

落实 SKILL.md §5.1 的承诺：储蓄理财类说明书含「示例利益演示表」时，
必须抽出来喂 irr.py 实算 总利益 + IRR。本脚本把这一步自动化。

列映射策略（针对德华安顾等常见分红演示表，已用真实说明书验证）：
  1) 优先用现成「生存总利益/总利益」列（SKILL §7.11 铁律①）：
       列头含「生存总利益」且「低档」→ 保证总利益；
       列头含「生存总利益」且「中性」→ 演示总利益（中档红利）。
  2) 若无现成总利益列，用组件求和（§7.11）：
       总利益(演示) = 现金价值 + 累积红利(中性) + 特别红利(中性) + 养老年金(carry-forward)；
       总利益(保证) = 现金价值 + 养老年金保证。
  3) 保费列：列头含「年度保险费/年交保费」→ 逐期保费；>0 的末年即交费期满。
     趸交判定：仅第1年（或投保时）有保费。
  4) 年金表稀疏（仅列 30/35/40…）→ 养老年金自首次给付年起 carry-forward 补齐（§7.10.1③）。
  5) ★ 零保额铁律（§7.11）：任何「保额型」列（含「保额/保险金额」且不含「现金价值」，
     如「累积红利保额」「基本保额」）**一律不映射到价值字段**，只登记告警。
     增额红利唯一能进总利益的是它的**现金价值**列。

用法：
  python build_policy.py extract.json --name 福享版 [--out policy.json] [--run] [--years 5,10,20,30,40,50,60,75]
  --run 直接调用 irr.py 输出 CSV（默认 <out同目录>/irr_<name>.csv）。
"""
import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))


def dedup_cjk(s):
    """去掉中文文本层的「逐字重复」伪影：保保单单年年年度度 → 保单年度。

    部分 PDF 用重叠字重模拟加粗，文本层里每个汉字都会出现两次。
    recognize_spec.py 早就有这一步，build_policy.py 此前没有，
    导致这类表的表头关键词全部匹配不上，整表被判为「未找到利益演示表」。
    只处理 CJK 区间，不影响数字与符号。
    """
    out = []
    for ch in s:
        if out and ch == out[-1] and ("\u4e00" <= ch <= "\u9fff"):
            continue
        out.append(ch)
    return "".join(out)


def norm(x):
    if x is None:
        return ""
    # ★ NFKC 归一化：部分计划书 PDF 的 ToUnicode 映射会把汉字映射成「康熙部首」
    #   （U+2F00–U+2FDF，如 ⾦ U+2FA6 代替 金 U+91D1、⽣ U+2F63 代替 生），
    #   导致「现⾦价值」匹配不到关键词「现金价值」，列定位全线失守、静默产出空结果。
    #   NFKC 会将其还原为对应的 CJK 统一汉字，同时保留全半角数字的可用性。
    s = unicodedata.normalize("NFKC", str(x))
    s = re.sub(r"\s+", "", s)
    return dedup_cjk(s)


def find_demo_table(data):
    """返回最可能是利益演示表的 table（含 保单年度 数字列 + 现金价值/生存总利益/养老年金 之一）。"""
    pages = data.get("data", {}).get("pages", []) if data.get("kind") == "pdf" else []
    cands = []
    for p in pages:
        for tb in p.get("tables", []):
            # ★ 噪声碎片过滤：真实利益演示表必然逐年列出 ≥5 个保单年度。
            #   绝对定位绘制的 PDF（无表格线）会被 extract 拆成大量 2~4 行碎片，
            #   不过滤就会被当成演示表，最终静默产出「总保费=0、最大年度=2」的垃圾结果。
            if len(tb) < 5:
                continue
            flat = " ".join(norm(c) for r in tb for c in r)
            score = 0
            if "保单年度" in flat or (len(tb) > 1 and re.search(r"^\d+$", norm(tb[1][0]))):
                score += 2
            for kw in ["生存总利益", "总利益", "现金价值", "累积红利", "养老年金", "特别红利"]:
                if kw in flat:
                    score += 1
            if score >= 2:
                cands.append((score, tb))
    if not cands:
        return None
    # 同分时优先取行数/列数更大的表：演示表通常比同页的说明性小表大得多
    cands.sort(key=lambda x: (-x[0], -len(x[1]),
                              -max((len(r) for r in x[1]), default=0)))
    return cands[0][1]


def col_header_texts(tb, data_rows_start):
    """对每一列，拼接其表头区（数据行之前）的所有 token。

    ★ 合并单元格还原：PDF 抽取结果里，跨列合并的表头只在**首格**有值、右侧子列为空。
      例如三层表头「生存总利益 ‖ 低档红利/中性红利 ‖ 万能最低保证利率/中性演示利率」，
      抽取后 col3 只剩「万能中性演示利率(3.5%)」，丢了上层的「生存总利益/低档红利」，
      导致列定位把保证档与演示档认错（静默选错列，比报错更危险）。
      正确做法：先在**每一行内**把空格右向填充为左侧最近的有效标签，再按列纵向拼接。
    """
    ncol = max((len(r) for r in tb[:data_rows_start]), default=len(tb[0]))
    filled = []
    for ri in range(data_rows_start):
        row = tb[ri]
        vals = [norm(row[ci]) if ci < len(row) else "" for ci in range(ncol)]
        out = []
        last = ""
        for v in vals:
            if v:
                last = v
            out.append(last)
        filled.append(out)
    heads = ["".join(filled[ri][ci] for ri in range(data_rows_start))
             for ci in range(ncol)]
    # 兼容旧行为：整列仍为空时，继承左侧最近的分组标签
    GROUP_KW = ["生存总利益", "总利益演示", "总现金价值", "身故/全残总利益"]
    last_group = ""
    new_heads = []
    for h in heads:
        base = h.replace("低档", "").replace("中性", "").replace("高档", "")
        if any(k in base for k in GROUP_KW):
            last_group = base if base else last_group
        if not h:
            new_heads.append(last_group)
        else:
            new_heads.append(h)
    return new_heads


def is_death(h):
    """「身故/全残给付型列」判定：身故、全残赔付不是能被投保人拿回的价值。

    ★ 零保额铁律（SKILL.md §7.1 / §7.11）：生存总利益只算「退保/满期能拿回多少」，
      身故/全残保险金**一分都不能进任何价值字段**。

    ★ 为什么 is_sa 拦不住它：is_sa 只认「保额」「保险金额」，而真实表头写的是
      「身故/全残**保险金**」——少了「额」字，关键词匹配不上，整列放行。

    ★ 实测坑（福享版 56 列宽表）：表头重建后「生存总利益」与「对应的身故/全残保险金」
      被拼进了同一个标签（如「总利益演示生存总利益对应的身故/全残保险金中性」），
      于是身故总利益列（首年 16000、第 5 年 80000）被当成**演示生存总利益**
      （首年应为 2005、第 5 年应为 27000）映射进 policy，演示 IRR 被严重高估。
      这类「标签自相矛盾」的列一律不映射到价值字段，交由 main() 告警。
    """
    return ("身故" in h or "全残" in h) and "现金价值" not in h


def is_sa(h):
    """「保额型列」判定：只表达保险金额，不表达价值。

    ★ 零保额铁律（SKILL.md §7.11）：生存总利益 = 退保/满期能拿回多少钱，
      保额（基本保额、红利保额、保险金额、身故保额…）**一分钱都不能进任何价值字段**。
      典型陷阱：「累积红利保额」是增额红利的**保额**，量级常与基本保额相当（几十万），
      若被当成现金价值加进总利益，演示口径会被放大到荒谬。
      唯一例外是列名里**同时写了「现金价值」**（如「累积红利保额对应的现金价值」），
      那才是能进总利益的口径。
    """
    return ("保额" in h or "保险金额" in h) and "现金价值" not in h


def _has_survival(tb, cols):
    head = "".join(str(c) for r in tb[:cols["data_start"]] for c in r)
    return "生存总利益" in head or "总利益" in head


def locate_columns(tb):
    """定位 年份/保费/保证总利益/演示总利益/年金/现金价值/累积红利/增额红利现价/特别红利 列。

    ★ 零保额铁律：任何「保额型」列（含保额/保险金额且不含现金价值）一律不映射到价值字段，
      只在 sa_skipped 里登记，交由 main() 告警（SKILL.md §7.11）。
    """
    # ★ data_start 判定：不能只看首列「保单年度」。
    #   真实演示表常因合并单元格导致首列稀疏（仅第 5/10/15… 年有值，其余为空），
    #   只看首列会把前几行真实数据误判成表头吞掉 —— 保费少算、IRR 被成倍虚报。
    #   改为「首个含 ≥2 个纯数字单元格的行」：表头行（保单年度/年末已达年龄…）不含数字，
    #   空分隔行也不含，只有数据行满足。
    NUMCELL = re.compile(r"^-?[\d,]+(\.\d+)?$")
    data_start = None
    for ri, r in enumerate(tb):
        if ri == 0:
            continue
        n = sum(1 for c in r if NUMCELL.match(norm(c)))
        if n >= 2:
            data_start = ri
            break
    if data_start is None:
        data_start = 1
    heads = col_header_texts(tb, data_start)

    year_col = 0
    prem_col = None
    g_col = None
    d_col = None
    ann_col = None
    cv_col = None
    cd_col = None
    tb_col = None
    pu_g_col = None      # 增额红利/交清增额 的「现金价值」列（保证档）
    pu_d_col = None      # 增额红利/交清增额 的「现金价值」列（中性/演示档）
    sa_skipped = []      # 被零保额铁律拦下的列

    PU_KW = ("红利保额", "增额红利", "交清增额")

    for ci, h in enumerate(heads):
        # 总利益列：生存总利益 / 总利益演示（排除 身故/全残总利益）
        # ★ is_death 守卫：标签里带「身故/全残」的一律不进价值字段。
        #   宽表（实测 56 列）表头重建常把「生存总利益」与「对应的身故/全残保险金」
        #   拼成同一个标签，此时该列数据是身故赔付量级（首年 16000 vs 生存 2005），
        #   选它等于把身故总利益当演示收益 —— 静默高估，必须拦下。
        if (("生存总利益" in h) or ("总利益" in h and "身故" not in h and "全残" not in h)
                or "总现金价值" in h):
            if is_death(h):
                sa_skipped.append((ci, h))
            elif "低档" in h or "保证" in h:
                g_col = ci
            elif "中性" in h or "高档" in h or "演示" in h:
                d_col = ci
            # 纯分组标签列（无 低档/中性/演示 修饰）跳过，数据在子列
        # ★ 保费列关键词：真实表头写法极多（年缴/年交/期缴/期交/当年…）。
        #   早前只认「年度保险费/年交保费/期交保费」，遇到「年缴保险费」会整列漏判，
        #   导致 premiums 全 0、IRR 无意义。此处补全写法，并用排除词防止把给付类列当保费。
        _prem_kw = ("年度保险费", "年交保费", "期交保费", "年缴保险费", "年缴保费",
                    "期缴保险费", "期缴保费", "当年保险费", "当年保费", "保险费", "保费")
        _prem_ex = ("累计", "身故", "生存", "满期", "返还", "给付", "保险金额",
                    "保额", "豁免", "残疾", "医疗", "红利", "年金", "账户")
        if any(k in h for k in _prem_kw) and not any(x in h for x in _prem_ex):
            prem_col = ci
        # ★ 年金/生存金列：真实表头不一定写「养老年金」，也可能是「生存保险金」「生存金」。
        #   漏判会让被保险人已领取的生存金整列不进总利益，IRR 被系统性低估。
        #   排除「累计已领取…」（用当年列 + carry-forward 推导，避免与当年列双算）。
        if (("养老年金" in h or "生存保险金" in h or "生存金" in h or "年金" in h)
                and "现金价值" not in h and "累计" not in h and "身故" not in h
                and "满期" not in h and not is_sa(h)):
            ann_col = ci
        if ("现金价值" in h and "红利" not in h and "身故" not in h and "累积" not in h
                and "生存总利益" not in h and cv_col is None):
            cv_col = ci
        # ── 红利列分类（三类互斥，先判增额，否则同一列会被 cd 与 pu 同时命中而双算）──
        if any(k in h for k in PU_KW):
            # 增额红利 / 交清增额：唯一能进总利益的是它的**现金价值**列，
            # 「累积红利保额」只是保额，量级与基本保额相当，进了就是灾难（零保额铁律）
            if "现金价值" in h:
                if "低档" in h or "保证" in h:
                    pu_g_col = ci
                else:
                    pu_d_col = ci
            else:
                sa_skipped.append((ci, h))
        elif "累积红利" in h or "现金红利" in h:
            if is_sa(h):
                sa_skipped.append((ci, h))
            elif "中性" in h or "高档" in h or "演示" in h or \
                    ("现金价值" in h and "低档" not in h):
                cd_col = ci
        elif "特别红利" in h:
            if is_sa(h):
                sa_skipped.append((ci, h))
            elif "中性" in h or "高档" in h or "演示" in h or \
                    ("现金价值" in h and "低档" not in h):
                tb_col = ci
        elif is_sa(h):
            # 其余任何保额列（如「基本保额」「身故保额」）一律拦下，仅作告警
            sa_skipped.append((ci, h))
    if g_col is None and d_col is None and cv_col is not None:
        g_col = cv_col
        d_col = cv_col
    return dict(year=year_col, prem=prem_col, g=g_col, d=d_col, ann=ann_col,
                cv=cv_col, cd=cd_col, tb=tb_col,
                pu_g=pu_g_col, pu_d=pu_d_col, sa_skipped=sa_skipped,
                data_start=data_start)


def build(tb, cols):
    year = cols["year"]; prem = cols["prem"]; g = cols["g"]; d = cols["d"]
    ann = cols["ann"]; cd = cols["cd"]; tbonus = cols["tb"]
    pu_g = cols.get("pu_g"); pu_d = cols.get("pu_d")
    rows = {}
    maxyr = 0
    # ★ 年份递推：首列「保单年度」稀疏时（合并单元格只留下 5/10/15…），
    #   空行不能整行 continue —— 那会丢掉整段保费与现价，IRR 被成倍虚报。
    #   改为：首列有明确年份就以其为准并对齐计数，为空则按上一年度 +1 递推。
    seq = 0
    for r in tb[cols["data_start"]:]:
        y_txt = norm(r[year])
        if re.match(r"^\d+$", y_txt):
            y = int(y_txt)
            seq = y
        else:
            seq += 1
            y = seq
        if y <= 0:
            continue
        maxyr = max(maxyr, y)
        row = {}

        def get(c):
            if c is None or c >= len(r):
                return 0.0
            v = norm(r[c]).replace(",", "")
            try:
                return float(v)
            except Exception:
                return 0.0

        row["prem"] = get(prem)
        row["g"] = get(g)
        row["d"] = get(d)
        row["ann"] = get(ann)
        row["cd"] = get(cd)
        row["tb"] = get(tbonus)
        row["pug"] = get(pu_g) if pu_g is not None else 0.0
        row["pud"] = get(pu_d) if pu_d is not None else 0.0
        rows[y] = row
    L = maxyr + 1
    premiums = [0.0] * L
    gv = [0.0] * L; dv = [0.0] * L
    annv = [0.0] * L; cdv = [0.0] * L; tbv = [0.0] * L
    pugv = [0.0] * L; pudv = [0.0] * L
    la = 0.0
    for y in range(L):
        if y in rows:
            rr = rows[y]
            if rr["prem"] > 0:
                premiums[y - 1] = rr["prem"]   # 第 y 年初 = 第 y-1 索引
            gv[y] = rr["g"]; dv[y] = rr["d"]
            if rr["ann"] > 0:
                la = rr["ann"]
            annv[y] = la
            cdv[y] = rr["cd"]; tbv[y] = rr["tb"]
            pugv[y] = rr["pug"]; pudv[y] = rr["pud"]
        else:
            gv[y] = gv[y - 1] if y > 0 else 0.0
            dv[y] = dv[y - 1] if y > 0 else 0.0
            annv[y] = la
            cdv[y] = cdv[y - 1] if y > 0 else 0.0
            tbv[y] = tbv[y - 1] if y > 0 else 0.0
            pugv[y] = pugv[y - 1] if y > 0 else 0.0
            pudv[y] = pudv[y - 1] if y > 0 else 0.0
    return premiums, gv, dv, annv, cdv, tbv, pugv, pudv, maxyr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--name", default="policy")
    ap.add_argument("--out")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--years", default="5,10,15,20,30,40,50,60,75")
    args = ap.parse_args()

    data = json.load(open(args.json, encoding="utf-8"))
    tb = find_demo_table(data)
    if tb is None:
        kind = data.get("kind")
        if kind and kind != "pdf":
            print(f"ERROR: 未找到利益演示表（本脚本只解析 extract.py 的 **PDF** 抽取结果，"
                  f"当前输入 kind={kind}）。\n"
                  f"  xlsx/docx 请按 SKILL §7.11 手工构造 policy JSON："
                  f"用 extract.py 定位「保单年度/现金价值/累积红利/养老年金」等列再喂 irr.py。",
                  file=sys.stderr)
        else:
            print("ERROR: 未找到利益演示表。若该 PDF 为绝对定位绘制（无表格线），"
                  "extract.py 抽不到表格属正常，请改用 "
                  "scripts/parse_pdf_table.py <file.pdf> --scan 按坐标重建演示表。",
                  file=sys.stderr)
        sys.exit(1)
    cols = locate_columns(tb)
    premiums, gv, dv, annv, cdv, tbv, pugv, pudv, maxyr = build(tb, cols)

    # ★ 硬守卫：抓不到保费 / 年度过少时一律硬失败。
    #   没有保费就没有现金流出，IRR 在数学上无意义；只有 2~3 个年度说明选中的是噪声碎片。
    #   这两种情况过去会以 exit 0 静默产出垃圾结果（比报错更危险），此处一律拦下。
    if sum(premiums) <= 0:
        print("ERROR: 未从表中解析出任何保费（总保费 = 0）。没有保费支出就构不成现金流，"
              "IRR 无法计算，本脚本拒绝产出结果。\n"
              "  常见原因：该 PDF 为绝对定位绘制（无表格线），extract.py 只抽到碎片表，"
              "真正的利益演示表未被识别为表格。\n"
              "  处理：改用 scripts/parse_pdf_table.py <file.pdf> --scan 按坐标重建演示表，"
              "或按 SKILL §7.11 手工构造 policy JSON。", file=sys.stderr)
        sys.exit(1)
    if maxyr < 5:
        print(f"ERROR: 利益演示表仅解析出 {maxyr} 个保单年度，明显不是逐年演示表"
              "（极可能是噪声碎片表）。\n"
              "  处理：改用 scripts/parse_pdf_table.py <file.pdf> --scan 按坐标重建，"
              "或按 SKILL §7.11 手工构造 policy JSON。", file=sys.stderr)
        sys.exit(1)

    # ★ 零保额铁律：被拦下的保额列必须显式告知，否则使用者会以为红利被漏计
    for ci, h in cols.get("sa_skipped", []):
        print(f"INFO: 第 {ci} 列「{h}」是**保额型**列，按零保额铁律未计入总利益。"
              "若要计增额红利，请改用「增额红利的现金价值」列（§7.11）。", file=sys.stderr)

    pol = {"start_date": "2026-01-01", "premiums": premiums}
    if _has_survival(tb, cols):
        pol["cv_guaranteed"] = gv
        pol["cv_demo"] = dv
    else:
        gsum = [gv[y] + annv[y] + pugv[y] for y in range(len(gv))]
        dsum = [dv[y] + cdv[y] + tbv[y] + annv[y] + pudv[y] for y in range(len(dv))]
        pol["cv_guaranteed"] = gsum
        pol["cv_demo"] = dsum
    total_ok = any(v != 0 for v in pol.get("cv_guaranteed", [])) or \
        any(v != 0 for v in pol.get("cv_demo", []))
    if not total_ok:
        # ★ 硬失败而不是只告警：全零总利益一旦被拿去跑 irr.py，得到的 IRR 必然是失真的。
        #   与 §7.17 的三道硬失败同一原则——抽取层「匹配不上」绝不退化成跳过或取 0。
        print("ERROR: 自动列映射未取到任何有效总利益数值（很可能是合并表头导致表头列与数据列错位，"
              "或「生存总利益」列被零保额/身故守卫拦下）。\n"
              "  处理：按 SKILL §7.11 铁律①，直接用说明书打印的「生存总利益/总利益」列"
              "手工构造 policy（参考 examples/ 中的做法）。\n"
              "  若上方出现大量「身故/全残」列的 INFO，说明表头重建把生存总利益与身故总利益"
              "拼成了同一个标签，本脚本无法可靠区分，必须手工指定列。",
              file=sys.stderr)
        sys.exit(1)
    if all(v == 0 for v in pol["cv_guaranteed"]):
        del pol["cv_guaranteed"]
    if "cv_demo" in pol and all(v == 0 for v in pol["cv_demo"]):
        del pol["cv_demo"]

    out = args.out or os.path.join(os.path.dirname(os.path.abspath(args.json)),
                                   f"policy_{args.name}.json")
    json.dump(pol, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"保费(前12年): {premiums[:12]}")
    print(f"交费期推定: {sum(1 for p in premiums if p>0)} 年; 总保费: {sum(premiums):.0f}")
    print(f"最大年度: {maxyr}; 年金列={'有' if cols['ann'] is not None else '无'}; "
          f"现成总利益列={'有' if _has_survival(tb, cols) else '无(组件求和)'}")
    print(f"零保额铁律：拦下保额列 {len(cols.get('sa_skipped', []))} 个；"
          f"增额红利现价列={'有' if (cols.get('pu_d') or cols.get('pu_g')) else '无'}")
    print(f"已写出 policy: {out}")
    if args.run:
        csvp = os.path.join(os.path.dirname(out), f"irr_{args.name}.csv")
        irr = os.path.join(HERE, "irr.py")
        cmd = [sys.executable, irr, "--input", out, "--years", args.years, "--out", csvp]
        print("\n>>> 运行 irr.py:")
        subprocess.run(cmd)


if __name__ == "__main__":
    try:
        from _feedback_hook import install; install()
    except Exception:
        pass
    main()
