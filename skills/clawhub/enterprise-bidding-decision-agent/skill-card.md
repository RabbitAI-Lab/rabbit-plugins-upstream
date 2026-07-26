## Description: <br>
企业投标决策智能助手 analyzes a specific tender using Zhiliaobiaoxun bidding data to produce bid/no-bid guidance, competitor forecasts, win probability signals, pricing references, buyer preference analysis, and disqualification risk notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business development, sales, and bid teams use this agent to evaluate whether to pursue a specific procurement opportunity, estimate competitive pressure, and draft a concise decision report grounded in bidding history. It is intended for users who provide a tender link, project title, or tender file and need commercial bid-decision support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-register a vendor account and persist an API key when ZLBX_API_KEY is not already configured. <br>
Mitigation: Prefer preconfiguring ZLBX_API_KEY or reviewing the auto-registration flow before installation so users understand the account creation and local credential storage behavior. <br>
Risk: Generated reports may preserve signed sk links returned by the API, which can make shared reports easier to access than intended. <br>
Mitigation: Review HTML and Markdown reports before sharing externally, and remove signed links unless the recipient is intended to receive them. <br>
Risk: Bid recommendations can influence commercial decisions and may be wrong if source data is incomplete, stale, or unavailable. <br>
Mitigation: Treat the report as decision support, require human review, and preserve the documented data gaps, time ranges, and disclaimers in final outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-bidding-decision-agent) <br>
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [API Quick Reference](artifact/references/api-quick.md) <br>
- [Workflow](artifact/references/workflow.md) <br>
- [Report Template](artifact/references/report-template.md) <br>
- [Auto Registration](artifact/references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision report, optional HTML report file, and concise user guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or vendor auto-registration; normal full analysis is documented as about 12-25 API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
