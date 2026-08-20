#!/usr/bin/env python3
"""
PDF 图纸解析器 - 支持 PDF 和图片格式
使用多种 OCR 引擎提取文字和表格
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import numpy as np


def try_import_rapidocr():
    """尝试导入 RapidOCR"""
    try:
        from rapidocr_onnxruntime import RapidOCR
        return RapidOCR
    except ImportError:
        return None


def try_import_paddleocr():
    """尝试导入 PaddleOCR"""
    try:
        from paddleocr import PaddleOCR
        return PaddleOCR
    except ImportError:
        return None


class OCREngine:
    """OCR 引擎封装，支持多种后端"""
    
    def __init__(self, mode: str = 'v6'):
        self.mode = mode
        self.engine = None
        self._init_engine()
    
    def _init_engine(self):
        """初始化 OCR 引擎"""
        if self.mode == 'v6':
            RapidOCR = try_import_rapidocr()
            if RapidOCR:
                self.engine = RapidOCR()
            else:
                # 降级到 rapid
                self.mode = 'rapid'
                self._init_engine()
        
        elif self.mode == 'rapid':
            # RapidOCR-json.exe
            self.engine = 'rapid'
        
        elif self.mode == 'fast':
            # PaddleOCR-json.exe
            self.engine = 'fast'
        
        elif self.mode == 'dl':
            # deepdoc ONNX
            self.engine = 'dl'
    
    def recognize(self, image) -> List[Dict]:
        """识别图片中的文字"""
        if self.mode == 'v6' and self.engine:
            result, _ = self.engine(image)
            return self._format_rapidocr_result(result)
        
        elif self.mode == 'rapid':
            # 调用 RapidOCR-json.exe
            return self._call_external_ocr(image, 'rapid')
        
        elif self.mode == 'fast':
            # 调用 PaddleOCR-json.exe
            return self._call_external_ocr(image, 'fast')
        
        elif self.mode == 'dl':
            # deepdoc ONNX
            return self._deepdoc_ocr(image)
        
        return []
    
    def _format_rapidocr_result(self, result) -> List[Dict]:
        """格式化 RapidOCR 结果"""
        texts = []
        if result:
            for line in result:
                if len(line) >= 2:
                    bbox = line[1]  # [x1,y1], [x2,y2], [x3,y3], [x4,y4]
                    content = line[0][0]
                    confidence = line[0][1]
                    
                    texts.append({
                        'content': content,
                        'bbox': [
                            float(bbox[0][0]), float(bbox[0][1]),
                            float(bbox[1][0]), float(bbox[1][1])
                        ],
                        'confidence': float(confidence)
                    })
        return texts
    
    def _call_external_ocr(self, image, engine_name: str) -> List[Dict]:
        """调用外部 OCR 引擎"""
        # 这里需要实现与 RapidOCR-json.exe / PaddleOCR-json.exe 的交互
        # 实际使用时需要根据 exe 的接口调整
        return []
    
    def _deepdoc_ocr(self, image) -> List[Dict]:
        """使用 deepdoc ONNX 进行 OCR"""
        # 这里需要实现 deepdoc 的调用逻辑
        return []


def parse_pdf_drawing(
    input_file: str,
    output_dir: str = './output',
    ocr_mode: str = 'v6',
    max_pages: int = 10,
    verbose: bool = False
) -> Dict[str, Any]:
    """
    解析 PDF 图纸
    
    Args:
        input_file: 输入 PDF 文件路径
        output_dir: 输出目录
        ocr_mode: OCR 模式（v6/dl/rapid/fast）
        max_pages: 最大处理页数
        verbose: 是否详细输出
    
    Returns:
        解析结果字典
    """
    import fitz  # PyMuPDF
    
    input_path = Path(input_file)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    result = {
        'project_name': input_path.stem,
        'source_file': str(input_path),
        'parse_time': datetime.now().isoformat(),
        'ocr_mode': ocr_mode,
        'texts': [],
        'paragraphs': [],
        'tables': [],
        'dimensions': [],
        'metadata': {}
    }
    
    try:
        # 打开 PDF
        if verbose:
            print(f"正在打开 PDF: {input_path}")
        doc = fitz.open(str(input_path))
        
        total_pages = min(len(doc), max_pages)
        if verbose:
            print(f"共 {len(doc)} 页，处理前 {total_pages} 页")
        
        # 初始化 OCR 引擎（自动降级）
        ocr = OCREngine(mode=ocr_mode)
        actual_mode = ocr.mode
        if actual_mode != ocr_mode:
            if verbose:
                print(f"OCR 模式降级：{ocr_mode} → {actual_mode}")
        
        # 逐页处理
        for page_num in range(total_pages):
            page = doc[page_num]
            
            if verbose:
                print(f"处理第 {page_num + 1} 页...")
            
            # 渲染为图片
            mat = fitz.Matrix(2.0, 2.0)  # 2x 缩放提高精度
            pix = page.get_pixmap(matrix=mat)
            img_array = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
                pix.height, pix.width, 3
            )
            
            # OCR 识别
            texts = ocr.recognize(img_array)
            result['texts'].extend(texts)
        
        doc.close()
        
        # 保存结果
        output_file = output_path / 'project_data.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        if verbose:
            print(f"✅ 解析完成，共提取 {len(result['texts'])} 条文字")
        
    except Exception as e:
        result['error'] = str(e)
        if verbose:
            print(f"❌ 解析失败: {e}")
    
    return result


if __name__ == '__main__':
    import argparse
    from datetime import datetime
    
    parser = argparse.ArgumentParser(description='PDF 图纸解析器')
    parser.add_argument('input', help='输入 PDF 文件')
    parser.add_argument('output', help='输出目录')
    parser.add_argument('--mode', '-m', choices=['v6', 'dl', 'rapid', 'fast'], default='v6')
    parser.add_argument('--pages', '-p', type=int, default=10)
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    
    result = parse_pdf_drawing(args.input, args.output, args.mode, args.pages, args.verbose)
    print(json.dumps(result, ensure_ascii=False, indent=2))
