"""
PP-StructureV3 适配器 - 为 pdf-invoice-stat 提供文档结构分析
v2.3.0 新增：版面分析 + 表格识别 + 关键信息抽取

依赖：
  - paddleocr>=3.0（含 PPStructureV3）
  - paddlepaddle>=3.0
  - paddlex[ocr]

模型自动下载到 ~/.paddlex/official_models/ (~470MB)
"""
import os
import re
from typing import List, Dict, Union
from pathlib import Path


# 单例模式
_PP_STRUCTURE_ENGINE = None


def get_pp_structure_engine():
    """获取 PP-StructureV3 引擎（单例，首次加载 ~80 秒）"""
    global _PP_STRUCTURE_ENGINE
    if _PP_STRUCTURE_ENGINE is None:
        from paddleocr import PPStructureV3
        _PP_STRUCTURE_ENGINE = PPStructureV3(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            use_table_recognition=True,    # ✅ 启用表格识别
            use_formula_recognition=False,
            use_chart_recognition=False,
            use_region_detection=False,
            use_seal_recognition=False,
        )
    return _PP_STRUCTURE_ENGINE


def parse_html_table(html: str) -> List[List[str]]:
    """
    解析 HTML 表格为二维列表
    
    Args:
        html: HTML 表格字符串
    
    Returns:
        二维列表 [[row1cell1, row1cell2], [row2cell1, row2cell2]]
    """
    from html.parser import HTMLParser
    
    class TableParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.in_table = False
            self.in_td = False
            self.current_cell = []
            self.current_row = []
            self.rows = []
        
        def handle_starttag(self, tag, attrs):
            if tag == 'table':
                self.in_table = True
            elif tag == 'tr':
                self.current_row = []
            elif tag in ('td', 'th'):
                self.in_td = True
                self.current_cell = []
        
        def handle_endtag(self, tag):
            if tag in ('td', 'th'):
                cell_text = ' '.join(self.current_cell).strip()
                self.current_row.append(cell_text)
                self.in_td = False
            elif tag == 'tr':
                if self.current_row:
                    self.rows.append(self.current_row)
            elif tag == 'table':
                self.in_table = False
        
        def handle_data(self, data):
            if self.in_td:
                self.current_cell.append(data)
    
    parser = TableParser()
    parser.feed(html)
    return parser.rows


def extract_table_rows(table_block) -> List[List[str]]:
    """从 LayoutBlock 中提取表格行"""
    if not hasattr(table_block, 'content') or not table_block.content:
        return []
    return parse_html_table(table_block.content)


def analyze_invoice(image_path: Union[str, Path]) -> Dict:
    """
    用 PP-StructureV3 分析发票（图片或 PDF）
    
    Args:
        image_path: 图片或 PDF 路径
    
    Returns:
        {
            'blocks': [block1, block2, ...],   # 所有 layout blocks
            'tables': [[row1], [row2], ...],   # 表格数据
            'texts': ['line1', 'line2', ...],   # 文本行
            'raw': 原结果,
        }
    """
    image_path = str(image_path)
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"文件不存在: {image_path}")
    
    # PDF 转图片
    if image_path.lower().endswith('.pdf'):
        from paddle_ocr import ocr_pdf_page
        ocr_items = ocr_pdf_page(image_path, page_num=0)
        # 用普通 OCR 引擎（PP-Structure 主要处理复杂版面）
        text_lines = [item['text'] for item in ocr_items]
        return {
            'blocks': [],
            'tables': [],
            'texts': text_lines,
            'raw': None,
        }
    
    # 图片用 PP-StructureV3
    engine = get_pp_structure_engine()
    result = list(engine.predict(image_path))
    
    page = result[0]
    # page.json 返回 dict, res 里包含 parsing_res_list
    page_data = page.json if hasattr(page, 'json') else {}
    res = page_data.get('res', {}) if isinstance(page_data, dict) else {}
    blocks = res.get('parsing_res_list', [])
    
    # 分类 blocks
    tables = []
    texts = []
    
    for block in blocks:
        label = block.get('block_label', '') or ''
        block_content = block.get('block_content', '') or ''
        
        if label == 'table':
            # 表格是 HTML
            if isinstance(block_content, str):
                rows = parse_html_table(block_content)
                if rows:
                    tables.append(rows)
        elif label in ('text', 'title', 'paragraph', 'figure_title', 'vision_footnote'):
            if block_content:
                texts.append(str(block_content).strip())
        elif label == 'image':
            # 跳过纯图片
            pass
        else:
            # 其他类型（如 seal, reference），尝试提取文本
            if isinstance(block_content, str) and block_content:
                texts.append(block_content.strip())
    
    return {
        'blocks': blocks,
        'tables': tables,
        'texts': texts,
        'raw': result,
    }


def parse_vat_invoice_from_tables(tables: List[List[str]], texts: List[str] = None) -> Dict:
    """
    从 PP-Structure 表格中解析增值税发票字段
    
    Args:
        tables: PP-Structure 提取的表格列表
    
    Returns:
        {
            '发票号码': '',
            '开票日期': '',
            '购买方信息-名称': '',
            '购买方信息-统一社会信用代码': '',
            '销售方信息-名称': '',
            '销售方信息-统一社会信用代码': '',
            '项目名称': [],
            '金额': float,
            '税率/征收率': '',
            '税额': float,
            '价税合计': float,
        }
    """
    result = {
        '发票号码': '',
        '开票日期': '',
        '购买方信息-名称': '',
        '购买方信息-统一社会信用代码': '',
        '销售方信息-名称': '',
        '销售方信息-统一社会信用代码': '',
        '项目名称': [],
        '金额': 0.0,
        '税率/征收率': '',
        '税额': 0.0,
        '价税合计': 0.0,
    }
    
    # 合并所有文本源（tables + texts）
    text_parts = []
    if texts:
        text_parts.extend(texts)
    for table in tables:
        for row in table:
            text_parts.append(' '.join(row))
    full_text = '\n'.join(text_parts)
    
    # 发票号码（20 位数字）
    m = re.search(r'发票号码[：:]\s*(\d{20})', full_text)
    if m: result['发票号码'] = m.group(1)
    
    # 开票日期
    m = re.search(r'开票日期[：:]\s*(\d{4}[-年]\d{1,2}[-月]\d{1,2})', full_text)
    if m: result['开票日期'] = m.group(1).replace('年', '-').replace('月', '-').replace('日', '')
    
    # 购方名称（在"购买方信息"后面第一个"名称："到下一个"销售方"之间的内容）
    m = re.search(r'购买方信息\s*名称[：:]\s*([^\s销售]+(?:\s[^\s销售]+)*?)\s*(?=销售方|统一社会信用代码|$)', full_text)
    if m: result['购买方信息-名称'] = m.group(1).strip()
    
    # 销方名称（在"销售方信息"后面第一个"名称："到下一个"统一社会信用代码"之间的内容）
    m = re.search(r'销售方信息\s*名称[：:]\s*([^\s统一]+(?:\s[^\s统一]+)*?)\s*(?=统一社会信用代码|$)', full_text)
    if m: result['销售方信息-名称'] = m.group(1).strip()
    
    # 税号（购买方在购买方信息之后，销售方在销售方信息之后）
    m = re.search(r'购买方信息[\s\S]*?统一社会信用代码[：:]\s*([A-Z0-9]{18,20})', full_text)
    if m: result['购买方信息-统一社会信用代码'] = m.group(1)
    m = re.search(r'销售方信息[\s\S]*?统一社会信用代码[：:]\s*([A-Z0-9]{18,20})', full_text)
    if m: result['销售方信息-统一社会信用代码'] = m.group(1)
    
    # 税号
    codes = re.findall(r'(?:统一社会信用代码|纳税人识别号)[：:]\s*([A-Z0-9]{18,20})', full_text)
    if codes:
        result['购买方信息-统一社会信用代码'] = codes[0]
        if len(codes) >= 2:
            result['销售方信息-统一社会信用代码'] = codes[1]
    
    # 表格行：项目/金额/税率/税额
    # 增值税发票表头通常是：
    # 项目名称 | 规格型号 | 单位 | 数量 | 单价 | 金额 | 税率/征收率 | 税额
    for table in tables:
        if len(table) < 5:  # 太短的表跳过
            continue
        # 检查第一行是否含"项目名称"或"金额"
        first_row = ' '.join(table[0]) if table else ''
        if '项目名称' not in first_row and '金额' not in first_row:
            continue
        
        # 找列索引
        col_map = {}
        for i, cell in enumerate(table[0]):
            cell = cell.strip()
            if '项目' in cell or '名称' in cell:
                col_map['item'] = i
            elif '金额' in cell and '税' not in cell:
                col_map['amount'] = i
            elif '税率' in cell or '征收率' in cell:
                col_map['rate'] = i
            elif '税额' in cell:
                col_map['tax'] = i
        
        # 处理每一行（数据行从第 2 行开始，跳过"合计"行）
        for row in table[1:]:
            if len(row) <= max(col_map.values(), default=0):
                continue
            
            item = row[col_map['item']].strip() if 'item' in col_map else ''
            # 跳过合计/价税合计行
            if any(k in item for k in ['合计', '价税', '小计']):
                # 合计行：提取金额/税额
                if 'item' in col_map and '合计' in item:
                    continue
                continue
            
            try:
                amount = float(row[col_map['amount']].replace(',', '')) if 'amount' in col_map else 0
                tax = float(row[col_map['tax']].replace(',', '')) if 'tax' in col_map else 0
            except (ValueError, IndexError):
                continue
            
            if item:
                result['项目名称'].append(item)
            result['金额'] += amount
            result['税额'] += tax
        
        # 税率：多税率留空，单税率取第一行
        rates = []
        for row in table[1:]:
            if 'rate' in col_map and len(row) > col_map['rate']:
                r = row[col_map['rate']].strip()
                if r and r not in ('合计', ''):
                    rates.append(r)
        if rates:
            result['税率/征收率'] = rates[0] if len(set(rates)) == 1 else ''
    
    # 价税合计：从表格里找（最后一行通常是"价税合计（大写）"）
    m = re.search(r'价税合计[^\d]*[¥￥]\s*(\d+\.\d{2})', full_text)
    if m: 
        result['价税合计'] = float(m.group(1))
    else:
        # 用 amount + tax 估算
        result['价税合计'] = round(result['金额'] + result['税额'], 2)
    
    return result


def extract_vat_invoice_pp_structure(image_path: str) -> Dict:
    """
    PP-StructureV3 路径：图片发票主入口
    
    Args:
        image_path: 发票图片路径（jpg/png/PDF）
    
    Returns:
        增值税发票字段 dict
    """
    analysis = analyze_invoice(image_path)
    return parse_vat_invoice_from_tables(analysis['tables'], analysis.get('texts', []))
