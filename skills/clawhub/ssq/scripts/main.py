#!/usr/bin/env python3
"""
Drawing Parser - 建筑图纸解析引擎主入口
支持 DWG/DXF/PDF/图片格式的图纸解析
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# 添加脚本目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def detect_format(file_path: str) -> str:
    """自动检测文件格式"""
    ext = Path(file_path).suffix.lower()
    format_map = {
        '.dwg': 'cad',
        '.dxf': 'cad',
        '.pdf': 'pdf',
        '.png': 'pdf',
        '.jpg': 'pdf',
        '.jpeg': 'pdf',
        '.bmp': 'pdf',
        '.tiff': 'pdf',
        '.tif': 'pdf'
    }
    return format_map.get(ext, 'unknown')


def parse_args():
    parser = argparse.ArgumentParser(
        description='建筑图纸解析引擎 - 支持DWG/DXF/PDF/图片',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python main.py drawing.dwg ./output --mode v4
  python main.py drawing.pdf ./output --mode v6
  python main.py drawing.png ./output --mode rapid
        """
    )
    parser.add_argument('input', help='输入图纸文件路径')
    parser.add_argument('output', help='输出目录路径')
    parser.add_argument('--mode', '-m', choices=['v4', 'v3', 'v6', 'dl', 'rapid', 'fast'],
                       default=None, help='解析模式（根据文件格式自动选择）')
    parser.add_argument('--pages', '-p', type=int, default=10,
                       help='最大处理页数（PDF/图片）')
    parser.add_argument('--config', '-c', default=None,
                       help='配置文件路径（JSON格式）')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='详细输出')
    return parser.parse_args()


def load_config(config_path: str) -> dict:
    """加载配置文件"""
    default_config = {
        "ODA_PATH": None,
        "ACCONSOLE_PATH": None,
        "OCR_MODE": "v6",
        "MAX_PAGES": 10,
        "OUTPUT_DIR": "./output"
    }
    
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            user_config = json.load(f)
            default_config.update(user_config)
    
    return default_config


def main():
    args = parse_args()
    
    # 检查输入文件
    if not os.path.exists(args.input):
        print(f"错误：输入文件不存在: {args.input}")
        sys.exit(1)
    
    # 检测格式
    file_format = detect_format(args.input)
    if file_format == 'unknown':
        print(f"错误：不支持的文件格式: {Path(args.input).suffix}")
        print("支持的格式：DWG, DXF, PDF, PNG, JPG, JPEG, BMP, TIFF")
        sys.exit(1)
    
    print(f"检测到文件格式：{file_format.upper()}")
    
    # 创建输出目录
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 加载配置
    config = load_config(args.config)
    
    # 根据格式调度解析器
    if file_format == 'cad':
        print("使用 CAD 解析管线...")
        try:
            from cad_parser import parse_cad_drawing
            result = parse_cad_drawing(
                args.input,
                output_dir=str(output_dir),
                mode=args.mode or 'v4',
                verbose=args.verbose
            )
        except ImportError as e:
            print(f"错误：CAD 解析器未安装: {e}")
            print("请确保已安装 ezdxf 和 ODA File Converter")
            sys.exit(1)
    else:
        print("使用 PDF/OCR 解析管线...")
        try:
            from pdf_parser import parse_pdf_drawing
            result = parse_pdf_drawing(
                args.input,
                output_dir=str(output_dir),
                ocr_mode=args.mode or config.get('OCR_MODE', 'v6'),
                max_pages=args.pages,
                verbose=args.verbose
            )
        except ImportError as e:
            print(f"错误：PDF 解析器未安装: {e}")
            print("请确保已安装 pymupdf 和 OCR 依赖")
            sys.exit(1)
    
    # 保存结果
    output_file = output_dir / 'project_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 解析完成！")
    print(f"📄 输出文件：{output_file}")
    print(f"📊 提取文字：{len(result.get('texts', []))} 条")
    print(f"📋 提取表格：{len(result.get('tables', []))} 个")
    print(f"📐 提取尺寸：{len(result.get('dimensions', []))} 条")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
