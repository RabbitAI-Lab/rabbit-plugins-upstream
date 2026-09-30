#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中国油价查询 - Python 解析模块
用法：python3 oil_price.py <临时文件路径> <省份编码> <时间戳>
"""

import json
import html
import sys

# API 返回的 HTML 实体编码的燃油名称（用于匹配）
FUEL_NAMES_HTML = {
    '89\u53f7\u6c7d\u6cb9': 'gasoline_89',
    '92\u53f7\u6c7d\u6cb9': 'gasoline_92',
    '95\u53f7\u6c7d\u6cb9': 'gasoline_95',
    '98\u53f7\u6c7d\u6cb9': 'gasoline_98',
    '0\u53f7\u67f4\u6cb9': 'diesel_0'
}

# 解码后的燃油名称（用于输出显示）
FUEL_NAMES_DISPLAY = {
    '89\u53f7\u6c7d\u6cb9': '89 号汽油',
    '92\u53f7\u6c7d\u6cb9': '92 号汽油',
    '95\u53f7\u6c7d\u6cb9': '95 号汽油',
    '98\u53f7\u6c7d\u6cb9': '98 号汽油',
    '0\u53f7\u67f4\u6cb9': '0 号柴油'
}

def main():
    if len(sys.argv) != 4:
        print("用法：python3 oil_price.py <临时文件路径> <省份编码> <时间戳>", file=sys.stderr)
        sys.exit(1)
    
    tmpfile = sys.argv[1]
    province_code = sys.argv[2]
    timestamp = sys.argv[3]
    
    try:
        with open(tmpfile, 'r', encoding='utf-8') as f:
            raw_response = f.read()
        
        # 先解码 HTML 实体，再解析 JSON
        decoded_response = html.unescape(raw_response)
        data = json.loads(decoded_response)
        
        # 查找对应的省份城市（通过 adcode 匹配）
        target_city = None
        for city in data.get('cities', []):
            if city.get('adcode') == province_code:
                target_city = city
                break
        
        if not target_city:
            print(f"❌ 未找到省份信息：{province_code}", file=sys.stderr)
            sys.exit(1)
        
        province_name = html.unescape(target_city.get('city', '未知'))
        cities_data = target_city.get('data', [])
        
        # 初始化燃油字典
        gasoline_89 = None
        gasoline_92 = None
        gasoline_95 = None
        gasoline_98 = None
        diesel_0 = None
        
        # 遍历所有燃油数据项
        for item in cities_data:
            fuel_name_html = item.get('name', '')
            price = html.unescape(item.get('price', ''))
            last_price = html.unescape(item.get('last', ''))
            
            # 使用独立的 if 语句（不是 elif），确保每个条件都能被检查
            if fuel_name_html == '89\u53f7\u6c7d\u6cb9':
                gasoline_89 = {'name': '89 号汽油', 'price': price, 'last': last_price}
            elif fuel_name_html == '92\u53f7\u6c7d\u6cb9':
                gasoline_92 = {'name': '92 号汽油', 'price': price, 'last': last_price}
            elif fuel_name_html == '95\u53f7\u6c7d\u6cb9':
                gasoline_95 = {'name': '95 号汽油', 'price': price, 'last': last_price}
            elif fuel_name_html == '98\u53f7\u6c7d\u6cb9':
                gasoline_98 = {'name': '98 号汽油', 'price': price, 'last': last_price}
            elif fuel_name_html == '0\u53f7\u67f4\u6cb9':
                diesel_0 = {'name': '0 号柴油', 'price': price, 'last': last_price}
        
        # 格式化输出
        print(f"\n============================================================")
        print(f"  油价查询结果 ({timestamp})")
        print("============================================================")
        print("")
        print("┌─────────────────────────────────────────────────┐")
        print(f"│  {province_name:18} 油价信息                     │")
        print("├─────────────────────────────────────────────────┤")
        
        fuels = [
            (gasoline_89, '89 号汽油', '⛽'),
            (gasoline_92, '92 号汽油', '⛽'),
            (gasoline_95, '95 号汽油', '⛽+'),
            (gasoline_98, '98 号汽油', '⛽++'),
            (diesel_0, '0 号柴油', '⛽')
        ]
        
        for fuel_info, fuel_name, prefix in fuels:
            if fuel_info and fuel_info['price']:
                price_str = f"   {fuel_info['price']} 元/L"
                last_price_str = f" (上次：{fuel_info['last']})"
                
                # 判断涨跌
                if fuel_info['last']:
                    try:
                        old_price = float(fuel_info['last'])
                        new_price = float(fuel_info['price'])
                        diff = round(new_price - old_price, 2)
                        
                        if diff > 0:
                            trend = "📈"
                            diff_str = f"+{diff}"
                        elif diff < 0:
                            trend = "📉"
                            diff_str = f"{diff}"
                        else:
                            trend = "➡️"
                            diff_str = "0.00"
                    except ValueError:
                        trend = "➡️"
                        diff_str = "无历史数据"
                else:
                    trend = "➡️"
                    diff_str = "无历史数据"
                
                print(f"│  {prefix} {fuel_name:11} : {price_str:12} {last_price_str:8} {trend} {diff_str}")
            else:
                print(f"│  {prefix} {fuel_name:11} :   无数据                       ➡️  未销售")
        
        print("└─────────────────────────────────────────────────┘")
        print("")
        
    except Exception as e:
        print(f"❌ 解析错误：{e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
