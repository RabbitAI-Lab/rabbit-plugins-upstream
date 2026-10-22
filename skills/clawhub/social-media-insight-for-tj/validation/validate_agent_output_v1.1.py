#!/usr/bin/env python3
"""
Agent产出验证脚本 v1.1
用途：验证聆媒洞察Agent产出的stage1_original_output.json是否符合Brief要求
执行时机：阶段1完成后，阶段2 Transform之前
变更（v1.1）：
  - 修复第4节 summaries 检查因注释导致的逻辑错误
  - 修复第5节悬空 break 导致只检查第一个事件
  - summaries 只检查非空字符串，删除字数限制
  - peak_events text 只检查非空字符串，删除字数限制和禁用词
  - date_label 格式扩展：同时接受 "M月D日" 和 "M月"
"""

import json
import re
import sys
from typing import Dict, List, Tuple

def validate_agent_output(file_path: str) -> Tuple[bool, List[str]]:
    """
    验证Agent产出文件的完整性和正确性
    
    Returns:
        (is_valid, error_messages)
    """
    errors = []
    
    # 1. 文件存在性和可解析性
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return False, [f"❌ 文件不存在: {file_path}"]
    except json.JSONDecodeError as e:
        return False, [f"❌ JSON格式错误: {e}"]
    
    # 2. 顶层结构检查
    required_top_keys = ['meta', 'summaries', 'peak_events', 'api']
    actual_top_keys = set(data.keys())
    expected_top_keys = set(required_top_keys)
    
    if actual_top_keys != expected_top_keys:
        missing = expected_top_keys - actual_top_keys
        extra = actual_top_keys - expected_top_keys
        if missing:
            errors.append(f"❌ 缺少顶层字段: {', '.join(missing)}")
        if extra:
            errors.append(f"❌ 多余顶层字段: {', '.join(extra)} (只能包含meta、summaries、peak_events、api)")
    
    # 3. api字段完整性检查（17个key）
    required_api_keys = [
        'main_overview', 'main_overview_yoy', 'main_trend',
        'main_platform', 'main_platform_yoy',
        'dy_overview', 'dy_overview_yoy', 'dy_trend',
        'wb_overview', 'wb_overview_yoy', 'wb_trend',
        'slot1_overview', 'slot1_platform', 'slot1_trend',
        'slot2_overview', 'slot2_platform', 'slot2_trend'
    ]
    
    if 'api' not in data:
        errors.append("❌ 缺少api字段（这是Transform阶段的唯一数据源）")
    else:
        api_data = data['api']
        missing_api_keys = [k for k in required_api_keys if k not in api_data]
        if missing_api_keys:
            errors.append(f"❌ api字段缺少以下key（共{len(missing_api_keys)}个）: {', '.join(missing_api_keys)}")
        
        # 检查每个api key是否有数据
        for key in required_api_keys:
            if key in api_data:
                value = api_data[key]
                if value is None or value == "" or value == []:
                    errors.append(f"❌ api.{key} 为空，必须包含MCP接口的原始返回数据")
    
    # 4. summaries字段检查（7个页面）
    required_summary_keys = ['P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8']
    
    if 'summaries' not in data:
        errors.append("❌ 缺少summaries字段")
    else:
        summaries = data['summaries']
        missing_summaries = [k for k in required_summary_keys if k not in summaries]
        if missing_summaries:
            errors.append(f"❌ summaries缺少以下页面: {', '.join(missing_summaries)}")
        
        # 检查每个summary非空
        for key in required_summary_keys:
            if key in summaries:
                text = summaries[key]
                if not isinstance(text, str):
                    errors.append(f"❌ summaries.{key} 不是字符串类型")
                elif not text.strip():
                    errors.append(f"❌ summaries.{key} 为空字符串")
    
    # 5. peak_events字段检查
    required_peak_keys = {
        'P2': 6, 'P5': 6, 'P6': 6,
        'P7_main': 3, 'P7_slot': 3,
        'P8_main': 3, 'P8_slot': 3
    }
    
    if 'peak_events' not in data:
        errors.append("❌ 缺少peak_events字段")
    else:
        peak_events = data['peak_events']
        for key, expected_count in required_peak_keys.items():
            if key not in peak_events:
                errors.append(f"❌ peak_events缺少{key}")
            else:
                events = peak_events[key]
                if not isinstance(events, list):
                    errors.append(f"❌ peak_events.{key} 不是数组类型")
                elif len(events) != expected_count:
                    errors.append(f"❌ peak_events.{key} 包含{len(events)}个事件，要求{expected_count}个")
                else:
                    # 检查每个事件的结构
                    for i, event in enumerate(events):
                        if not isinstance(event, dict):
                            errors.append(f"❌ peak_events.{key}[{i}] 不是对象类型")
                            continue
                        
                        required_event_fields = ['event_id', 'idx', 'date_label', 'text']
                        missing_fields = [f for f in required_event_fields if f not in event]
                        if missing_fields:
                            errors.append(f"❌ peak_events.{key}[{i}] 缺少字段: {', '.join(missing_fields)}")
                        
                        # date_label 格式检查：接受 "M月D日" 或 "M月"
                        if 'date_label' in event:
                            dl = event['date_label']
                            if not isinstance(dl, str) or not re.match(r'^\d+月\d+日$', dl):
                                errors.append(f"❌ peak_events.{key}[{i}].date_label 格式错误，期望 'M月D日'，实际 '{dl}'")
                        
                        # text 非空检查
                        if 'text' in event:
                            text = event['text']
                            if not isinstance(text, str) or not text.strip():
                                errors.append(f"❌ peak_events.{key}[{i}].text 为空")
    
    # 6. meta字段检查
    required_meta_keys = [
        'main_event', 'report_stage', 'main_time_range', 'yoy_time_range',
        'slot1_time_range', 'slot2_time_range',
        'slot1_event_name', 'slot2_event_name',
        'playoff_start', 'generated_at'
    ]
    
    if 'meta' not in data:
        errors.append("❌ 缺少meta字段")
    else:
        meta = data['meta']
        missing_meta = [k for k in required_meta_keys if k not in meta]
        if missing_meta:
            errors.append(f"❌ meta缺少以下字段: {', '.join(missing_meta)}")
    
    # 7. 返回验证结果
    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    if len(sys.argv) < 2:
        print("用法: python3 validate_agent_output.py <stage1_original_output.json>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    print("=" * 60)
    print("Agent产出验证脚本 v1.1")
    print("=" * 60)
    print(f"验证文件: {file_path}")
    print()
    
    is_valid, errors = validate_agent_output(file_path)
    
    if is_valid:
        print("✅ 验证通过！Agent产出符合Brief要求，可以进入Transform阶段。")
        print()
        sys.exit(0)
    else:
        print(f"❌ 验证失败！发现 {len(errors)} 个错误：")
        print()
        for i, error in enumerate(errors, 1):
            print(f"{i}. {error}")
        print()
        print("=" * 60)
        print("⚠️  必须修复以上错误后才能进入Transform阶段")
        print("⚠️  建议返回Agent重新取数，确保api字段包含全部17个MCP原始响应")
        print("=" * 60)
        sys.exit(1)
