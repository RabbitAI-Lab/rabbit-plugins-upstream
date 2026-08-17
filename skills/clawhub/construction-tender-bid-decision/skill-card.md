## Description:

建筑工程投标决策分析助手，用于评估施工、市政、装修、园林、公路、房建、基建等工程项目是否值得投标，并基于招中标历史数据分析采购方、竞争者、报价参考、资质门槛和废标风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External construction bidding teams and agents use this skill to turn a specific engineering tender notice, title, or file into a bid/no-bid decision report with buyer history, likely competitors, pricing references, qualification risks, and action guidance. It can also generate a shareable HTML report from the completed analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores API credentials locally and uses them for vendor API calls.

Mitigation: Use an account key intended for this service, keep generated configuration files private, and remove the local key if the skill is no longer used.

Risk: Automatic registration collects platform, CPU architecture, and a hashed MAC address for device de-duplication.

Mitigation: Skip automatic registration by preconfiguring ZLBX_API_KEY, or decline registration and use the manual account portal.

Risk: Generated reports may include signed sk links that can bypass login for referenced platform pages.

Mitigation: Review reports before sharing and remove or redact access-bearing links when the recipient should not receive that access.

Risk: HTML reports are written to a user home-directory report folder by default.

Mitigation: Check the output path and file permissions before storing sensitive tender analysis or distributing the report.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/construction-tender-bid-decision)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [Workflow Guide](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto-Registration Guide](references/auto-register.md)
- [Zhiliao Biaoxun API Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Zhiliao Biaoxun Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s75)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown decision reports, optional self-contained HTML report files, configuration guidance, and internal API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full analysis is documented as about 12-25 API calls; quick analysis is documented as about 5-8 API calls. HTML reports are written under the user's home directory by default.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
