## Description: <br>
图表工具服务 is an MCP-style skill that sends Quick Chart-compatible JSON to an upstream service and returns generated chart image data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to generate chart image links from Quick Chart-style JSON parameters through an upstream service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags unrelated XBY/Gaokao credential handling and silent local API-key persistence for a chart-generation skill. <br>
Mitigation: Review the upstream service dependency before installation, use a dedicated key, and isolate the execution environment and local .env file. <br>
Risk: The skill sends user-provided chart parameters and an XBY API key to an upstream service. <br>
Mitigation: Avoid sending sensitive chart data, limit credential scope where possible, and remove persisted credentials when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alinklab/skills/quick-chart) <br>
- [Xiaobenyang service](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Markdown or structured text summarizing raw JSON responses and chart image links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY API key and upstream network access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
