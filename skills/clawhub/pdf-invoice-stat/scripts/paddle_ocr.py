"""
PaddleOCR 适配器 - 为 pdf-invoice-stat 提供 OCR 能力
v2.2.0 新增：火车票 OCR + 纯图片发票 OCR

依赖：
  - paddleocr>=3.0
  - paddlepaddle>=3.0

模型自动下载到 ~/.paddlex/official_models/ (~180MB)
"""
import os
import re
import sys
from typing import List, Dict, Optional, Union
from pathlib import Path

# 单例模式（避免重复初始化）
_OCR_ENGINE = None

def get_ocr_engine(lang='ch'):
    """获取 PaddleOCR 引擎（单例，首次加载 ~30 秒）"""
    global _OCR_ENGINE
    if _OCR_ENGINE is None:
        from paddleocr import PaddleOCR
        _OCR_ENGINE = PaddleOCR(lang=lang, use_doc_orientation_classify=False, use_doc_unwarping=False)
    return _OCR_ENGINE


def ocr_image(image_path: Union[str, Path]) -> List[Dict]:
    """
    OCR 图片，返回结构化结果。
    
    Args:
        image_path: 图片路径（jpg/png/PDF）
    
    Returns:
        [
          {
            'text': str,           # 识别的文字
            'bbox': [(x1,y1), (x2,y2), (x3,y3), (x4,y4)],  # 文本框坐标
            'score': float,        # 置信度 0-1
          },
          ...
        ]
    """
    image_path = str(image_path)
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"图片不存在: {image_path}")
    
    ocr = get_ocr_engine()
    result = ocr.predict(image_path)
    
    items = []
    for page_result in result:
        # paddleocr 3.x 返回 Result 对象
        if hasattr(page_result, 'json'):
            res = page_result.json
            rec_data = res.get('res', {})
            texts = rec_data.get('rec_texts', [])
            scores = rec_data.get('rec_scores', [])
            bboxes = rec_data.get('rec_boxes', [])
            for i, text in enumerate(texts):
                item = {
                    'text': text,
                    'score': scores[i] if i < len(scores) else 0.0,
                    'bbox': bboxes[i] if i < len(bboxes) else None,
                }
                items.append(item)
    return items


def ocr_pdf_page(pdf_path: Union[str, Path], page_num: int = 0, dpi: int = 200) -> List[Dict]:
    """
    OCR PDF 指定页面（先把 PDF 转图片，再 OCR）
    
    Args:
        pdf_path: PDF 路径
        page_num: 页码（0-indexed）
        dpi: 渲染 DPI（默认 200）
    
    Returns:
        同 ocr_image()
    """
    import pymupdf
    pdf_path = str(pdf_path)
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF 不存在: {pdf_path}")
    
    doc = pymupdf.open(pdf_path)
    if page_num >= len(doc):
        doc.close()
        raise ValueError(f"页码超出范围: {page_num} >= {len(doc)}")
    
    page = doc[page_num]
    # DPI 转 matrix scale
    scale = dpi / 72.0
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale))
    
    # 写到临时文件
    tmp_path = f"/tmp/paddle_ocr_page_{os.getpid()}.jpg"
    pix.save(tmp_path)
    doc.close()
    
    try:
        result = ocr_image(tmp_path)
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
    
    return result


def is_image_only_pdf(pdf_path: Union[str, Path]) -> bool:
    """
    检测 PDF 是否为纯图片（文本层缺失）
    
    Returns:
        True if 图片 PDF（需要 OCR）
        False if 文本 PDF（pdfplumber 即可）
    """
    try:
        import pdfplumber
        with pdfplumber.open(str(pdf_path)) as pdf:
            for page in pdf.pages[:3]:  # 只看前 3 页
                text = page.extract_text() or ""
                if len(text.strip()) > 50:
                    return False
        return True
    except Exception:
        return True  # 默认按图片处理


def extract_train_ticket_fields(ocr_items: List[Dict]) -> Dict:
    """
    从 OCR 结果中抽取火车票字段
    
    Args:
        ocr_items: ocr_image() 返回的列表
    
    Returns:
        {
            '发票号码': str,
            '开票日期': str,
            '车次': str,           # G600/D1234
            '起点': str,
            '终点': str,
            '票价': float,
            '身份证': str,
            '姓名': str,
            '购方': str,
            '购方税号': str,
            '电子客票号': str,
            '席别': str,           # 二等座/一等座
            '车厢座位': str,       # 08车09C号
        }
    """
    # 合并所有文本
    full_text = '\n'.join(item['text'] for item in ocr_items)
    
    result = {
        '发票号码': '',
        '开票日期': '',
        '车次': '',
        '起点': '',
        '终点': '',
        '票价': 0.0,
        '身份证': '',
        '姓名': '',
        '购方': '',
        '购方税号': '',
        '电子客票号': '',
        '席别': '',
        '车厢座位': '',
    }
    
    # 发票号码（20位数字）
    m = re.search(r'发票号码[::]\s*(\d{20})', full_text)
    if m: result['发票号码'] = m.group(1)
    
    # 开票日期
    m = re.search(r'开票日期[::]\s*(\d{4}年\d{2}月\d{2}日)', full_text)
    if m: result['开票日期'] = m.group(1)
    
    # 车次（G/D/C 后数字）
    m = re.search(r'\b([GDC]\d{1,4})\b', full_text)
    if m: result['车次'] = m.group(1)
    
    # 票价
    m = re.search(r'票价[::]\s*[￥¥]\s*(\d+\.\d{2})', full_text)
    if m: result['票价'] = float(m.group(1))
    
    # 身份证（18位或15位+星号）
    m = re.search(r'(\d{6,})\*{2,}(\d{4,})', full_text)
    if m: result['身份证'] = m.group(0)
    
    # 电子客票号
    m = re.search(r'电子客票号[::]\s*(\d{20,})', full_text)
    if m: result['电子客票号'] = m.group(1)
    
    # 购方税号（9131... 18位）
    m = re.search(r'统一社会信用代码[::]\s*([A-Z0-9]{18,20})', full_text)
    if m: result['购方税号'] = m.group(1)
    
    # 购方名称
    m = re.search(r'购买方名称[::]\s*([^统一\n]+?)(?=\s*统一|$)', full_text, re.MULTILINE)
    if m: result['购方'] = m.group(1).strip()
    
    # 姓名（身份证号附近）
    m = re.search(r'\*{4}\d{4}\s+(\S{2,4})', full_text)
    if m: result['姓名'] = m.group(1)
    
    # 席别（二等座/一等座/商务座等）
    m = re.search(r'(二等座|一等座|商务座|特等座|硬座|软座|硬卧|软卧)', full_text)
    if m: result['席别'] = m.group(1)
    
    # 车厢座位
    m = re.search(r'(\d{2}车\d{2}[A-F]号|\d{2}车\d{2}号)', full_text)
    if m: result['车厢座位'] = m.group(1)
    
    # 起点 + 终点（车次前后两个站名）
    train_match = re.search(r'([\u4e00-\u9fa5]{2,5}站)\s+' + re.escape(result['车次']) + r'\s+([\u4e00-\u9fa5]{2,5}站)', full_text)
    if train_match:
        result['起点'] = train_match.group(1)
        result['终点'] = train_match.group(2)
    
    return result


def is_train_ticket_ocr(ocr_items: List[Dict]) -> bool:
    """判断 OCR 结果是否火车票"""
    full_text = '\n'.join(item['text'] for item in ocr_items)
    return bool(re.search(r'电子客票|中国铁路|国铁|12306', full_text))


def is_vat_invoice_ocr(ocr_items: List[Dict]) -> bool:
    """判断 OCR 结果是否增值税发票"""
    full_text = '\n'.join(item['text'] for item in ocr_items)
    return bool(re.search(r'增值税|电子普通发票|发票代码|价税合计', full_text))


# === 火车票专用抽取函数 ===

def extract_train_ticket(image_path: str) -> dict:
    """
    火车票图片专用抽取
    
    Args:
        image_path: 火车票图片路径（jpg/png）或 PDF 单页路径
    
    Returns:
        {
            'is_train_ticket': bool,
            'fields': {...},        # 抽取的字段
            'confidence': float,    # 平均置信度
            'raw_text': str,        # OCR 原始文本
        }
    """
    # PDF 还是图片？
    if image_path.lower().endswith('.pdf'):
        # 默认 OCR 第 0 页
        items = ocr_pdf_page(image_path, page_num=0)
    else:
        items = ocr_image(image_path)
    
    is_train = is_train_ticket_ocr(items)
    fields = extract_train_ticket_fields(items) if is_train else {}
    
    avg_score = sum(item['score'] for item in items) / len(items) if items else 0
    
    return {
        'is_train_ticket': is_train,
        'fields': fields,
        'confidence': avg_score,
        'raw_text': '\n'.join(item['text'] for item in items),
    }


# === 公开 API ===

def ocr_invoice_or_image(file_path: str) -> Dict:
    """
    统一入口：根据文件类型自动选择 pdfplumber 或 PaddleOCR
    
    Args:
        file_path: PDF 或图片路径
    
    Returns:
        {
            'method': 'pdfplumber' | 'paddleocr',
            'is_train_ticket': bool,
            'is_vat_invoice': bool,
            'fields': {...},
            'raw_text': str,
        }
    """
    if file_path.lower().endswith('.pdf'):
        # 先判断是否纯图片 PDF
        if is_image_only_pdf(file_path):
            items = ocr_pdf_page(file_path, page_num=0)
            method = 'paddleocr'
        else:
            # 文本层完整，用 pdfplumber
            import pdfplumber
            with pdfplumber.open(file_path) as pdf:
                raw_text = pdf.pages[0].extract_text() or ""
            return {
                'method': 'pdfplumber',
                'is_train_ticket': bool(re.search(r'电子客票|中国铁路|国铁|12306', raw_text)),
                'is_vat_invoice': bool(re.search(r'增值税|电子普通发票', raw_text)),
                'raw_text': raw_text,
            }
    else:
        items = ocr_image(file_path)
        method = 'paddleocr'
    
    is_train = is_train_ticket_ocr(items)
    is_vat = is_vat_invoice_ocr(items)
    
    fields = extract_train_ticket_fields(items) if is_train else {}
    
    return {
        'method': method,
        'is_train_ticket': is_train,
        'is_vat_invoice': is_vat,
        'fields': fields,
        'raw_text': '\n'.join(item['text'] for item in items),
    }
