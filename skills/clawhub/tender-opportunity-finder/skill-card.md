## Description:

Finds and ranks early tender opportunities from proposed projects, purchase intentions, and contracts nearing expiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to find and prioritize potential tender opportunities in China before bidding begins, with suggested follow-up actions.

### Deployment Geography for Use:

Global (China-focused tender data)

## Known Risks and Mitigations:

Risk: Automatic registration uses device-derived information to create an account.

Mitigation: Review the registration flow and obtain user consent first, or supply a ZLBX_API_KEY to skip registration.

Risk: A locally stored API key could be disclosed or reused by someone with access to the machine.

Mitigation: Protect the local credential file and never paste or share the API key in chat or reports.

Risk: Result links include signed access parameters that can grant access when shared in chat or HTML reports.

Mitigation: Treat signed result links and generated reports as sensitive; avoid forwarding reports publicly.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/tender-opportunity-finder)
- [Skill usage documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [API quick reference](references/api-quick.md)
- [Opportunity scanning workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [Registration and credential handling](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML report, Guidance]

**Output Format:** [Ranked Markdown opportunity list and shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, ranking rationale, and suggested next steps; full scans produce an HTML file.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
