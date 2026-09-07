## Description:

Helps agents find early business opportunities by scanning proposed projects, purchase intentions, expiring contracts, and project timelines from the Zhiliao Biaoxun platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External sales, business development, and market research users use this skill to identify and prioritize early commercial opportunities by industry, product, region, amount threshold, and renewal timing. The skill returns ranked opportunity lists with next-step guidance and can export a shareable HTML report.

### Deployment Geography for Use:

Global use; data coverage and service endpoints are focused on the Zhiliao Biaoxun opportunity and bidding data platform.

## Known Risks and Mitigations:

Risk: Opportunity-search queries are sent to the third-party Zhiliao Biaoxun service.

Mitigation: Use the skill only for queries you are comfortable sharing with the vendor, and avoid entering sensitive internal opportunity strategy or customer information.

Risk: Automatic registration can send a stable MAC-derived device hash to the vendor.

Mitigation: Prefer supplying your own ZLBX_API_KEY through a secure environment variable, or proceed with automatic registration only after reviewing and accepting the device-hash behavior.

Risk: The skill can persist credentials locally in ~/.zlbx/config.json.

Mitigation: Protect the credential file, avoid committing it to repositories, and rotate or replace the API key if the local machine or file is exposed.

Risk: Generated sk and auto-login links can provide signed access to platform content or account flows.

Mitigation: Treat generated links as sensitive, avoid posting them publicly, and review shared HTML reports before distribution.

Risk: Evidence security notes an unsafe HTML renderer and advises review before broad sharing.

Mitigation: Open exported reports in trusted environments, inspect report content before forwarding, and avoid broad sharing until link-handling and credential-file protections are improved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-opportunity-radar)
- [Publisher Profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [API Quick Reference](references/api-quick.md)
- [Workflow](references/workflow.md)
- [Automatic Registration](references/auto-register.md)
- [Report Template](references/report-template.md)
- [Zhiliao Biaoxun Skill Documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Zhiliao Opportunity Master](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown opportunity lists with optional self-contained HTML report files and JSON report input.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires or obtains ZLBX_API_KEY, may store credentials in ~/.zlbx/config.json, and writes HTML reports to ~/zlbx-opportunity-radar-files/.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
