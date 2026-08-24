## Description:

临期项目与续约商机发现助手，用于查询合同到期前0-180天的项目、识别现供应商、按到期紧急度排序，并结合拟建项目与采购意向扫描输出商机清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, bidding, and business development teams use this skill to find China-focused renewal and replacement opportunities from expiring contracts, procurement intentions, and proposed projects. It helps prioritize opportunities by value, timing, buyer type, and next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives search terms and region or industry filters used for opportunity scanning.

Mitigation: Avoid entering sensitive internal strategy or confidential customer information in queries.

Risk: Automatic signup can use a MAC-derived device hash and create a local credential file.

Mitigation: Prefer a user-provided ZLBX_API_KEY when possible, and review or delete ~/.zlbx/config.json when the skill is no longer used.

Risk: Generated reports and sk or auto-login URLs can expose convenient access to report or account data if broadly shared.

Mitigation: Treat generated report files and signed links as sensitive and share them only with intended recipients.

Risk: The skill writes opportunity reports under ~/zlbx-opportunity-radar-files/.

Mitigation: Review generated files before redistribution and remove reports that are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/expiring-contract-renewal-finder)
- [API Quick Reference](artifact/references/api-quick.md)
- [Workflow](artifact/references/workflow.md)
- [Report Template](artifact/references/report-template.md)
- [Auto Registration](artifact/references/auto-register.md)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [知了商机大师](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown opportunity lists and generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service-returned opportunity links, local HTML report paths, scoring rationale, data gaps, and disclaimers.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
