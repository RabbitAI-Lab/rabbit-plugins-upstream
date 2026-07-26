## Description: <br>
text2echart generates ECharts chart configurations and HTML/SVG/PNG chart outputs from JSON or CSV data through an agent-facing workflow, CLI, and interactive web app. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ifeel-is-a-mouse](https://clawhub.ai/user/ifeel-is-a-mouse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use text2echart to turn structured JSON or CSV data into ECharts visualizations, including browser-previewable HTML and CLI-generated chart files. It is suited to chart, graph, visualization, SVG, screenshot, and word cloud requests where the user explicitly asks for chart generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML in default CDN mode may expose confidential chart data to externally loaded assets. <br>
Mitigation: Use embed or offline mode for sensitive charts and review generated HTML before sharing. <br>
Risk: Documentation may overstate some behaviors, including browser opening and the breadth of CLI CSV chart support. <br>
Mitigation: Confirm the requested output mode and chart type after generation, especially for CLI-driven workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ifeel-is-a-mouse/skills/text2echart) <br>
- [Prompt guide](prompt.md) <br>
- [ECharts option reference](references/echarts-option-reference.md) <br>
- [ECharts Chinese option reference](references/echarts-option-zh.md) <br>
- [ECharts wordcloud reference](references/echarts-wordcloud.md) <br>
- [ECharts title documentation](https://echarts.apache.org/en/option.html#title) <br>
- [ECharts grid documentation](https://echarts.apache.org/en/option.html#grid) <br>
- [ECharts series bar documentation](https://echarts.apache.org/en/option.html#series-bar) <br>
- [ECharts series line documentation](https://echarts.apache.org/en/option.html#series-line) <br>
- [ECharts series pie documentation](https://echarts.apache.org/en/option.html#series-pie) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with HTML, JSON, and shell command snippets; CLI runs can produce HTML, SVG, or PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports JSON/CSV inputs; SVG and PNG export require Playwright, and default CDN mode may reference external ECharts assets.] <br>

## Skill Version(s): <br>
2.3.11 (source: server release metadata, artifact metadata, and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
