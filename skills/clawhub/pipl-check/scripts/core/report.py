"""报告生成器 — 附件1自查表 + 附件2影响评估，精确匹配官模板式"""

import os
from datetime import datetime
from .audit_items import AUDIT_ITEMS, IMPACT_ITEMS

CHECK_ON  = "■"
CHECK_OFF = "□"


def _cb(sel: bool) -> str:
    return CHECK_ON if sel else CHECK_OFF


# ═══════════════════════════════════════════════════════════════════
#  附件1：合规审计自查表  —  Markdown
# ═══════════════════════════════════════════════════════════════════

def gen_audit_markdown(results: list[dict], org_name: str = "") -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []
    lines.append("# 个人信息保护合规审计自查表")
    lines.append(f"**编制时间**: {now}")
    if org_name:
        lines.append(f"**企业/组织名称**: {org_name}")
    lines.append("**依据法规**: 《小型个人信息处理者个人信息保护简化措施规定》（国家互联网信息办公室、公安部令第25号）附件1")
    lines.append("")

    total = len(results)
    compliant = sum(1 for r in results if r["status"] == "合规")
    noncompliant = sum(1 for r in results if r["status"] == "不合规")
    na = sum(1 for r in results if r["status"] == "不适用")
    skipped = sum(1 for r in results if r["status"] == "跳过")

    lines.append("## 概览")
    lines.append(f"| 总计 | ✅ 合规 | ⚠️ 不合规 | ☑ 不适用 | 跳过 |")
    lines.append("|:---:|:------:|:---------:|:--------:|:----:|")
    lines.append(f"| {total} | {compliant} | {noncompliant} | {na} | {skipped} |")
    if noncompliant == 0:
        lines.append("\n**评估结论**: ✅ 全部合规")
    elif noncompliant <= 3:
        lines.append(f"\n**评估结论**: ⚠️ 存在 {noncompliant} 项不合规，建议尽快整改")
    else:
        lines.append(f"\n**评估结论**: ❌ 存在 {noncompliant} 项不合规，需全面整改")
    lines.append("")

    lines.append("## 自查明细")
    lines.append("")
    lines.append("| 序号 | 合规审计事项 | 合规情况自查 | 不合规及整改情况说明 |")
    lines.append("|:---:|:------------|:-------------|:---------------------|")
    for r in results:
        item = AUDIT_ITEMS[r["id"] - 1]
        # Vertical checkboxes
        cb_lines = []
        for opt in ["合规", "不合规", "不适用"]:
            cb_lines.append(f"{_cb(r['status'] == opt)} {opt}")
        status_text = "<br>".join(cb_lines)
        note = r.get("note", "") or "—"
        lines.append(f"| {r['id']} | {item['name']} | {status_text} | {note} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("本人已对上述事项进行了合规审计自查，并如实填写自查情况，如有不实，承担相应法律责任。")
    lines.append("")
    lines.append("合规审计负责人签字：______________　　日期：______________")
    lines.append("")
    lines.append("*免责声明：本报告由 pipl-check 工具辅助生成，仅供企业自查参考，不构成合规保证。*")
    return "\n".join(lines)


def gen_audit_pdf(results: list[dict], output_path: str, org_name: str = ""):
    """PDF版合规审计自查表 — 官方模板格式：复选框竖排三行 + 申明签字"""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor, white, grey
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    # Font
    FONT = "Helvetica"
    for fp, fn in [
        ("/System/Library/Fonts/PingFang.ttc", "PingFang"),
        ("/System/Library/Fonts/STHeiti Light.ttc", "STHeiti"),
    ]:
        try:
            pdfmetrics.registerFont(TTFont(fn, fp))
            FONT = fn
            break
        except Exception:
            continue

    now = datetime.now().strftime("%Y年%m月%d日")
    doc = SimpleDocTemplate(output_path, pagesize=A4,
        leftMargin=12*mm, rightMargin=12*mm, topMargin=15*mm, bottomMargin=15*mm)

    s_title = ParagraphStyle("T", fontName=FONT, fontSize=17, alignment=TA_CENTER, spaceAfter=3*mm)
    s_info = ParagraphStyle("I", fontName=FONT, fontSize=11, alignment=TA_CENTER, textColor=grey, spaceAfter=4*mm)
    s_h = ParagraphStyle("H", fontName=FONT, fontSize=10, leading=14)
    s_c = ParagraphStyle("C", fontName=FONT, fontSize=9.5, leading=14)
    s_cb = ParagraphStyle("CB", fontName=FONT, fontSize=9.5, leading=13)
    s_decl = ParagraphStyle("D", fontName=FONT, fontSize=11, leading=18, spaceBefore=4*mm, alignment=TA_JUSTIFY)
    s_sig = ParagraphStyle("Sg", fontName=FONT, fontSize=11.5, leading=18, spaceBefore=2*mm)
    s_footer = ParagraphStyle("F", fontName=FONT, fontSize=10, textColor=grey, alignment=TA_CENTER, spaceBefore=3*mm)

    story = []
    story.append(Paragraph("小型个人信息处理者个人信息保护合规审计自查表", s_title))
    story.append(Paragraph(
        f"依据：《小型个人信息处理者个人信息保护简化措施规定》（国家互联网信息办公室、公安部令第25号）附件1", s_info))
    if org_name:
        story.append(Paragraph(f"企业/组织名称：{org_name}", s_info))
    story.append(Paragraph(f"编制时间：{now}", s_info))
    story.append(Spacer(1, 2*mm))

    # Summary row
    total = len(results)
    compliant = sum(1 for r in results if r["status"] == "合规")
    noncompliant = sum(1 for r in results if r["status"] == "不合规")
    na = sum(1 for r in results if r["status"] == "不适用")
    sd = [["总计", "合规", "不合规", "不适用"]] + [[str(total), str(compliant), str(noncompliant), str(na)]]
    st = Table(sd, colWidths=[28*mm]*4)
    st.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.2, HexColor("#aaa")),
        ('BACKGROUND', (0,0), (-1,0), HexColor("#d0d8e8")),
        ('FONTNAME', (0,0), (-1,-1), FONT),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(st)
    story.append(Spacer(1, 3*mm))

    # ── Main table: 序号 | 合规审计事项 | 合规情况自查 | 不合规及整改情况说明 ──
    hdr = [Paragraph("<b>序号</b>", s_h), Paragraph("<b>合规审计事项</b>", s_h),
           Paragraph("<b>合规情况自查</b>", s_h), Paragraph("<b>不合规及整改情况说明</b>", s_h)]
    tbl = [hdr]

    for r in results:
        item = AUDIT_ITEMS[r["id"] - 1]
        # Status: vertical (three lines)
        cb_lines = []
        for opt in ["合规", "不合规", "不适用"]:
            cb_lines.append(f"{_cb(r['status'] == opt)} {opt}")
        status_txt = "<br/>".join(cb_lines)

        # Full description — no truncation
        desc = item["desc"]
        desc = desc.replace("；（", "；<br/>（")
        desc = desc.replace("：（", "：<br/>（")
        note = r.get("note", "") or "—"

        tbl.append([
            Paragraph(str(r["id"]), s_c),
            Paragraph(desc, s_c),
            Paragraph(status_txt, s_cb),
            Paragraph(note, s_c)
        ])

    col_w = [8*mm, 94*mm, 22*mm, 46*mm]
    mt = Table(tbl, colWidths=col_w, repeatRows=1)
    cmds = [
        ('GRID', (0,0), (-1,-1), 0.2, HexColor("#bbb")),
        ('BACKGROUND', (0,0), (-1,0), HexColor("#d0d8e8")),
        ('FONTNAME', (0,0), (-1,-1), FONT),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (0,-1), 'CENTER'), ('ALIGN', (2,0), (2,-1), 'CENTER'),
    ]
    for i in range(2, len(tbl), 2):
        cmds.append(('BACKGROUND', (0,i), (-1,i), HexColor("#f5f7fa")))
    mt.setStyle(TableStyle(cmds))
    story.append(mt)

    # ── 备注行（全幅，约6行高度） ──
    note_data = [[Paragraph("备注：其他需说明的情况及证明材料（可另附页）", s_c)]]
    note_tbl = Table(note_data, colWidths=[sum(col_w)])
    note_tbl.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.2, HexColor("#bbb")),
        ('FONTNAME', (0,0), (-1,-1), FONT),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 25),
        ('BOTTOMPADDING', (0,0), (-1,-1), 25),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(note_tbl)

    # ── 申明 + 签字（冒号对齐） ──
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        "本人已对上述事项进行了合规审计自查，并如实填写自查情况，"
        "如有不实，承担相应法律责任。", s_decl))
    story.append(Spacer(1, 3*mm))
    sig_tbl = Table([
        [Paragraph("合规审计负责人签字", s_sig), Paragraph("：", s_sig), Paragraph("__________________　　", s_sig)],
        [Paragraph("日　　　　期", s_sig), Paragraph("：", s_sig), Paragraph("__________________　　", s_sig)],
    ], colWidths=[48*mm, 5*mm, 67*mm])
    sig_tbl.setStyle(TableStyle([
        ('ALIGN', (0,0), (0,-1), 'RIGHT'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        ('ALIGN', (2,0), (2,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('FONTNAME', (0,0), (-1,-1), FONT),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ]))
    story.append(sig_tbl)

    story.append(Spacer(1, 5*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=grey))
    story.append(Paragraph(
        "免责声明：本报告由 pipl-check 工具辅助生成，仅供企业自查参考，不构成合规保证。"
        "最终合规责任由企业自行承担。", s_footer))
    doc.build(story)
    print(f"  ✅ PDF审计自查表: {output_path}")


# ═══════════════════════════════════════════════════════════════════
#  附件2：个人信息保护影响评估表
# ═══════════════════════════════════════════════════════════════════

def _impact_cell(answer: str, choices: list[str]) -> str:
    parts = []
    for opt in choices:
        parts.append(f"{_cb(answer == opt)} {opt}")
    return "  ".join(parts)


def gen_impact_markdown(results: list[dict], org_name: str = "") -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []
    lines.append("# 个人信息保护影响评估表")
    lines.append(f"**编制时间**: {now}")
    if org_name:
        lines.append(f"**企业/组织名称**: {org_name}")
    lines.append("**依据法规**: 《小型个人信息处理者个人信息保护简化措施规定》（国家互联网信息办公室、公安部令第25号）附件2")
    lines.append("")
    lines.append("| 序号 | 影响评估情形 | 影响评估内容 | 影响评估结论 | 备注（其他需说明的情况及证明材料） |")
    lines.append("|:---:|:------------|:------------|:-------------|:----|")

    for scenario in results:
        s_item = IMPACT_ITEMS[scenario["id"] - 1]
        answers = scenario.get("answers", [])
        note = scenario.get("note", "") or "—"
        for idx, ans in enumerate(answers):
            criterion = s_item["criteria"][idx]
            status_text = _impact_cell(ans["answer"], criterion["choices"])
            seq = str(scenario["id"]) if idx == 0 else ""
            name = s_item["name"] if idx == 0 else ""
            n = note if idx == len(answers) - 1 else ""
            lines.append(f"| {seq} | {name} | {criterion['q']} | {status_text} | {n} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("本人已对上述事项进行了影响评估，并如实填写影响评估情况，如有不实，承担相应法律责任。")
    lines.append("")
    lines.append("影响评估负责人签字：______________　　日期：______________")
    lines.append("")
    lines.append("*免责声明：本报告由 pipl-check 工具辅助生成，仅供企业自查参考。*")
    return "\n".join(lines)


def gen_impact_pdf(results: list[dict], output_path: str, org_name: str = ""):
    """PDF版影响评估表 — 第二列合并、全部□选项、申明签字"""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor, white, grey
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    )
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    FONT = "Helvetica"
    for fp, fn in [
        ("/System/Library/Fonts/PingFang.ttc", "PingFang"),
        ("/System/Library/Fonts/STHeiti Light.ttc", "STHeiti"),
    ]:
        try:
            pdfmetrics.registerFont(TTFont(fn, fp))
            FONT = fn
            break
        except Exception:
            continue

    now = datetime.now().strftime("%Y年%m月%d日")
    doc = SimpleDocTemplate(output_path, pagesize=A4,
        leftMargin=12*mm, rightMargin=12*mm, topMargin=15*mm, bottomMargin=15*mm)

    s_title = ParagraphStyle("T", fontName=FONT, fontSize=17, alignment=TA_CENTER, spaceAfter=3*mm)
    s_info = ParagraphStyle("I", fontName=FONT, fontSize=11, alignment=TA_CENTER, textColor=grey, spaceAfter=4*mm)
    s_h = ParagraphStyle("H", fontName=FONT, fontSize=10, leading=14)
    s_c = ParagraphStyle("C", fontName=FONT, fontSize=9.5, leading=14)
    s_cb = ParagraphStyle("CB", fontName=FONT, fontSize=9.5, leading=13)
    s_decl = ParagraphStyle("D", fontName=FONT, fontSize=11.5, leading=18, spaceBefore=4*mm, alignment=TA_JUSTIFY)
    s_sig = ParagraphStyle("Sg", fontName=FONT, fontSize=11.5, leading=18, spaceBefore=2*mm)
    s_footer = ParagraphStyle("F", fontName=FONT, fontSize=10, textColor=grey, alignment=TA_CENTER, spaceBefore=3*mm)

    story = []
    story.append(Paragraph("小型个人信息处理者个人信息保护影响评估表", s_title))
    story.append(Paragraph(
        f"依据：《小型个人信息处理者个人信息保护简化措施规定》（国家互联网信息办公室、公安部令第25号）附件2", s_info))
    if org_name:
        story.append(Paragraph(f"企业/组织名称：{org_name}", s_info))
    story.append(Paragraph(f"编制时间：{now}", s_info))
    story.append(Spacer(1, 2*mm))

    # ── Table: 序号 | 影响评估情形 | 影响评估内容 | 影响评估结论 | 备注 ──
    hdr = [Paragraph("<b>序号</b>", s_h), Paragraph("<b>影响评估情形</b>", s_h),
           Paragraph("<b>影响评估内容</b>", s_h), Paragraph("<b>影响评估结论</b>", s_h),
           Paragraph("备注<br/>（其他需说明的情况及证明材料）", s_h)]
    tbl = [hdr]
    spans = []
    data_row = 1  # 0-indexed row in the table (0=header)

    for scenario in results:
        s_item = IMPACT_ITEMS[scenario["id"] - 1]
        answers = scenario.get("answers", [])
        note = scenario.get("note", "") or "—"
        num_rows = len(answers)
        start_row = data_row

        for idx, ans in enumerate(answers):
            criterion = s_item["criteria"][idx]

            # Build checkbox text for each choice
            cb_parts = []
            for opt in criterion["choices"]:
                cb_parts.append(f"{_cb(ans['answer'] == opt)} {opt}")
            status_txt = "  ".join(cb_parts)

            # Only first row of each scenario has number and name
            seq_txt = str(scenario["id"]) if idx == 0 else ""
            name_txt = s_item["name"] if idx == 0 else ""
            note_txt = note if idx == num_rows - 1 else ""

            tbl.append([
                Paragraph(seq_txt, s_c),
                Paragraph(name_txt, s_c),
                Paragraph(criterion["q"], s_c),
                Paragraph(status_txt, s_cb),
                Paragraph(note_txt, s_c)
            ])
            data_row += 1

        end_row = data_row - 1
        if num_rows > 1:
            # Merge column 0 (序号) and column 1 (影响评估情形) across rows of this scenario
            spans.append(('SPAN', (0, start_row), (0, end_row)))
            spans.append(('SPAN', (1, start_row), (1, end_row)))

    col_w = [8*mm, 38*mm, 46*mm, 40*mm, 34*mm]
    mt = Table(tbl, colWidths=col_w, repeatRows=1)
    cmds = [
        ('GRID', (0,0), (-1,-1), 0.2, HexColor("#bbb")),
        ('BACKGROUND', (0,0), (-1,0), HexColor("#d0d8e8")),
        ('FONTNAME', (0,0), (-1,-1), FONT),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('ALIGN', (0,0), (0,-1), 'CENTER'), ('ALIGN', (3,0), (3,-1), 'CENTER'),
    ]
    cmds.extend(spans)
    for i in range(2, len(tbl), 2):
        cmds.append(('BACKGROUND', (0,i), (-1,i), HexColor("#f5f7fa")))
    mt.setStyle(TableStyle(cmds))
    story.append(mt)

    # ── 申明 + 签字 ──
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        "本人已对上述事项进行了影响评估，并如实填写影响评估情况，"
        "如有不实，承担相应法律责任。", s_decl))
    story.append(Spacer(1, 3*mm))
    sig_tbl = Table([
        [Paragraph("影响评估负责人签字", s_sig), Paragraph("：", s_sig), Paragraph("__________________　　", s_sig)],
        [Paragraph("日　　　　期", s_sig), Paragraph("：", s_sig), Paragraph("__________________　　", s_sig)],
    ], colWidths=[48*mm, 5*mm, 67*mm])
    sig_tbl.setStyle(TableStyle([
        ('ALIGN', (0,0), (0,-1), 'RIGHT'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        ('ALIGN', (2,0), (2,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('FONTNAME', (0,0), (-1,-1), FONT),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
    ]))
    story.append(sig_tbl)

    story.append(Spacer(1, 5*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=grey))
    story.append(Paragraph(
        "免责声明：本报告由 pipl-check 工具辅助生成，仅供企业自查参考。", s_footer))
    doc.build(story)
    print(f"  ✅ PDF影响评估表: {output_path}")


# ═══════════════════════════════════════════════════════════════════
#  统一入口
# ═══════════════════════════════════════════════════════════════════

def generate_audit(results: list[dict], output_path: str, org_name: str = "",
                   fmt: str = "pdf"):
    md_path = output_path + ".md"
    pdf_path = output_path + ".pdf"
    md = gen_audit_markdown(results, org_name)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  ✅ Markdown自查表: {os.path.abspath(md_path)}")
    if fmt != "md":
        gen_audit_pdf(results, pdf_path, org_name)


def generate_impact(results: list[dict], output_path: str, org_name: str = "",
                    fmt: str = "pdf"):
    md_path = output_path + "-impact.md"
    pdf_path = output_path + "-impact.pdf"
    md = gen_impact_markdown(results, org_name)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"  ✅ Markdown影响评估: {os.path.abspath(md_path)}")
    if fmt != "md":
        gen_impact_pdf(results, pdf_path, org_name)
