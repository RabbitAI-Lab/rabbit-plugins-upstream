#!/usr/bin/env python3
"""
A股全市场股票代码列表导出脚本
使用 AKShare 获取所有A股股票代码，保存为JSON文件供 stock-screener 使用
"""
import akshare as ak
import json
import sys
import os

def main():
    output_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..', 'all_a_shares.json')
    output_path = os.path.abspath(output_path)

    print("正在获取A股全市场数据...")
    df = ak.stock_zh_a_spot()
    print(f"获取到 {len(df)} 只股票")

    # 提取代码和名称，转换为 stock-screener 使用的格式
    stocks = []
    for _, row in df.iterrows():
        code = str(row['代码']).strip()
        name = str(row['名称']).strip()
        if code.startswith('bj'):
            continue  # 跳过北交所，专注沪深主板/创业板/科创板
        # 转换为 stock-screener 格式: sh600519 / sz000001
        if code.startswith('sh'):
            screener_code = code
        elif code.startswith('sz'):
            screener_code = code
        else:
            # akshare 返回的可能是纯数字代码，需要补上前缀
            if code.startswith('6'):
                screener_code = 'sh' + code
            elif code.startswith('0') or code.startswith('3'):
                screener_code = 'sz' + code
            else:
                continue
        stocks.append({
            'code': screener_code,
            'name': name,
            'akshare_code': code,
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(stocks, f, ensure_ascii=False, indent=2)

    print(f"已保存 {len(stocks)} 只股票到 {output_path}")

if __name__ == '__main__':
    main()
