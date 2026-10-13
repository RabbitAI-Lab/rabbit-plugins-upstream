## Description:

帮助用户发现即将到期的采购合同与续约机会，并结合拟建项目和采购意向生成优先排序的商机清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to find Chinese procurement opportunities by industry, product, and region, identify incumbent suppliers, and prioritize upcoming contract renewals alongside planned projects and purchase intentions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration sends a hashed MAC-derived device identifier and platform details to the service.

Mitigation: Provide your own ZLBX_API_KEY to skip registration, or explicitly consent before device information is collected and sent.

Risk: Saved credentials, HTML reports, and signed announcement links may expose account access or sensitive opportunity details if shared.

Mitigation: Restrict access to ~/.zlbx/config.json and reports; do not publish signed links, recharge or login links, or saved reports broadly.

Risk: Searches consume paid service credits and procurement results may be incomplete or out of date.

Mitigation: Review the estimated credit usage before scanning and verify high-priority opportunities against their linked source notices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/expiring-contract-renewal-finder)
- [API quick reference](references/api-quick.md)
- [Opportunity-scanning workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Auto-registration procedure](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML reports, Guidance]

**Output Format:** [Prioritized opportunity list in Markdown, with an optional saved HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes opportunity rankings, source links, and suggested next steps; full scans save a shareable HTML report.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
