## Description:

Finds and prioritizes early business opportunities from proposed projects, procurement intentions, and expiring contracts in China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to identify and rank Chinese procurement leads before tender publication, then plan follow-up actions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Search terms and, during automatic registration, a hashed device identifier are sent to the vendor.

Mitigation: Review the vendor's data practices; supply your own ZLBX_API_KEY to avoid automatic registration.

Risk: The skill can create and store account credentials locally.

Mitigation: Consent before registration and review ~/.zlbx/config.json after use.

Risk: Forwarding signed sk links or exported HTML reports may grant access to underlying records.

Mitigation: Treat generated links and reports as sensitive and share them only with intended recipients.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-opportunity-radar)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [API quick reference](artifact/references/api-quick.md)
- [Opportunity scanning workflow](artifact/references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown opportunity list and standalone HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked leads with source links and suggested next steps; full scans also produce a shareable HTML report.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
