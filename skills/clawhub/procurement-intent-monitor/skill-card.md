## Description:

采购意向监控与早期商机发现助手，可帮助用户查询发标前1-3个月的采购意向、拟建项目和临期续约机会，并按行业、地区、预算和优先级生成商机清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to find early procurement opportunities before formal bid publication, monitor intent announcements, scan proposed projects, and track expiring contracts. The skill returns prioritized opportunity reports with next-step guidance based on public procurement and project data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can preserve signed links containing sk parameters in reports and shareable outputs.

Mitigation: Treat reports and links containing sk as sensitive, avoid broad forwarding, and review generated reports before sharing outside the intended audience.

Risk: The skill stores credentials in ~/.zlbx/config.json and writes generated reports under ~/zlbx-opportunity-radar-files/.

Mitigation: Protect the local config and report directories with normal credential hygiene, and preconfigure ZLBX_API_KEY when centralized secret management is preferred.

Risk: Procurement queries are sent to Zhiliaobiaoxun services and may consume account credits.

Mitigation: Confirm the user is comfortable sending the query terms to Zhiliaobiaoxun, disclose expected credit use before scans, and keep API keys out of conversation output.

Risk: Automatic registration may collect platform, CPU architecture, and hashed MAC address for free-trial device deduplication.

Mitigation: Request user consent before auto-registration, allow users to skip it by setting ZLBX_API_KEY, and do not collect hostnames, usernames, paths, or file contents.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/procurement-intent-monitor)
- [Publisher Profile](https://clawhub.ai/user/dragonzu)
- [Workflow Reference](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Report Template](references/report-template.md)
- [Auto-Registration Reference](references/auto-register.md)
- [Zhiliaobiaoxun API Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun Agent Portal](https://agent.zhiliaobiaoxun.com)
- [Zhiliaobiaoxun Registration and Recharge](https://ai.zhiliaobiaoxun.com/?ch=s99)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown opportunity reports, optional self-contained HTML report files, and concise setup or follow-up guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include prioritized procurement opportunities, public data links, scan counts, disclaimers, and local HTML file paths.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
