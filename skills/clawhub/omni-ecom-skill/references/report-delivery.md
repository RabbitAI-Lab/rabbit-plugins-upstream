# 报告交付与图表化 PDF

## 默认主交付物

周报、月报、年报、店铺诊断和经营复盘都默认生成 A4 图表化 PDF，不等待用户追加“转 PDF”。PDF 至少包含 3 张与当前数据直接对应的内嵌图表（例如 GMV/流量/转化趋势、渠道结构、商品或投流效率），不使用外链图片。

交付集合：`report.json`、`report.md`、`report.pdf`、`pdf-delivery.json`、`release-receipt.json`。PPT/XLSX 是可选下游格式，不能替代 PDF 主交付物。

## PDF 质量

- 首页显示客户范围、期间、专家团版本、报告修订号、执行模式和一句话结论。
- 图表、表格和正文只消费已批准指标；图注写清口径和时间。
- 中文字体正常、无空白页、无图表溢出；页数超限时压缩图表或合并重复章节，不删除事实结论。
- `pdf-delivery.json.status` 不是 `pdf_render_verified` 时不得公开交付。

宿主不支持文件或图表生成时，诚实返回 `pdf_delivery_unavailable`，并提供可渲染的结构化底稿和图表规格，不声称“PDF 已生成”。
