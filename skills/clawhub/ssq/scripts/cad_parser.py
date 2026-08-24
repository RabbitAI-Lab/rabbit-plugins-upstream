#!/usr/bin/env python3
"""
CAD 图纸解析器 - 支持 DWG/DXF 格式
使用 ezdxf 库解析 DXF 文件
"""

import os
import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import ezdxf


def extract_texts_from_dxf(mspace, min_length: int = 1) -> List[Dict]:
    """从 DXF 模型空间提取所有文字对象"""
    texts = []
    
    for text in mspace.query('TEXT, MTEXT'):
        try:
            content = text.dxf.text.strip()
            if len(content) >= min_length:
                # 获取边界框
                bbox = text.bounding_box()
                texts.append({
                    'content': content,
                    'bbox': [
                        float(bbox[0][0]), float(bbox[0][1]),
                        float(bbox[1][0]), float(bbox[1][1])
                    ],
                    'layer': text.dxf.layer,
                    'height': float(text.dxf.height) if hasattr(text.dxf, 'height') else 0,
                    'type': 'MTEXT' if text.dxftype() == 'MTEXT' else 'TEXT'
                })
        except Exception as e:
            continue
    
    return texts


def extract_dimensions_from_dxf(mspace) -> List[Dict]:
    """从 DXF 提取尺寸标注"""
    dimensions = []
    
    for dim in mspace.query('DIMENSION'):
        try:
            # 获取标注值
            measured_value = dim.measured_distance if hasattr(dim, 'measured_distance') else None
            if measured_value is None:
                measured_value = dim.dxf.measureddistance if hasattr(dim.dxf, 'measureddistance') else None
            
            if measured_value:
                dimensions.append({
                    'value': float(measured_value),
                    'unit': 'mm',  # 默认为毫米
                    'type': dim.dxftype(),
                    'layer': dim.dxf.layer
                })
        except Exception as e:
            continue
    
    return dimensions


def extract_layers(dxf_doc) -> List[str]:
    """提取所有图层名称"""
    return list(dxf_doc.layers.keys())


def parse_cad_drawing(
    input_file: str,
    output_dir: str = './output',
    mode: str = 'v4',
    verbose: bool = False
) -> Dict[str, Any]:
    """
    解析 CAD 图纸
    
    Args:
        input_file: 输入文件路径（DWG 或 DXF）
        output_dir: 输出目录
        mode: 解析模式（v4=ODA+ezdxf, v3=accoreconsole+LISP）
        verbose: 是否详细输出
    
    Returns:
        解析结果字典
    """
    input_path = Path(input_file)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    result = {
        'project_name': input_path.stem,
        'source_file': str(input_path),
        'parse_time': datetime.now().isoformat(),
        'mode': mode,
        'texts': [],
        'paragraphs': [],
        'tables': [],
        'dimensions': [],
        'layers': [],
        'metadata': {}
    }
    
    # 如果是 DWG，先转换为 DXF
    dxf_file = input_path
    if input_path.suffix.lower() == '.dwg':
        if mode == 'v4':
            # 使用 ODA 转换
            dxf_file = output_path / f"{input_path.stem}.dxf"
            if not dxf_file.exists():
                if verbose:
                    print(f"正在使用 ODA 转换 DWG → DXF: {dxf_file}")
                # 这里需要调用 ODA File Converter
                # 实际使用时需要配置 ODA_PATH
                pass
        else:
            # v3 模式使用 accoreconsole
            pass
    
    # 解析 DXF
    try:
        if verbose:
            print(f"正在解析 DXF 文件: {dxf_file}")
        
        doc = ezdxf.readfile(str(dxf_file))
        msp = doc.modelspace()
        
        # 提取文字
        if verbose:
            print("提取文字...")
        result['texts'] = extract_texts_from_dxf(msp)
        
        # 提取尺寸
        if verbose:
            print("提取尺寸标注...")
        result['dimensions'] = extract_dimensions_from_dxf(msp)
        
        # 提取图层
        if verbose:
            print("提取图层列表...")
        result['layers'] = extract_layers(doc)
        
        # 保存详细结果
        detail_file = output_path / f"{input_path.stem}_detail.json"
        with open(detail_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        if verbose:
            print(f"✅ 解析完成，共提取 {len(result['texts'])} 条文字，{len(result['dimensions'])} 条尺寸")
        
    except Exception as e:
        result['error'] = str(e)
        if verbose:
            print(f"❌ 解析失败: {e}")
    
    return result


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='CAD 图纸解析器')
    parser.add_argument('input', help='输入 DWG/DXF 文件')
    parser.add_argument('output', help='输出目录')
    parser.add_argument('--mode', '-m', choices=['v4', 'v3'], default='v4')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    
    result = parse_cad_drawing(args.input, args.output, args.mode, args.verbose)
    print(json.dumps(result, ensure_ascii=False, indent=2))
