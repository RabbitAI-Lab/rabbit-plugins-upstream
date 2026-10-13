## Description:

Analyzes construction tenders using historical bid and award data to recommend whether to bid, identify likely competitors, estimate a bid range, and flag qualification risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Construction contractors and bid teams use this skill to assess a specific tender, compare past awards and likely competitors, and prepare an evidence-backed bid decision and pricing reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trial registration collects a hashed MAC-derived device identifier.

Mitigation: Review the collection before consenting to registration; use a preconfigured API key to skip automatic registration.

Risk: Automatic registration stores an API key locally.

Mitigation: Protect the local credential file and avoid sharing or including the key in reports.

Risk: Reports may contain signed bid-record links or auto-login links that grant access to their recipients.

Mitigation: Treat generated HTML reports and signed links as sensitive; share them only with trusted recipients.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/construction-tender-bid-decision)
- [Vendor skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Analysis workflow](references/workflow.md)
- [Report template](references/report-template.md)
- [API quick reference](references/api-quick.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML report]

**Output Format:** [Markdown bid-decision report, with an HTML export in full mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes supporting bid records, a confidence rating, data gaps, and a suggested bid range; full analysis consumes account credits.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
