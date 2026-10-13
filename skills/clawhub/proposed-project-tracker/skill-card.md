## Description:

Finds and ranks early-stage project, procurement-intent, and expiring-contract opportunities by industry, product, and region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to find and prioritize Chinese project approvals, upcoming procurement, and contract-renewal opportunities, with suggested follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor receives search terms during queries and a hashed device identifier during optional registration.

Mitigation: Review the vendor's data handling before use; obtain consent before registration, or use an existing API key.

Risk: API keys are stored in ~/.zlbx/config.json and could be exposed if the file is shared.

Mitigation: Restrict access to the local configuration file and do not include keys in reports or shared messages.

Risk: Generated report links contain sk login-bypass parameters that may grant access to recipients.

Mitigation: Treat report links as sensitive and share reports only with trusted recipients after reviewing their access implications.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/proposed-project-tracker)
- [API quick reference](artifact/references/api-quick.md)
- [Opportunity scanning workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Vendor skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Markdown, HTML report, Guidance]

**Output Format:** [Ranked Markdown opportunity list and optional shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes project links, ranking rationale, data gaps, and recommended next actions.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
