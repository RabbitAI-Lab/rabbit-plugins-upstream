## Description: <br>
Tracks industry prosperity by combining A-share leading company financial data with macro indicators such as PMI, PPI, exports, and imports to calculate a 0-100 prosperity score and classify the industry cycle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sunsongyeah](https://clawhub.ai/user/sunsongyeah) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to fetch public macroeconomic and A-share company indicators, calculate an industry prosperity score, and generate a local research report. It supports built-in sectors and custom sectors where representative A-share leading stocks are supplied. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public financial and macroeconomic data online through AKShare, so upstream site changes, network failures, or delayed source data can make outputs incomplete or stale. <br>
Mitigation: Review fetch warnings, data dates, and source labels in the generated report before relying on the score. <br>
Risk: The output is finance research support and could be mistaken for investment advice. <br>
Mitigation: Keep the report disclaimer visible and treat scores as data aggregation and indicator calculation only, not buy, sell, price, return, or outcome guidance. <br>
Risk: Custom sectors require representative A-share stock selections, which can bias the calculated prosperity score if the selected companies are not appropriate proxies. <br>
Mitigation: Use 2-5 liquid, representative industry leaders and document or review the selection before running custom-sector analysis. <br>
Risk: The HTML report generator processes local JSON input and renders an HTML file. <br>
Mitigation: Use trusted generated JSON inputs and avoid feeding untrusted sector names, stock names, or JSON content into the report generator. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sunsongyeah/skills/industry-prosperity-tracker) <br>
- [Data Sources](references/data_sources.md) <br>
- [Industry Registry](references/industry_registry.md) <br>
- [Scoring Methodology](references/scoring_methodology.md) <br>
- [Semiconductor Indicators](references/semiconductor_indicators.md) <br>
- [Semiconductor Industry Association](https://www.semiconductors.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, HTML files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus generated JSON data files and a local HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes data/{sector}_latest.json, data/{sector}_scored.json, and output/{sector}_report.html when the documented scripts are run.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
