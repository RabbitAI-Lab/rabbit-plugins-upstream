#!/usr/bin/env python3
"""
基金分析脚本 - 用于分析基金/ETF的年度走势和投资策略

使用方法：
    python3 fund_strategy_csv.py <CSV文件路径> [基金代码] [基金名称]

示例：
    python3 fund_strategy_csv.py investment_analysis/sz159768/sz159768.csv sz159768 房地产ETF银华
"""

import csv
import sys
import os
from datetime import datetime
from pathlib import Path


def load_data(file_path):
    """加载CSV数据"""
    data = []
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
            row['open'] = float(row['open'])
            row['close'] = float(row['close'])
            row['high'] = float(row['high'])
            row['low'] = float(row['low'])
            data.append(row)
    return sorted(data, key=lambda x: x['date'])


def analyze_annual(data):
    """年度分析"""
    years = {}
    for row in data:
        y = row['date'].year
        if y not in years:
            years[y] = []
        years[y].append(row)

    stats = []
    for y in sorted(years.keys()):
        y_data = years[y]
        high_row = max(y_data, key=lambda x: x['high'])
        low_row = min(y_data, key=lambda x: x['low'])

        start_price = y_data[0]['open']
        end_price = y_data[-1]['close']
        y_return = (end_price - start_price) / start_price * 100
        price_range = (high_row['high'] - low_row['low']) / low_row['low'] * 100

        stats.append({
            'year': y,
            'low': low_row['low'],
            'low_date': low_row['date'].strftime('%Y-%m-%d'),
            'high': high_row['high'],
            'high_date': high_row['date'].strftime('%Y-%m-%d'),
            'return': y_return,
            'range': price_range,
            'trading_days': len(y_data)
        })
    return stats


def generate_report(data, stats, fund_code, fund_name):
    """生成分析报告"""
    report = []
    report.append(f"# {fund_name} ({fund_code}) 投资分析报告\n")
    report.append(f"**分析日期**: {datetime.now().strftime('%Y-%m-%d')}")
    report.append(f"**数据期间**: {data[0]['date'].strftime('%Y-%m-%d')} 至 {data[-1]['date'].strftime('%Y-%m-%d')}")
    report.append(f"**交易日数**: {len(data)}天")
    report.append(f"**上市首日开盘价**: {data[0]['open']:.3f}元")
    report.append(f"**最新收盘价**: {data[-1]['close']:.3f}元")
    total_return = (data[-1]['close'] - data[0]['open']) / data[0]['open'] * 100
    report.append(f"**累计涨跌**: {total_return:.2f}%\n")

    report.append("---\n\n## 一、年度走势特点分析\n\n### 1.1 年度高低点统计\n")
    report.append("| 年份 | 年度低点 | 低点日期 | 年度高点 | 高点日期 | 年度收益率 | 年度波幅 |")
    report.append("|------|---------|----------|---------|----------|-----------|---------|")
    for s in stats:
        report.append(f"| {s['year']} | {s['low']:.3f} | {s['low_date']} | {s['high']:.3f} | {s['high_date']} | {s['return']:.2f}% | {s['range']:.2f}% |")
    report.append("")

    report.append("### 1.2 走势特点总结\n")
    avg_return = sum(s['return'] for s in stats) / len(stats)
    avg_range = sum(s['range'] for s in stats) / len(stats)
    report.append(f"1. **长期表现**: 近{len(stats)}年平均年化收益率为{avg_return:.2f}%")
    report.append(f"2. **波动特征**: 年度波幅平均为{avg_range:.2f}%，具有较高的波动性")
    report.append("3. **季节性规律**: 待分析具体数据")
    report.append("")

    report.append("---\n\n## 二、买入时机分析\n")
    report.append("请参考 SKILL.md 中的买入时机分析框架\n\n")
    report.append("---\n\n## 三、卖出时机分析\n")
    report.append("请参考 SKILL.md 中的卖出时机分析框架\n\n")
    report.append("---\n\n## 四、预估收益率\n")
    report.append("请参考 SKILL.md 中的预估收益率框架\n\n")
    report.append("---\n\n## 五、投资策略建议\n")
    report.append("请参考 SKILL.md 中的投资策略框架\n\n")
    report.append("---\n\n## 免责声明\n\n本分析仅基于历史数据，不构成投资建议。市场有风险，投资需谨慎。")

    return "\n".join(report)


def main():
    if len(sys.argv) < 2:
        print("使用方法: python3 analyze_fund.py <CSV文件路径> [基金代码] [基金名称]")
        sys.exit(1)

    file_path = sys.argv[1]
    fund_code = sys.argv[2] if len(sys.argv) > 2 else "未知"
    fund_name = sys.argv[3] if len(sys.argv) > 3 else "未知"

    if not Path(file_path).exists():
        print(f"错误: 文件不存在 {file_path}")
        sys.exit(1)

    print(f"加载数据: {file_path}")
    data = load_data(file_path)
    print(f"加载完成，共{len(data)}条记录")

    print("年度分析...")
    stats = analyze_annual(data)
    print(f"分析完成，共{len(stats)}年数据")

    print("生成报告...")
    report = generate_report(data, stats, fund_code, fund_name)

    # Use relative paths based on current working directory or skill location
    # Default to ./investment_analysis/<fund_code>_analysis.md but allow override via env var
    base_path = os.environ.get('FUND_ANALYSIS_BASE_PATH', 'investment_analysis')
    output_file = Path('.') / base_path / f"{fund_code}_analysis.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"报告已保存至: {output_file}")
    print("\n年度统计:")
    for s in stats:
        print(f"  {s['year']}: 低点 {s['low']:.3f} ({s['low_date']}), 高点 {s['high']:.3f} ({s['high_date']}), 收益 {s['return']:.2f}%, 波幅 {s['range']:.2f}%")


if __name__ == "__main__":
    main()
