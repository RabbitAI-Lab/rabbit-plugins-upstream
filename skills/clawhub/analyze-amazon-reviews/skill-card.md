## Description: <br>
Fetches Amazon product reviews through the Reveyes task API, applies cost-aware sampling and evidence-grounded Voice of Customer analysis, and generates a self-contained interactive HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhuojiuya](https://clawhub.ai/user/zhuojiuya) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and marketplace operators use this skill to fetch Amazon ASIN reviews, analyze product pain points, return reasons, selling points, listing gaps, media defects, variants, and competitor differences, then produce evidence-backed reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The paid Reveyes API can spend points when a fetch is executed. <br>
Mitigation: Generate and review a non-billable plan first, require an explicit maximum point confirmation before fetch, and reuse permanent task IDs when available. <br>
Risk: The Reveyes API key can be exposed if pasted into prompts, reports, or source files. <br>
Mitigation: Load the key from REVEYES_API_KEY or an explicit env file, do not print or embed it in generated files, and rotate any key pasted into chat. <br>
Risk: Raw run directories can contain reviewer names, profile URLs, task IDs, and raw review text. <br>
Mitigation: Share the default public HTML report rather than raw run directories unless the recipient is authorized to receive the underlying data. <br>
Risk: Review analysis can overstate evidence or imply product-wide conclusions from targeted samples. <br>
Mitigation: Label computed metrics as sample values, bind conclusions to valid review IDs and exact quotes, validate analysis JSON before rendering, and disclose unavoidable limitations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhuojiuya/skills/analyze-amazon-reviews) <br>
- [Reveyes](https://www.reveyes.cn/) <br>
- [Reveyes API base](https://server.reveyes.cn/api/open) <br>
- [Evidence-grounded review analysis methodology](references/analysis-methodology.md) <br>
- [Semantic analysis JSON contract](references/analysis-schema.md) <br>
- [Reveyes review API reference](references/reveyes-api.md) <br>
- [Scenario routing and sampling plans](references/scenario-routing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, json, html files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON analysis artifacts, and a self-contained HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local run directory for plans, fetched review data, analysis JSON, validation output, and rendered report.html.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
