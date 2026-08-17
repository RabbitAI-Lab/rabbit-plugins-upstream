## Description:

商机雷达（知了标讯官方） helps agents find early business opportunities, sales leads, proposed projects, purchase intentions, expiring renewal windows, and project timeline signals for a requested industry, product, or region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and sales teams use this skill to scan for early business opportunities across proposed projects, purchase intentions, and expiring contracts, then receive a ranked lead list with objective next steps. The skill is intended for business development research based on Zhiliao Biaoxun data and user-provided search criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Opportunity search terms are sent to the Zhiliao Biaoxun API.

Mitigation: Avoid entering sensitive or restricted business plans unless sharing those terms with the vendor is acceptable.

Risk: Optional trial registration sends platform, CPU architecture, and a hashed MAC-derived identifier after consent.

Mitigation: Configure ZLBX_API_KEY before use to skip trial registration, or proceed only after the user agrees to the disclosed device-feature collection.

Risk: The skill stores a returned API key and generated HTML reports under the user's home directory.

Mitigation: Protect the local configuration and report directories, and review generated reports before sharing them outside the organization.

Risk: A full three-route scan consumes paid or trial account credits.

Mitigation: Tell the user the estimated 8-15 credit cost before a full scan and pause before exceeding the stated call budget.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-opportunity-radar)
- [Workflow Guide](references/workflow.md)
- [API Quick Reference](references/api-quick.md)
- [Auto Registration Guide](references/auto-register.md)
- [Report Template](references/report-template.md)
- [Zhiliao Business Opportunity Platform](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown lead report with an optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports rank opportunities by amount, maturity or urgency, and keyword match; HTML reports are written under the user's home directory when generated.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
