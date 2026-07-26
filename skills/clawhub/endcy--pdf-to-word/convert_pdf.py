#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pdf-to-word - 极速PDF转Word

用法:
    python convert_pdf.py <PDF文件路径> [输出Word路径]

说明:
    本工具用于将PDF文档转换为Word格式，保留原文档的段落布局、表格和样式。
    适用于企业环境中授权的文件转换场景，兼容加密文件。
    基于 PyMuPDF 和 pdf2docx 库实现高保真转换。
"""

import sys
import os


def check_dependencies():
    """检查并提示安装依赖"""
    try:
        from pdf2docx import Converter
        return True
    except ImportError:
        print("ERROR: 缺少依赖库", file=sys.stderr)
        print("请运行以下命令安装依赖:", file=sys.stderr)
        print("  pip install pdf2docx python-docx PyMuPDF", file=sys.stderr)
        return False


def convert_pdf_to_word(pdf_path, output_path=None):
    """
    将PDF转换为Word文档
    
    Args:
        pdf_path: PDF文件路径
        output_path: 输出Word文件路径（可选，默认输出到同目录，同名.docx）
    
    Returns:
        输出文件路径
    """
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF文件不存在：{pdf_path}")
    
    # 检查文件扩展名
    if not pdf_path.lower().endswith('.pdf'):
        raise ValueError(f"文件不是PDF格式：{pdf_path}")
    
    # 确定输出路径
    if output_path is None:
        base_name = os.path.splitext(pdf_path)[0]
        output_path = base_name + '.docx'
    
    # 确保输出目录存在
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 执行转换
    try:
        from pdf2docx import Converter
        
        print(f"[INFO] 开始转换: {os.path.basename(pdf_path)}")
        
        cv = Converter(pdf_path)
        cv.convert(output_path)
        cv.close()
        
        # 获取文件信息
        file_size = os.path.getsize(output_path)
        size_str = format_file_size(file_size)
        
        print(f"[INFO] 转换完成")
        print(f"[INFO] 输出文件: {output_path}")
        print(f"[INFO] 文件大小: {size_str}")
        
        return output_path
        
    except Exception as e:
        raise RuntimeError(f"转换失败: {str(e)}")


def format_file_size(size_bytes):
    """格式化文件大小"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"


def main():
    if len(sys.argv) < 2:
        print("用法：python convert_pdf.py <PDF文件路径> [输出Word路径]")
        print("示例：python convert_pdf.py E:\\data\\document.pdf")
        print("      python convert_pdf.py E:\\data\\document.pdf E:\\output\\document.docx")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = convert_pdf_to_word(pdf_path, output_path)
        print(result)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
