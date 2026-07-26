## Description: <br>
Mines related Ozon and available Wildberries keywords from a seed term using Seerfar data, then returns market metrics such as search volume, growth, product and seller counts, competition, pricing, relevancy, title density, cart-add conversion, and top products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and commerce analysts use this skill to expand Ozon keyword ideas around a seed term, find long-tail or low-competition opportunities, and inspect market profiles before deciding what to query next. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and sends keyword queries plus session metadata to LinkFox-controlled services. <br>
Mitigation: Install only when that data sharing is acceptable; use a scoped API key and avoid sending sensitive query terms or workspace metadata. <br>
Risk: Each API call can spend LinkFox credits, and repeated exploration can increase cost. <br>
Mitigation: Confirm cost expectations before repeated calls, rely on the built-in 24-hour cache for identical parameters, and ask before broad follow-up queries. <br>
Risk: Full API responses are persisted locally in the workspace or fallback LinkFox data directory. <br>
Mitigation: Use the skill only in workspaces where local response storage is acceptable, and review or clean saved response files when they contain sensitive market research. <br>
Risk: Security evidence flags onboarding installation and automatic feedback reporting as behavior to review in sensitive environments. <br>
Mitigation: Review or disable those flows before deploying the skill in restricted workspaces. <br>


## Reference(s): <br>
- [Seerfar Ozon keyword mining API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-keyword-mining) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples; runtime output is JSON or a concise text summary with a saved JSON file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved locally; small responses can be printed inline, large responses are summarized, and repeated parameter sets may be served from a 24-hour local cache.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
