## Description:

帮助代理根据产品线和地区扫描医疗设备相关拟建项目、采购意向和临期续约机会，并按预算、成熟度和紧急度生成可跟进的商机清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and procurement intelligence users use this skill to find early hospital and medical-equipment purchasing opportunities before formal tender activity. Given a product line and region, the agent queries proposed projects, purchase intentions, and expiring contracts, then returns a prioritized opportunity list with suggested next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-register a vendor account and store an API key locally.

Mitigation: Require explicit user consent before registration, prefer a user-supplied ZLBX_API_KEY, and avoid exposing API keys in conversation or reports.

Risk: Auto-registration transmits a MAC-derived device hash for free-trial de-duplication.

Mitigation: Tell users what device fields are collected before registration and allow them to bypass the flow by setting their own API key.

Risk: Generated reports and opportunity links may include login-bypass or signed access URLs.

Mitigation: Treat generated reports and signed URLs as sensitive and share them only with trusted recipients.

Risk: The skill handles real procurement entities and may surface incomplete or delayed procurement data.

Mitigation: Keep claims factual, include data gaps and disclaimers, and require independent review before commercial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/medical-equipment-opportunity-radar)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow guide](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Auto-registration guide](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration API](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists, optional self-contained HTML reports, JSON report inputs, and user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; complete scans are expected to consume 8-15 account credits.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
