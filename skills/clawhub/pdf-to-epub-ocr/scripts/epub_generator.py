#!/usr/bin/env python3
"""
EPUB生成模块
负责创建结构化的EPUB电子书文件
"""

import os
import logging
import uuid
from pathlib import Path
from typing import List, Dict, Optional
from ebooklib import epub

class EPUBGenerator:
    """EPUB生成器"""
    
    def __init__(self):
        """初始化EPUB生成器"""
        self.logger = logging.getLogger(__name__)
        
    def create_epub(
        self,
        title: str,
        author: str,
        chapters: List,
        cover_path: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> epub.EpubBook:
        """
        创建EPUB书籍对象
        
        Args:
            title: 书名
            author: 作者
            chapters: 章节列表
            cover_path: 封面图片路径
            metadata: 额外的元数据
            
        Returns:
            EPUB书籍对象
        """
        self.logger.info(f"开始创建EPUB: {title}")
        
        # 创建EPUB书籍
        book = epub.EpubBook()
        
        # 设置基本元数据
        book.set_identifier(str(uuid.uuid4()))
        book.set_title(title)
        book.set_language('zh-CN')
        book.add_author(author)
        
        # 添加额外的元数据
        if metadata:
            if 'creator' in metadata:
                book.add_metadata('DC', 'creator', metadata['creator'])
            if 'publisher' in metadata:
                book.add_metadata('DC', 'publisher', metadata['publisher'])
            if 'subject' in metadata:
                book.add_metadata('DC', 'subject', metadata['subject'])
            if 'description' in metadata:
                book.add_metadata('DC', 'description', metadata['description'])
        
        # 添加封面
        if cover_path and os.path.exists(cover_path):
            self._add_cover(book, cover_path)
        
        # 添加CSS样式
        css_content = self._get_default_css()
        nav_css = epub.EpubItem(
            uid="style_nav",
            file_name="style/nav.css",
            media_type="text/css",
            content=css_content
        )
        book.add_item(nav_css)
        
        # 创建章节
        epub_chapters = []
        toc_entries = []
        
        for i, chapter in enumerate(chapters):
            epub_chapter = self._create_chapter(chapter, nav_css)
            book.add_item(epub_chapter)
            epub_chapters.append(epub_chapter)
            
            # 添加到目录
            toc_entries.append(epub_chapter)
        
        # 设置目录
        book.toc = toc_entries
        
        # 添加导航文件
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        
        # 设置spine（阅读顺序）
        book.spine = ['nav'] + epub_chapters
        
        return book
    
    def _add_cover(self, book: epub.EpubBook, cover_path: str):
        """
        添加封面图片
        
        Args:
            book: EPUB书籍对象
            cover_path: 封面图片路径
        """
        try:
            with open(cover_path, 'rb') as f:
                cover_data = f.read()
            
            cover_filename = 'cover.jpg'
            cover_item = epub.EpubItem(
                uid="cover",
                file_name=cover_filename,
                media_type="image/jpeg",
                content=cover_data
            )
            book.add_item(cover_item)
            
            # 设置封面
            book.set_cover(cover_filename, cover_data)
            
            self.logger.info("封面添加成功")
            
        except Exception as e:
            self.logger.error(f"添加封面失败: {e}")
    
    def _create_chapter(self, chapter, css_item: epub.EpubItem) -> epub.EpubHtml:
        """
        创建单个章节
        
        Args:
            chapter: 章节信息
            css_item: CSS样式项
            
        Returns:
            EPUB HTML章节对象
        """
        # 创建HTML内容
        html_content = f"""
        <?xml version="1.0" encoding="utf-8"?>
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
          "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
        
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
          <title>{chapter.title}</title>
          <link rel="stylesheet" type="text/css" href="style/nav.css"/>
        </head>
        <body>
          <h1>{chapter.title}</h1>
          <div class="content">
            {self._format_content(chapter.content)}
          </div>
        </body>
        </html>
        """
        
        # 创建章节
        epub_chapter = epub.EpubHtml(
            title=chapter.title,
            file_name=f'{chapter.id}.xhtml',
            content=html_content
        )
        epub_chapter.add_item(css_item)
        
        return epub_chapter
    
    def _format_content(self, content: str) -> str:
        """
        格式化章节内容
        
        Args:
            content: 原始内容
            
        Returns:
            格式化后的HTML内容
        """
        if not content:
            return "<p>（无内容）</p>"
        
        # 分段处理
        paragraphs = content.split('\n\n')
        html_paragraphs = []
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            # 转义HTML特殊字符
            para = para.replace('&', '&amp;')
            para = para.replace('<', '&lt;')
            para = para.replace('>', '&gt;')
            
            # 检测是否为标题
            if len(para) < 50 and not para.endswith('。'):
                html_paragraphs.append(f"<h3>{para}</h3>")
            else:
                html_paragraphs.append(f"<p>{para}</p>")
        
        return '\n'.join(html_paragraphs)
    
    def _get_default_css(self) -> str:
        """
        获取默认CSS样式
        
        Returns:
            CSS样式字符串
        """
        return """
        body {
            font-family: "PingFang SC", "Microsoft YaHei", "SimHei", serif;
            line-height: 1.8;
            margin: 1em;
            padding: 0;
        }
        
        h1 {
            text-align: center;
            margin: 1em 0;
            font-size: 1.8em;
            color: #333;
            border-bottom: 2px solid #eee;
            padding-bottom: 0.5em;
        }
        
        h2 {
            margin: 1.5em 0 0.8em 0;
            font-size: 1.4em;
            color: #444;
        }
        
        h3 {
            margin: 1.2em 0 0.6em 0;
            font-size: 1.2em;
            color: #555;
        }
        
        p {
            margin: 0.8em 0;
            text-align: justify;
            text-indent: 2em;
            font-size: 1em;
            color: #333;
        }
        
        .content {
            max-width: 100%;
            margin: 0 auto;
        }
        
        @media screen and (max-width: 600px) {
            body {
                font-size: 16px;
                margin: 0.5em;
            }
            
            h1 {
                font-size: 1.5em;
            }
            
            h2 {
                font-size: 1.3em;
            }
            
            p {
                text-indent: 1.5em;
            }
        }
        """
    
    def generate(
        self,
        title: str,
        author: str,
        chapters: List,
        cover_path: Optional[str] = None,
        output_path: Optional[Path] = None,
        metadata: Optional[Dict] = None
    ) -> Path:
        """
        生成EPUB文件
        
        Args:
            title: 书名
            author: 作者
            chapters: 章节列表
            cover_path: 封面图片路径
            output_path: 输出文件路径
            metadata: 额外的元数据
            
        Returns:
            输出文件路径
        """
        # 创建EPUB书籍
        book = self.create_epub(title, author, chapters, cover_path, metadata)
        
        # 确定输出路径
        if output_path is None:
            output_path = Path(f"{title}.epub")
        else:
            output_path = Path(output_path)
        
        # 确保输出目录存在
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 写入EPUB文件
        try:
            epub.write_epub(str(output_path), book, {})
            self.logger.info(f"EPUB文件生成成功: {output_path}")
            return output_path
        except Exception as e:
            self.logger.error(f"EPUB文件生成失败: {e}")
            raise
    
    def validate_epub(self, epub_path: Path) -> bool:
        """
        验证EPUB文件的有效性
        
        Args:
            epub_path: EPUB文件路径
            
        Returns:
            是否有效
        """
        try:
            # 尝试读取EPUB文件
            book = epub.read_epub(str(epub_path))
            
            # 检查基本结构
            if not book.get_metadata('DC', 'title'):
                self.logger.warning("EPUB缺少标题元数据")
                return False
            
            if not book.spine:
                self.logger.warning("EPUB缺少spine")
                return False
            
            # 检查是否有内容
            items = list(book.get_items())
            content_items = [item for item in items if item.get_type() == 9]  # XHTML类型
            
            if not content_items:
                self.logger.warning("EPUB没有内容项")
                return False
            
            self.logger.info("EPUB验证通过")
            return True
            
        except Exception as e:
            self.logger.error(f"EPUB验证失败: {e}")
            return False