---
name: data-analyzer
version: 1.1.0
description: |
  销售数据分析技能，支持数据查询、图表生成、趋势分析和 PDF 报告导出。
  用户询问销售数据、销售额、利润、销量、数据分析、图表或导出报告时使用本技能。
categories:
  - data-analysis
user-invocable: true
requires:
  bins: ["python3"]
---

# data-analyzer 销售数据分析技能

## 可用工具
1. **query_sales_data(question:string)** 分析查询：支持最高销售额/利润/销量、总销售额/总利润/总销量、按月汇总统计
2. **plot_sales_data(chart_type:string, metric:string)** 生成图表：chart_type 为 'line' 折线图或 'bar' 柱状图；metric 为 'sales'/'profit'/'quantity'
3. **analyze_sales_trend(question:string)** 趋势分析：如"为什么利润下降了？"返回按月利润变化
4. **export_report(questions:list, trends:list, charts:list)** 导出 PDF 报告：整合查询结果与图表到一份 PDF 文件并返回文件路径

## 触发条件
- 用户询问销售额、利润、销量等数据问题时，调用 query
- 用户要求画图、图表、可视化时，调用 plot
- 用户询问趋势、为什么上升/下降时，调用 trend
- 用户要求导出报告、生成 PDF、整合分析结果时，调用 report

## 调用方式
使用 bash exec 工具运行本目录下 data_analyzer.py 脚本，输出为 JSON：

```bash
# 查询
python3 ~/.openclaw/workspace/skills/data-analyzer/data_analyzer.py query "总销售额"
python3 ~/.openclaw/workspace/skills/data-analyzer/data_analyzer.py query "销售额最高的月份"
# 图表
python3 ~/.openclaw/workspace/skills/data-analyzer/data_analyzer.py plot line sales
python3 ~/.openclaw/workspace/skills/data-analyzer/data_analyzer.py plot bar profit
# 趋势
python3 ~/.openclaw/workspace/skills/data-analyzer/data_analyzer.py trend "为什么利润下降了"
# 导出 PDF 报告（问题可多个，--trend 可多个，--chart 可多个）
python3 ~/.openclaw/workspace/skills/data-analyzer/data_analyzer.py report "总销售额" "总利润" --trend "利润趋势" --chart line profit --chart bar sales
```

注意：
- 图表保存到 /tmp/sales_<metric>_<chart_type>.png，需要时告知用户文件路径
- PDF 报告保存到 ~/.openclaw/workspace/skills/data-analyzer/reports/sales_report_<时间戳>.pdf，返回该路径，并告知用户可通过 Windows 资源管理器 \\wsl$\Ubuntu\home\asus\.openclaw\workspace\skills\data-analyzer\reports\ 访问
