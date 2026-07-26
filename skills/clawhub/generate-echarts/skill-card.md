## Description: <br>
MCP ECharts 是一个基于 Apache ECharts 的动态图表生成和数据分析工具，支持多种导出格式和 MinIO 对象存储集成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to generate Apache ECharts visualizations from structured chart data and ECharts options. It supports common chart types such as line, bar, pie, radar, scatter, sankey, funnel, gauge, treemap, sunburst, heatmap, candlestick, boxplot, graph, parallel, and tree charts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Chart data may be sent to a referenced external service. <br>
Mitigation: Use only data appropriate for that external transfer, and avoid sensitive business, customer, financial, or proprietary datasets unless the publisher clarifies endpoint handling and retention. <br>
Risk: The API key is stored locally in .env. <br>
Mitigation: Use a limited-scope key where possible, keep .env out of source control, and rotate or remove the key when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/generate-echarts) <br>
- [Publisher profile](https://clawhub.ai/user/alinklab) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Files, Configuration] <br>
**Output Format:** [Markdown summaries with API-returned chart artifacts or ECharts options; chart output can be PNG, SVG, or option JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value; chart requests are sent to an external service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
