## Description:

AI bidding strategy advisor that analyzes a specific procurement opportunity using ZLBX historical tender and award data to produce bid/no-bid, pricing, competitor, buyer-pattern, win-probability, risk, and action guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding and proposal teams use this skill to decide whether and how to bid on a specific procurement project. It helps compare buyer history, likely competitors, pricing ranges, data gaps, risks, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bidding projects, competitor names, pricing assumptions, or procurement targets may be exposed through the skill's vendor-backed analysis workflow.

Mitigation: Review the skill before installing for sensitive bidding work and only submit project details appropriate for processing by the ZLBX service.

Risk: The skill can persist an API key in ~/.zlbx/config.json.

Mitigation: Prefer a preconfigured ZLBX_API_KEY where possible and check permissions on ~/.zlbx/config.json when local key storage is used.

Risk: Automatic registration transmits device-identifying registration data, and generated reports include vendor-provided commercial links.

Mitigation: Require user consent before automatic registration, avoid auto-registration when a key is already configured, and treat generated report links as vendor-provided content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-strategy-advisor)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Workflow](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Automatic registration flow](references/auto-register.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZLBX AI platform](https://ai.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown decision report, optional self-contained HTML report, and JSON input for the report renderer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include cited ZLBX data links where available; exported HTML is written to a local report directory.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
