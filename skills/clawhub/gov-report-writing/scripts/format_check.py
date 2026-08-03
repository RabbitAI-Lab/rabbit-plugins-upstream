#!/usr/bin/env python3
"""
gov-report-writing 格式自动检查脚本

检查生成的 DOCX 文件是否符合 GB/T 9704-2012 以及企业级公文格式规范。

用法:
    python format_check.py <docx文件路径>

输出:
    格式检查报告，标注所有不符合规范的问题
"""
import sys
import zipfile
import re
import os
import xml.etree.ElementTree as ET

# GB/T 9704-2012 + 企业标准 参数
EXPECTED_PARAMS = {
    # 页边距 (DXA单位, 1mm ≈ 56.7 DXA, 但Word用DXA=1440/inch, 1cm≈567 DXA)
    'margin_top_cm': 3.7,      # 上边距
    'margin_bottom_cm': 3.5,    # 下边距
    'margin_left_cm': 2.8,     # 左边距（订口）
    'margin_right_cm': 2.6,    # 右边距（翻口）

    # 标题
    'title_font': '方正小标宋简体',
    'title_size_pt': [20, 22],  # 党组20pt / 通用22pt，允许18pt(小二号)

    # 正文
    'body_font': '仿宋_GB2312',
    'body_size_pt': 16,  # 三号 = 16pt

    # 一级标题
    'h1_font': '黑体',

    # 二级标题
    'h2_font': '楷体_GB2312',

    # 行距
    'line_spacing_pt': 28,  # 固定值28磅

    # 首行缩进
    'indent_chars': 2,

    # 数字字体
    'number_font': 'Times New Roman',
}

# CM → DXA conversion (1cm = 567 DXA, approximate)
def cm_to_dxa(cm):
    return int(cm * 567)

def check_format(docx_path):
    """检查 DOCX 格式"""
    issues = []
    passed = []

    if not os.path.exists(docx_path):
        print(f"❌ 文件不存在: {docx_path}")
        return

    try:
        with zipfile.ZipFile(docx_path) as z:
            # 读取 document.xml
            doc_xml = z.read('word/document.xml').decode('utf-8')
    except Exception as e:
        print(f"❌ 无法打开文件: {e}")
        return

    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    root = ET.fromstring(doc_xml)

    # 1. 检查页边距
    margins = root.findall('.//w:sectPr/w:pgMar', ns)
    if margins:
        mg = margins[0]
        for attr, expected_cm in [
            ('top', EXPECTED_PARAMS['margin_top_cm']),
            ('bottom', EXPECTED_PARAMS['margin_bottom_cm']),
            ('left', EXPECTED_PARAMS['margin_left_cm']),
            ('right', EXPECTED_PARAMS['margin_right_cm']),
        ]:
            val = int(mg.get(f'{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{attr}', 0))
            expected_dxa = cm_to_dxa(expected_cm)
            if val == 0:
                issues.append(f"⚠️ 未设置页边距: {attr}")
            elif abs(val - expected_dxa) > 100:  # 允许约2mm误差
                issues.append(f"❌ 页边距 {attr}: 当前 {val} DXA ({val/567:.1f}cm), 应为 {expected_cm}cm ({expected_dxa} DXA)")
            else:
                passed.append(f"✅ 页边距 {attr}: {expected_cm}cm ✓")

    # 2. 检查字体
    fonts_elements = root.findall('.//w:rFonts', ns)
    document_text = ''.join(t.text or '' for t in root.findall('.//w:t', ns))

    # Check title font (first heading)
    title_para = root.find('.//w:p/w:pPr/w:pStyle[@w:val="Title"]/..', ns)
    if title_para is not None:
        title_font_elem = title_para.find('.//w:rFonts', ns)
        if title_font_elem is not None:
            asc = title_font_elem.get(f'{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}eastAsia', '')
            if EXPECTED_PARAMS['title_font'] not in asc:
                issues.append(f"❌ 标题字体: {asc}, 应为 {EXPECTED_PARAMS['title_font']} 或其变体")
            else:
                passed.append(f"✅ 标题字体: {asc} ✓")

    # 3. 检查正文缩进
    indent_elements = root.findall('.//w:pPr/w:ind', ns)
    correct_indent = 0
    wrong_indent = 0
    for indent in indent_elements:
        first_line = int(indent.get(f'{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}firstLine', 0))
        if first_line > 0:
            # 2 chars ≈ 480 DXA (at 12pt) or 640 DXA (at 16pt)
            if 400 <= first_line <= 700:
                correct_indent += 1
            else:
                wrong_indent += 1
    if correct_indent > 0:
        passed.append(f"✅ 首行缩进: {correct_indent} 段正确 ✓")
    if wrong_indent > 0:
        issues.append(f"❌ 首行缩进: {wrong_indent} 段缩进值异常")

    # 4. 检查行距
    spacing_elements = root.findall('.//w:pPr/w:spacing', ns)
    line_issues = 0
    for spacing in spacing_elements:
        line = int(spacing.get(f'{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}line', 0))
        line_rule = spacing.get(f'{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}lineRule', '')
        # 固定值 28pt = 28 * 20 = 560 twips
        expected_line = 560  # 28pt in twips
        if line_rule == 'exact' and abs(line - expected_line) > 20:
            line_issues += 1
    if line_issues == 0 and spacing_elements:
        passed.append("✅ 行距: 固定值28磅 ✓")
    elif line_issues > 0:
        issues.append(f"❌ 行距: {line_issues} 段行距偏离28磅")

    # 5. 检查层级序号
    cn_numbering = re.findall(r'[一二三四五六七八九十]+、', document_text)
    if cn_numbering:
        wrong = [x for x in cn_numbering if re.match(r'[一二三四五六七八九十]+\.$', x.replace('、','.'))]
        if wrong:
            issues.append(f"❌ 一级标题序号: 发现用点号代替顿号 ({wrong[:3]})")
        else:
            passed.append(f"✅ 一级标题序号: "一、" 格式正确 ✓")

    # 6. 检查年份括号
    if re.search(r'\[\d{4}\]', document_text):
        issues.append("❌ 年份括号: 发现使用方括号[]，应使用六角括号〔〕")
    elif re.search(r'〔\d{4}〕', document_text):
        passed.append("✅ 年份括号: 〔〕六角括号正确 ✓")

    # 7. 检查数字字体（简化检查）
    if 'Times New Roman' not in doc_xml and len(re.findall(r'\d{2,}', document_text)) > 5:
        issues.append("⚠️ 数字字体: 未设置 Times New Roman（建议设置）")

    # 8. 页码检查（简化）
    footer_text = ''
    try:
        with zipfile.ZipFile(docx_path) as z:
            footer_files = [f for f in z.namelist() if 'footer' in f.lower() and f.endswith('.xml')]
            for ff in footer_files[:1]:
                footer_text = z.read(ff).decode('utf-8')
    except:
        pass
    if footer_text and ('page' in footer_text.lower() or '页码' in footer_text):
        passed.append("✅ 页码: 已设置 ✓")
    elif not footer_text:
        passed.append("ℹ️ 未检测到页脚（可能使用默认页码）")

    # ======== 输出报告 ========
    print(f"\n{'='*60}")
    print(f"  公文格式检查报告: {os.path.basename(docx_path)}")
    print(f"{'='*60}\n")

    print(f"## 通过项 ({len(passed)})")
    for p in passed:
        print(f"  {p}")

    print(f"\n## 问题项 ({len(issues)})")
    if issues:
        for i in issues:
            print(f"  {i}")
    else:
        print("  🎉 未发现格式问题！")

    print(f"\n{'='*60}")
    total = len(passed) + len(issues)
    if total > 0:
        score = len(passed) / total * 100
        print(f"  格式规范度: {score:.0f}% ({len(passed)}/{total})")
    print(f"{'='*60}\n")

    return len(issues) == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python format_check.py <docx文件路径>")
        sys.exit(1)

    ok = check_format(sys.argv[1])
    sys.exit(0 if ok else 1)
