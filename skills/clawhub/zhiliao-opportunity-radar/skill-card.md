## Description:

商机雷达（知了标讯官方） helps agents find early sales opportunities from proposed projects, procurement intents, and expiring contracts before formal tenders are published.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and market research users use this skill to scan Chinese project and procurement data for early opportunity signals, rank leads by value and timing, and produce a concise opportunity list with next actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Search terms and a MAC-derived hashed device identifier may be sent to the vendor during use or automatic registration.

Mitigation: Prefer providing an existing API key and review the vendor registration flow before allowing automatic account creation.

Risk: The skill can store a vendor API key in ~/.zlbx/config.json.

Mitigation: Protect or delete the local credential file when the skill is no longer needed.

Risk: Generated reports and raw result links may contain login-bypass sk links.

Mitigation: Share generated reports and result links only with trusted recipients.

Risk: Opportunity summaries can affect commercial decisions and may reflect incomplete or delayed public data.

Mitigation: Review source records and independently validate important amounts, dates, organizations, and next actions before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-opportunity-radar)
- [Workflow reference](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Auto-registration reference](references/auto-register.md)
- [Report template reference](references/report-template.md)
- [Zhiliao opportunity platform](https://agent.zhiliaobiaoxun.com)
- [Zhiliao AI platform skill docs](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown opportunity summaries, optional self-contained HTML reports, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call vendor APIs, read or persist a vendor API key, and write local HTML report files.]

## Skill Version(s):

1.0.4 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
