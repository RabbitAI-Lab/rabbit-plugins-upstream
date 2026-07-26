## Description: <br>
Analyzes Amazon keyword-level competition by querying LinkFox SIF data for search volume, product counts, ad competition, popularity rank, and supply-demand ratio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace analysts, and agents use this skill to evaluate keyword competition across supported Amazon marketplaces and present the returned SIF metrics in concise tables or summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon keyword queries, API credentials, and session or app metadata are sent to LinkFox services. <br>
Mitigation: Install and run the skill only when that data sharing is acceptable, and restrict credentials to the minimum required scope. <br>
Risk: Full API responses are saved locally and may contain sensitive keyword research. <br>
Mitigation: Review the configured output location and periodically clean LinkFox cache and output directories for sensitive projects. <br>
Risk: Feedback reporting can send user comments or task context to LinkFox services. <br>
Mitigation: Review or disable feedback-reporting behavior before use in workflows with private or regulated content. <br>
Risk: API calls consume LinkFox credits. <br>
Mitigation: Warn users before repeated or multi-marketplace calls and reuse cached results when appropriate. <br>


## Reference(s): <br>
- [SIF keyword API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-keyword-overview) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and tables, shell command examples, and JSON API responses saved to local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a single keyword per request, supports 13 Amazon marketplaces, and stores full API responses locally while summarizing large responses.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
