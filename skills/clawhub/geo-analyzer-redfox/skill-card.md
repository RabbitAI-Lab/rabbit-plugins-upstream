## Description: <br>
GEO Analyzer submits brand questions to Doubao, Kimi, and DeepSeek, analyzes mentions, sentiment, citations, and competitors, and produces an interactive HTML report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Brand marketers, product managers, and content operators use this skill to measure how a brand appears in AI search answers, compare competitors, inspect cited sources, and identify GEO optimization opportunities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated report can incorrectly summarize sentiment as fully positive even when negative results exist. <br>
Mitigation: Manually verify sentiment metrics before using the report for business decisions until the positive-rate summary issue is fixed. <br>
Risk: Brand plans, unreleased product names, or other confidential prompts could be submitted during analysis. <br>
Mitigation: Use non-sensitive brand and category inputs, and avoid confidential or unreleased information in questions. <br>
Risk: The RedFox API key is required for execution and could be exposed if mishandled. <br>
Mitigation: Provide REDFOX_API_KEY through environment or configuration only, and avoid placing it in code, prompts, logs, or output files. <br>


## Reference(s): <br>
- [GEO metrics reference](artifact/references/geo-metrics.md) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/geo-analyzer-redfox) <br>
- [RedFox API key setup](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, HTML, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON intermediate files, and an interactive HTML report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; results depend on Doubao, Kimi, and DeepSeek responses at analysis time.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
