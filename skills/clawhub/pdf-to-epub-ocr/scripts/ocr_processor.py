#!/usr/bin/env python3
"""
OCR处理模块
负责将PDF页面转换为图片并进行OCR文字识别
"""

import os
import logging
from pathlib import Path
from typing import Dict, List, Any
import concurrent.futures
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

class OCRProcessor:
    """OCR处理器"""
    
    def __init__(self, dpi: int = 300, language: str = 'chi_sim+eng'):
        """
        初始化OCR处理器
        
        Args:
            dpi: 转换图片的DPI
            language: OCR识别语言配置
        """
        self.dpi = dpi
        self.language = language
        self.logger = logging.getLogger(__name__)
        
        # 检查Tesseract是否可用
        self._check_tesseract()
        
    def _check_tesseract(self):
        """检查Tesseract OCR是否安装"""
        try:
            pytesseract.get_tesseract_version()
            self.logger.info("Tesseract OCR检查通过")
        except EnvironmentError:
            self.logger.error("Tesseract OCR未安装或不在PATH中")
            raise RuntimeError("请先安装Tesseract OCR")
    
    def pdf_to_images(self, pdf_path: str, output_dir: Path) -> List[Path]:
        """
        将PDF转换为图片
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 输出目录
            
        Returns:
            图片文件路径列表
        """
        self.logger.info(f"开始转换PDF为图片: {pdf_path}")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            # 转换PDF为图片
            images = convert_from_path(
                pdf_path,
                dpi=self.dpi,
                fmt='png',
                thread_count=4
            )
            
            image_paths = []
            for i, image in enumerate(images, 1):
                image_path = output_dir / f"page_{i:04d}.png"
                image.save(image_path, 'PNG')
                image_paths.append(image_path)
                
                if i % 10 == 0:
                    self.logger.info(f"已转换 {i}/{len(images)} 页")
            
            self.logger.info(f"PDF转换完成，共 {len(image_paths)} 页")
            return image_paths
            
        except Exception as e:
            self.logger.error(f"PDF转换失败: {e}")
            raise
    
    def ocr_image(self, image_path: Path) -> Dict[str, Any]:
        """
        对单个图片进行OCR识别
        
        Args:
            image_path: 图片文件路径
            
        Returns:
            OCR结果字典，包含文本和置信度
        """
        try:
            # 打开图片
            image = Image.open(image_path)
            
            # 执行OCR识别
            ocr_result = pytesseract.image_to_data(
                image,
                lang=self.language,
                config='--psm 6',
                output_type=pytesseract.Output.DICT
            )
            
            # 提取文本和置信度
            text_lines = []
            confidences = []
            
            for i, text in enumerate(ocr_result['text']):
                if text.strip():  # 跳过空行
                    conf = int(ocr_result['conf'][i])
                    if conf > 0:  # 只保留有置信度的文本
                        text_lines.append(text.strip())
                        confidences.append(conf)
            
            # 计算平均置信度
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0
            
            full_text = '\n'.join(text_lines)
            
            return {
                'page_number': int(image_path.stem.split('_')[1]),
                'text': full_text,
                'line_count': len(text_lines),
                'confidences': confidences,
                'average_confidence': avg_confidence,
                'success': len(text_lines) > 0
            }
            
        except Exception as e:
            self.logger.error(f"OCR识别失败 {image_path}: {e}")
            return {
                'page_number': int(image_path.stem.split('_')[1]),
                'text': '',
                'line_count': 0,
                'confidences': [],
                'average_confidence': 0,
                'success': False,
                'error': str(e)
            }
    
    def process_pdf(self, pdf_path: str, output_dir: Path) -> Dict[str, Any]:
        """
        处理整个PDF文件
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 工作目录
            
        Returns:
            处理结果统计
        """
        self.logger.info(f"开始处理PDF: {pdf_path}")
        
        # 转换PDF为图片
        image_dir = output_dir / "pages"
        image_paths = self.pdf_to_images(pdf_path, image_dir)
        
        # 并行OCR识别
        ocr_results = []
        total_pages = len(image_paths)
        successful_pages = 0
        all_confidences = []
        
        # 使用线程池并行处理
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_page = {
                executor.submit(self.ocr_image, img_path): img_path 
                for img_path in image_paths
            }
            
            for future in concurrent.futures.as_completed(future_to_page):
                result = future.result()
                ocr_results.append(result)
                
                if result['success']:
                    successful_pages += 1
                    all_confidences.extend(result['confidences'])
                
                # 输出进度
                completed = len(ocr_results)
                if completed % 5 == 0 or completed == total_pages:
                    self.logger.info(f"OCR进度: {completed}/{total_pages} 页")
        
        # 按页码排序
        ocr_results.sort(key=lambda x: x['page_number'])
        
        # 计算总体统计
        average_confidence = (
            sum(all_confidences) / len(all_confidences) 
            if all_confidences else 0
        )
        
        result = {
            'total_pages': total_pages,
            'successful_pages': successful_pages,
            'failed_pages': total_pages - successful_pages,
            'average_confidence': average_confidence,
            'pages': ocr_results,
            'full_text': '\n\n'.join([
                page['text'] for page in ocr_results if page['text']
            ])
        }
        
        self.logger.info(
            f"OCR处理完成: 成功 {successful_pages}/{total_pages} 页, "
            f"平均置信度 {average_confidence:.2%}"
        )
        
        return result