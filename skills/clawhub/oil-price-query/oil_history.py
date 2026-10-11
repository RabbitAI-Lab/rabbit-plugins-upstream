#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国油价查询 - 历史油价解析模块
用法：python3 oil_history.py <临时文件路径> <省份编码> <起始日期> [结束日期]
"""

import json
import sys
import re

# 历史油价 API 返回的燃油名称（Unicode 字符串）
HISTORY_FUEL_NAMES = {
    '88#汽油': '88#汽油',
    '89#汽油': '89#汽油',
    '91#汽油': '91#汽油',
    '92#汽油': '92#汽油',
    '94#汽油': '94#汽油',
    '95#汽油': '95#汽油',
    '1#柴油': '1#柴油',
    '0#柴油': '0#柴油'
}

# 标准燃油名称映射
STANDARD_FUEL_NAMES = {
    '89#汽油': '89 号汽油',
    '92#汽油': '92 号汽油',
    '95#汽油': '95 号汽油',
    '98#汽油': '98 号汽油',
    '0#柴油': '0 号柴油'
}

def map_fuel_name(fuel_name):
    """将历史油价 API 返回的燃油名称映射为标准名称"""
    # 使用字典查找，避免 elif 链的逻辑问题
    if fuel_name in HISTORY_FUEL_NAMES:
        return STANDARD_FUEL_NAMES.get(HISTORY_FUEL_NAMES[fuel_name], fuel_name)
    
    return None

def normalize_date(date_str):
    """标准化日期格式，支持多种格式"""
    if not date_str:
        return None
    
    # 尝试解析日期字符串
    # 支持格式：2026-05-08, 2026/5/8, 2026/05/08, 2026/5/08
    date_patterns = [
        (r'^(\d{4})-(\d{2})-(\d{2})$', 'iso'),
        (r'^(\d{4})/(\d{1,2})/(\d{1,2})$', 'slash')
    ]
    
    for pattern, fmt in date_patterns:
        match = re.match(pattern, date_str)
        if match:
            year, month, day = match.groups()
            if fmt == 'iso':
                return f"{year}-{month}-{day}"
            else:
                month = month.zfill(2)
                day = day.zfill(2)
                return f"{year}-{month}-{day}"
    
    return None

def main():
    if len(sys.argv) != 5:
        print("用法：python3 oil_history.py <临时文件路径> <省份编码> <起始日期> [结束日期]", file=sys.stderr)
        sys.exit(1)
    
    tmpfile = sys.argv[1]
    province_code = sys.argv[2]
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    
    try:
        with open(tmpfile, 'r', encoding='utf-8') as f:
            raw_response = f.read()
        
        # 解析 JSON 数据（不需要 html.unescape）
        data = json.loads(raw_response)
        
        # 标准化日期
        start_date_norm = normalize_date(start_date)
        end_date_norm = normalize_date(end_date)
        
        if not start_date_norm or not end_date_norm:
            print(f"❌ 日期格式错误，请确保日期格式为 YYYY-MM-DD", file=sys.stderr)
            sys.exit(1)
        
        # 历史油价 API 返回的是列表，直接是城市数据
        # 第一个元素是目标城市
        if not data or len(data) == 0:
            print("❌ 无法获取历史油价数据", file=sys.stderr)
            sys.exit(1)
        
        city_data = data[0]
        city_name = city_data.get('city', '未知')
        city_adcode = city_data.get('adcode', '')
        province_name = city_data.get('province_name', '')
        
        # 检查是否匹配用户查询的省份
        if city_adcode != province_code and province_code:
            print(f"⚠️  API 返回城市 ({city_name}, adcode: {city_adcode}) 与查询的省份 ({province_code}) 不匹配", file=sys.stderr)
            print(f"提示：历史油价 API 可能只返回固定城市的数据，不支持按省份查询历史油价。", file=sys.stderr)
        
        # 获取当前油价数据
        data_records = city_data.get('data', [])
        
        # 过滤日期范围内的数据
        filtered_records = [
            record for record in data_records
            if start_date_norm <= record.get('date', '') <= end_date_norm
        ]
        
        if not filtered_records:
            # 如果找不到指定日期范围的数据，显示最早和最晚的数据
            if data_records:
                sorted_by_date = sorted(data_records, key=lambda x: x.get('date', ''))
                start_date_norm = sorted_by_date[0].get('date', '')
                end_date_norm = sorted_by_date[-1].get('date', '')
                filtered_records = data_records
                print(f"\n⚠️  未找到 {start_date} 至 {end_date} 期间的数据，显示完整历史数据", file=sys.stderr)
            else:
                print(f"❌ 未找到历史油价数据", file=sys.stderr)
                sys.exit(1)
        
        # 输出历史数据
        print(f"\n============================================================")
        print(f"  油价历史查询结果 ({start_date_norm} - {end_date_norm})")
        print("============================================================")
        print("")
        print("┌─────────────────────────────────────────────────┐")
        print(f"│  {city_name:18} 历史油价                     │")
        print("├─────────────────────────────────────────────────┤")
        
        # 提取各燃油类型的历史价格
        gasoline_89_history = []
        gasoline_92_history = []
        gasoline_95_history = []
        gasoline_98_history = []
        diesel_0_history = []
        
        for record in filtered_records:
            # 从 data 数组中获取燃油数据
            data_array = record.get('data', [])
            if not data_array:
                continue
                
            for item in data_array:
                fuel_name = item.get('name', '')
                price = item.get('price', '')  # 不需要 html.unescape
                record_date = record.get('date', '')
                
                fuel_type = map_fuel_name(fuel_name)
                
                if fuel_type:
                    if price:
                        history_data = {
                            'date': record_date,
                            'price': price,
                            'fuel_type': fuel_type,
                            'updown': item.get('updown', '')
                        }
                        if fuel_type == '89 号汽油':
                            gasoline_89_history.append(history_data)
                        elif fuel_type == '92 号汽油':
                            gasoline_92_history.append(history_data)
                        elif fuel_type == '95 号汽油':
                            gasoline_95_history.append(history_data)
                        elif fuel_type == '98 号汽油':
                            gasoline_98_history.append(history_data)
                        elif fuel_type == '0 号柴油':
                            diesel_0_history.append(history_data)
        
        # 输出历史数据
        fuel_histories = [
            (gasoline_89_history, '89 号汽油', '⛽'),
            (gasoline_92_history, '92 号汽油', '⛽'),
            (gasoline_95_history, '95 号汽油', '⛽+'),
            (gasoline_98_history, '98 号汽油', '⛽++'),
            (diesel_0_history, '0 号柴油', '⛽')
        ]
        
        for history_list, fuel_name, prefix in fuel_histories:
            if history_list:
                print(f"│  {prefix} {fuel_name:11} 价格变化：")
                
                # 按日期排序
                sorted_history = sorted(history_list, key=lambda x: x['date'])
                
                # 只显示最近的变化
                display_count = min(len(sorted_history), 10)
                for i, record in enumerate(sorted_history[-display_count:]):
                    updown = record.get('updown', '')
                    if updown and '↑' in updown and '↓' not in updown:
                        trend = "📈"
                    elif updown and '↓' in updown and '↑' not in updown:
                        trend = "📉"
                    else:
                        trend = ""
                    
                    print(f"│      {record['date']:10} : {record['price']} 元/L {trend} {updown}")
                print(f"│      (共 {len(sorted_history)} 条记录)")
            else:
                print(f"│  {prefix} {fuel_name:11} : 无历史数据")
        
        print("└─────────────────────────────────────────────────┘")
        print("")
        
    except Exception as e:
        print(f"❌ 解析错误：{e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
