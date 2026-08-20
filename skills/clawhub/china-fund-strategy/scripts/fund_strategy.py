#!/usr/bin/env python3
"""
增强版基金分析脚本 - 主入口
支持 akshare 数据获取、增量分析和目录结构管理

使用方法：
    python3 fund_strategy.py <基金代码> [基金名称] [--use-akshare] [--csv-path <CSV路径>]

示例：
    # 使用 akshare 获取数据并分析
    python3 fund_strategy.py sz159768 "房地产ETF银华" --use-akshare
    
    # 使用本地 CSV 文件分析
    python3 fund_strategy.py sz159768 "房地产ETF银华" --csv-path investment_analysis/sz159768/sz159768.csv
"""

import sys
import argparse
from analyzer.base_analyzer import FundAnalyzer

def main():
    parser = argparse.ArgumentParser(description='基金分析工具')
    parser.add_argument('fund_code', help='基金代码')
    parser.add_argument('fund_name', nargs='?', default='', help='基金名称')
    parser.add_argument('--use-akshare', action='store_true', help='使用 akshare 获取数据')
    parser.add_argument('--csv-path', help='使用本地 CSV 文件')
    
    args = parser.parse_args()
    
    # 创建分析器实例
    analyzer = FundAnalyzer(args.fund_code, args.fund_name)
    
    # 执行分析
    analyzer.analyze(use_akshare=args.use_akshare, csv_path=args.csv_path)

if __name__ == '__main__':
    main()