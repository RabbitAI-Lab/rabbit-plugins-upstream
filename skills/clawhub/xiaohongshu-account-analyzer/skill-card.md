## Description: <br>
Analyzes Xiaohongshu accounts and produces data-grounded diagnostic reports, comparable account recommendations, and practical optimization guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Xiaohongshu creators, MCN operators, brands, and content teams use this skill to evaluate account health, commercial value, content strategy, similar accounts, and multi-account comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Xiaohongshu account identifiers and analytics requests to RedFox using a REDFOX_API_KEY. <br>
Mitigation: Use it only for accounts the user is authorized to analyze, keep the API key in environment configuration, and avoid exposing the key in prompts, logs, or generated files. <br>
Risk: The security review reports disabled TLS verification and remote report JavaScript, which can reduce trust in fetched data or rendered reports. <br>
Mitigation: Prefer a fixed version that restores TLS verification and bundles report export JavaScript locally before relying on reports in sensitive workflows. <br>
Risk: The skill writes local raw data, report data, and HTML reports that may contain account analytics. <br>
Mitigation: Store generated output in an approved location, review it before sharing, and remove reports when they are no longer needed. <br>
Risk: Optional WebSearch enrichment and delayed subscription workflows can broaden profiling or create persistent follow-up tasks. <br>
Mitigation: Disable or explicitly approve cross-platform enrichment, and use delayed subscriptions only when the user understands and accepts the follow-up behavior. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-account-analyzer) <br>
- [RedFox API key setup](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [API guide](references/api_guide.md) <br>
- [Workflow guide](references/workflow_guide.md) <br>
- [Report template](references/report_template.md) <br>
- [Benchmark data](references/benchmark_data.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, HTML, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown diagnosis in chat plus generated JSON data files and HTML reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a REDFOX_API_KEY for account data, can write local report artifacts under output/, and may create a delayed follow-up task when the user opts into a subscription workflow.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
