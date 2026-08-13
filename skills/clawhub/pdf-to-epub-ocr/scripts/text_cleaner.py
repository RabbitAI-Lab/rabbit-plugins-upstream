#!/usr/bin/env python3
"""
文本清洗和章节识别模块
负责OCR文本的后处理，包括清洗和章节识别
"""

import re
import logging
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import Counter

@dataclass
class ChapterInfo:
    """章节信息"""
    id: str
    title: str
    level: int
    content: str
    start_page: int
    end_page: int

class TextCleaner:
    """文本清洗器"""
    
    def __init__(self):
        """初始化文本清洗器"""
        self.logger = logging.getLogger(__name__)
        
        # 章节标题正则表达式模式
        self.chapter_patterns = [
            # 中文章节
            (r'^第[一二三四五六七八九十百千]+章[^\n]*$', 1),
            (r'^第[0-9]+章[^\n]*$', 1),
            (r'^第[一二三四五六七八九十百千]+节[^\n]*$', 2),
            (r'^第[0-9]+节[^\n]*$', 2),
            # 英文章节
            (r'^Chapter\s+[0-9IVXLCDM]+[^\n]*$', 1, re.IGNORECASE),
            (r'^Part\s+[0-9IVXLCDM]+[^\n]*$', 1, re.IGNORECASE),
            (r'^Section\s+[0-9]+[^\n]*$', 2, re.IGNORECASE),
            # 数字编号
            (r'^[0-9]+\.[0-9]+[^\n]*$', 2),  # 1.1, 2.3等
            (r'^[0-9]+\.[0-9]+\.[0-9]+[^\n]*$', 3),  # 1.1.1等
        ]
        
        # 页眉页脚和噪音模式
        self.noise_patterns = [
            # 页码
            r'-\s*\d+\s*-',
            r'第\s*\d+\s*页',
            r'Page\s*\d+',
            r'^\d+$',
            # 水印
            r'^[机密|内部|Confidential|Internal]',
            # 常见页眉
            r'^.*出版.*$',
            r'^.*出版社.*$',
            r'^.*版权所有.*$',
        ]
    
    def clean_page_text(self, text: str) -> str:
        """
        清洗单页文本
        
        Args:
            text: 原始文本
            
        Returns:
            清洗后的文本
        """
        if not text:
            return ""
        
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检查是否为噪音行
            is_noise = False
            for pattern in self.noise_patterns:
                if re.match(pattern, line, re.IGNORECASE):
                    is_noise = True
                    break
            
            if not is_noise:
                cleaned_lines.append(line)
        
        # 规范化空白
        cleaned_text = '\n'.join(cleaned_lines)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # 多个空格转为一个
        cleaned_text = re.sub(r'\n\s*\n', '\n\n', cleaned_text)  # 多个空行转为两个
        
        return cleaned_text.strip()
    
    def detect_chapter_titles(self, text: str) -> List[Tuple[int, str, int]]:
        """
        检测章节标题
        
        Args:
            text: 完整文本
            
        Returns:
            章节标题列表，格式为[(行号, 标题, 级别), ...]
        """
        lines = text.split('\n')
        chapters = []
        
        for line_num, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            # 尝试匹配各种章节模式
            for pattern in self.chapter_patterns:
                if len(pattern) == 2:
                    regex, level = pattern
                    flags = 0
                else:
                    regex, level, flags = pattern
                
                match = re.match(regex, line, flags)
                if match:
                    chapters.append((line_num, line, level))
                    break  # 找到匹配就跳出
        
        return chapters
    
    def segment_chapters(
        self, 
        ocr_result: Dict, 
        metadata: Dict
    ) -> List[ChapterInfo]:
        """
        根据OCR结果和章节标题分割文本
        
        Args:
            ocr_result: OCR处理结果
            metadata: 文档元数据
            
        Returns:
            章节信息列表
        """
        # 构建完整文本
        full_text = ocr_result['full_text']
        
        # 检测章节标题
        chapter_titles = self.detect_chapter_titles(full_text)
        
        if not chapter_titles:
            # 没有检测到章节，创建单个章节
            self.logger.warning("未检测到章节标题，创建单个章节")
            return [ChapterInfo(
                id='chapter_001',
                title=metadata.get('title', '正文'),
                level=1,
                content=full_text,
                start_page=1,
                end_page=ocr_result['total_pages']
            )]
        
        # 分割章节
        chapters = []
        lines = full_text.split('\n')
        
        for i, (line_num, title, level) in enumerate(chapter_titles):
            # 确定章节内容范围
            start_line = line_num
            end_line = chapter_titles[i + 1][0] if i + 1 < len(chapter_titles) else len(lines)
            
            # 提取章节内容
            content_lines = lines[start_line + 1:end_line]  # 跳过标题行
            content = '\n'.join(content_lines).strip()
            
            # 确定页码范围
            start_page = self._line_to_page(line_num, ocr_result['pages']) + 1
            end_page = self._line_to_page(end_line, ocr_result['pages']) + 1
            
            # 创建章节
            chapter_id = f"chapter_{i + 1:03d}"
            chapter = ChapterInfo(
                id=chapter_id,
                title=title,
                level=level,
                content=content,
                start_page=start_page,
                end_page=end_page
            )
            chapters.append(chapter)
        
        self.logger.info(f"识别到 {len(chapters)} 个章节")
        return chapters
    
    def _line_to_page(self, line_num: int, pages: List[Dict]) -> int:
        """
        将行号转换为页码
        
        Args:
            line_num: 行号
            pages: 页面信息列表
            
        Returns:
            页码（从0开始）
        """
        total_lines = sum(page.get('line_count', 0) for page in pages)
        lines_per_page = total_lines / len(pages) if pages else 0
        
        if lines_per_page > 0:
            return min(int(line_num / lines_per_page), len(pages) - 1)
        return 0
    
    def process_ocr_result(
        self, 
        ocr_result: Dict, 
        metadata: Dict
    ) -> List[ChapterInfo]:
        """
        处理OCR结果，返回结构化的章节信息
        
        Args:
            ocr_result: OCR处理结果
            metadata: 文档元数据
            
        Returns:
            章节信息列表
        """
        self.logger.info("开始处理OCR结果...")
        
        # 清洗每页文本
        for page in ocr_result['pages']:
            page['cleaned_text'] = self.clean_page_text(page['text'])
        
        # 重建完整文本
        ocr_result['full_text'] = '\n\n'.join([
            page['cleaned_text'] 
            for page in ocr_result['pages'] 
            if page['cleaned_text']
        ])
        
        # 分割章节
        chapters = self.segment_chapters(ocr_result, metadata)
        
        # 清洗章节内容
        for chapter in chapters:
            chapter.content = self.clean_page_text(chapter.content)
        
        return chapters
    
    def analyze_text_quality(self, text: str) -> Dict[str, float]:
        """
        分析文本质量
        
        Args:
            text: 文本内容
            
        Returns:
            质量指标字典
        """
        if not text:
            return {
                'avg_line_length': 0,
                'empty_line_ratio': 1.0,
                'special_char_ratio': 0
            }
        
        lines = text.split('\n')
        line_lengths = [len(line) for line in lines]
        
        # 计算各种指标
        avg_line_length = sum(line_lengths) / len(line_lengths) if line_lengths else 0
        empty_lines = sum(1 for line in lines if not line.strip())
        empty_line_ratio = empty_lines / len(lines) if lines else 0
        
        special_chars = sum(1 for char in text if not char.isalnum() and not char.isspace())
        special_char_ratio = special_chars / len(text) if text else 0
        
        return {
            'avg_line_length': avg_line_length,
            'empty_line_ratio': empty_line_ratio,
            'special_char_ratio': special_char_ratio
        }