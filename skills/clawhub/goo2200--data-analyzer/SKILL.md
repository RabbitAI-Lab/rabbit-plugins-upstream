---
name: data_analyzer
description: 销售数据分析技能，支持数据查询、图表生成、深度业务分析、自动整合图文导出PDF业务周报
version: 1.1.0
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
对销售数据进行深度分析，输出业务洞察文字结论。
参数: question (string) 分析问题,如"为什么利润下降了?"

## export_sales_pdf_report
整合数据查询文字结论、可视化图表、深度业务洞察，自动生成完整销售业务周报PDF文件，返回本地存储文件路径。
### 参数
1. query_result (string | list) 【必填】query_sales_data 输出的文字统计结果
2. chart_paths (list[str]) 【必填】plot_sales_data 生成的图表本地文件路径数组，支持多张图表嵌入周报
3. analysis_text (string) 【必填】analyze_sales_trend 输出的深度业务洞察分析文本
4. report_title (string) 【可选，默认：销售业务周报】周报PDF标题
5. report_date_range (string) 【可选】报表统计时间范围，如"2026年1月-6月"
### 返回值
string：生成完成的PDF文件本地绝对路径，可直接用于文件下载、文件读取操作
### 功能说明
1. 自动排版：封面标题、统计文字板块、图表插图板块、业务洞察分章节排版
2. 图文混排：依次插入文字数据、所有图表、深度分析结论
3. 标准化周报格式，适配销售业务汇报场景
4. 文件自动持久化存储，返回完整路径供上层接口读取下发
### 调用示例参数
{
  "query_result": "2026上半年总销售额1200万，华东区域销量第一",
  "chart_paths": ["./output/sales_bar.png", "./output/profit_line.png"],
  "analysis_text": "6月利润下滑原因为原材料涨价，建议调整产品定价",
  "report_title": "2026上半年华东销售周报",
  "report_date_range": "2026-01 ~ 2026-06"
}
