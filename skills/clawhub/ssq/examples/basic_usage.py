#!/usr/bin/env python3
"""
Drawing Parser 基础使用示例
"""

import sys
import os
from pathlib import Path

# 添加 scripts 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from cad_parser import parse_cad_drawing
from pdf_parser import parse_pdf_drawing


def example_cad_parsing():
    """示例：解析 CAD 图纸"""
    print("=" * 50)
    print("示例 1：解析 CAD 图纸")
    print("=" * 50)
    
    # 解析 DWG 文件（自动转换为 DXF）
    result = parse_cad_drawing(
        input_file='examples/test.dwg',
        output_dir='examples/output',
        mode='v4',  # ODA + ezdxf
        verbose=True
    )
    
    print(f"\n提取结果：")
    print(f"  - 文字数量：{len(result['texts'])}")
    print(f"  - 尺寸数量：{len(result['dimensions'])}")
    print(f"  - 图层数量：{len(result['layers'])}")
    
    # 显示前 5 条文字
    if result['texts']:
        print(f"\n前 5 条文字：")
        for i, text in enumerate(result['texts'][:5], 1):
            print(f"  {i}. [{text['layer']}] {text['content'][:30]}...")


def example_pdf_parsing():
    """示例：解析 PDF 图纸"""
    print("\n" + "=" * 50)
    print("示例 2：解析 PDF 图纸")
    print("=" * 50)
    
    # 解析 PDF 文件（自动降级 OCR 模式）
    result = parse_pdf_drawing(
        input_file='examples/test.pdf',
        output_dir='examples/output',
        ocr_mode='v6',  # PP-OCRv6（推荐）
        max_pages=5,
        verbose=True
    )
    
    print(f"\n提取结果：")
    print(f"  - 文字数量：{len(result['texts'])}")
    
    # 显示前 5 条文字
    if result['texts']:
        print(f"\n前 5 条文字：")
        for i, text in enumerate(result['texts'][:5], 1):
            print(f"  {i}. [{text.get('layer', 'unknown')}] {text['content'][:30]}...")


def example_batch_parsing():
    """示例：批量解析"""
    print("\n" + "=" * 50)
    print("示例 3：批量解析")
    print("=" * 50)
    
    import glob
    
    # 查找所有 DWG 文件
    dwg_files = glob.glob('examples/*.dwg')
    pdf_files = glob.glob('examples/*.pdf')
    
    all_results = []
    
    for dwg_file in dwg_files:
        print(f"\n处理 CAD: {dwg_file}")
        result = parse_cad_drawing(dwg_file, 'examples/output/batch')
        all_results.append(result)
    
    for pdf_file in pdf_files:
        print(f"\n处理 PDF: {pdf_file}")
        result = parse_pdf_drawing(pdf_file, 'examples/output/batch')
        all_results.append(result)
    
    print(f"\n✅ 批量处理完成，共 {len(all_results)} 个文件")


if __name__ == '__main__':
    # 运行示例
    example_cad_parsing()
    example_pdf_parsing()
    # example_batch_parsing()  # 取消注释以运行批量示例
