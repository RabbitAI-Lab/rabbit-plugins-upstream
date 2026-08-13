#!/usr/bin/env python3
"""
PDF转EPUB转换器 - 主脚本
将扫描版PDF通过OCR识别转换为结构化的EPUB电子书
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple
import uuid

# 导入自定义模块
from ocr_processor import OCRProcessor
from text_cleaner import TextCleaner, ChapterInfo
from epub_generator import EPUBGenerator

class PDFToEPUBConverter:
    """PDF转EPUB转换器主类"""
    
    def __init__(self, pdf_path: str, output_dir: str = "output"):
        """
        初始化转换器
        
        Args:
            pdf_path: PDF文件路径
            output_dir: 输出目录
        """
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 生成工作目录
        self.work_dir = self.output_dir / f"work_{uuid.uuid4().hex[:8]}"
        self.work_dir.mkdir(exist_ok=True)
        
        # 初始化各模块
        self.ocr_processor = OCRProcessor()
        self.text_cleaner = TextCleaner()
        self.epub_generator = EPUBGenerator()
        
        # 设置日志
        self._setup_logging()
        
    def _setup_logging(self):
        """设置日志"""
        log_file = self.work_dir / "conversion.log"
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def extract_metadata(self) -> Dict[str, str]:
        """
        提取PDF元数据
        
        Returns:
            元数据字典
        """
        self.logger.info("开始提取PDF元数据...")
        try:
            from PyPDF2 import PdfReader
            
            with open(self.pdf_path, 'rb') as f:
                reader = PdfReader(f)
                metadata = reader.metadata
                
                if metadata:
                    return {
                        'title': metadata.get('/Title', ''),
                        'author': metadata.get('/Author', ''),
                        'creator': metadata.get('/Creator', ''),
                        'producer': metadata.get('/Producer', ''),
                        'subject': metadata.get('/Subject', ''),
                        'pages': len(reader.pages)
                    }
                else:
                    return {
                        'title': self.pdf_path.stem,
                        'author': 'Unknown',
                        'pages': len(reader.pages)
                    }
        except Exception as e:
            self.logger.error(f"提取元数据失败: {e}")
            return {
                'title': self.pdf_path.stem,
                'author': 'Unknown',
                'pages': 0
            }
    
    def extract_cover(self) -> Optional[str]:
        """
        提取PDF封面
        
        Returns:
            封面图片路径，如果提取失败返回None
        """
        self.logger.info("开始提取PDF封面...")
        try:
            from pdf2image import convert_from_path
            from PIL import Image
            
            # 只转换第一页
            images = convert_from_path(
                str(self.pdf_path),
                first_page=1,
                last_page=1,
                dpi=300,
                fmt='jpeg'
            )
            
            if images:
                cover_path = self.work_dir / "cover.jpg"
                images[0].save(cover_path, 'JPEG', quality=95)
                self.logger.info(f"封面提取成功: {cover_path}")
                return str(cover_path)
            else:
                self.logger.warning("无法提取封面")
                return None
                
        except Exception as e:
            self.logger.error(f"提取封面失败: {e}")
            return None
    
    def convert(self, metadata: Optional[Dict[str, str]] = None) -> Tuple[str, Dict]:
        """
        执行完整的转换流程
        
        Args:
            metadata: 可选的元数据，如果提供将覆盖PDF中的元数据
            
        Returns:
            (输出EPUB路径, 转换统计信息)
        """
        self.logger.info(f"开始转换PDF: {self.pdf_path}")
        
        # 提取基础元数据
        pdf_metadata = self.extract_metadata()
        self.logger.info(f"PDF元数据: {pdf_metadata}")
        
        # 合并元数据
        if metadata:
            final_metadata = {**pdf_metadata, **metadata}
        else:
            final_metadata = pdf_metadata
        
        # 提取封面
        cover_path = self.extract_cover()
        
        # OCR识别
        self.logger.info("开始OCR识别...")
        ocr_result = self.ocr_processor.process_pdf(
            str(self.pdf_path),
            self.work_dir / "images"
        )
        
        # 文本清洗和章节识别
        self.logger.info("开始文本清洗和章节识别...")
        chapters = self.text_cleaner.process_ocr_result(
            ocr_result,
            final_metadata
        )
        
        self.logger.info(f"识别到 {len(chapters)} 个章节")
        
        # 生成EPUB
        self.logger.info("开始生成EPUB...")
        epub_path = self.epub_generator.generate(
            title=final_metadata.get('title', 'Untitled'),
            author=final_metadata.get('author', 'Unknown'),
            chapters=chapters,
            cover_path=cover_path,
            output_path=self.output_dir / f"{self.pdf_path.stem}_converted.epub",
            metadata=final_metadata
        )
        
        # 生成统计信息
        stats = {
            'total_pages': ocr_result['total_pages'],
            'successful_pages': ocr_result['successful_pages'],
            'average_confidence': ocr_result['average_confidence'],
            'total_chapters': len(chapters),
            'output_file': str(epub_path),
            'file_size': os.path.getsize(epub_path) if os.path.exists(epub_path) else 0
        }
        
        self.logger.info(f"转换完成: {epub_path}")
        self.logger.info(f"统计信息: {stats}")
        
        return str(epub_path), stats

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='PDF转EPUB转换器')
    parser.add_argument('pdf_path', help='PDF文件路径')
    parser.add_argument('--output-dir', default='output', help='输出目录')
    parser.add_argument('--title', help='书名（覆盖PDF元数据）')
    parser.add_argument('--author', help='作者（覆盖PDF元数据）')
    
    args = parser.parse_args()
    
    # 构建元数据
    metadata = {}
    if args.title:
        metadata['title'] = args.title
    if args.author:
        metadata['author'] = args.author
    
    # 创建转换器并执行转换
    converter = PDFToEPUBConverter(args.pdf_path, args.output_dir)
    epub_path, stats = converter.convert(metadata)
    
    print(f"\n转换完成！")
    print(f"输出文件: {epub_path}")
    print(f"文件大小: {stats['file_size'] / 1024:.2f} KB")
    print(f"总页数: {stats['total_pages']}")
    print(f"识别成功页数: {stats['successful_pages']}")
    print(f"平均置信度: {stats['average_confidence']:.2%}")
    print(f"章节数: {stats['total_chapters']}")

if __name__ == '__main__':
    main()