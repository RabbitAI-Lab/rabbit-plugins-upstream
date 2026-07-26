---
name: data_analyzer
description: 销售数据分析技能,支持查询、图表生成和深度分析
version: 1.0.0

---

# data_analyzer 技能
该技能提供四类数据分析工具：
## query_sales_data
对销售数据执行分析查询。支持:最高销售额/利润、总销售额/总利润、各地区/各月份统计、产品销量筛选。
参数: question (string) 用户的分析问题,如"销售额最高的月份是哪个月?"

## plot_sales_data
生成销售数据可视化图表。
参数:

- chart_type (string) 图表类型:'line'折线图 或 'bar'柱状图
- metric (string) 指标:'sales'销售额 或 'profit'利润

## analyze_sales_trend
对销售数据进行深度分析,生成业务洞察。
参数: question (string) 分析问题,如"为什么利润下降了?"

## generate_pdf_report
生成业务周报 PDF 报告，整合文字内容和图表。
参数：
- title （string）报告标题，默认“业务周报”
- content （string）查询结果文字内容
- chart_path (string) 图表图片路径（可选）