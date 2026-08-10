## Description:

Pre-publication compliance and quality reviewer. Checks factual citations, customer redaction, product naming, competitor rules, internal information, formatting, and AI traces; outputs a pre-review report and fix suggestions without modifying the original.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Brand-side content marketing, editorial, and compliance teams use this skill to review finished technology-product drafts before publication. It checks factual support, customer redaction, product naming, competitor references, internal information, formatting, and content quality, then returns a pre-review report with fixes and an approval recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic activation phrases such as review can invoke the skill during ordinary review requests.

Mitigation: Use TCMS, compliance, or pre-publication context when requesting this skill, and confirm the requested review scope before relying on the report.

Risk: Compliance checks depend on the supplied brand rules, sensitive-term lists, product-public-status data, customer-redaction policy, competitor policy, and knowledge-base sources.

Mitigation: Provide current compliance profiles and approved sources; mark missing or unavailable references as incomplete or unverifiable in the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-compliance-reviewer)
- [README.md](artifact/README.md)
- [README_zh.md](artifact/README_zh.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown pre-review report with summary tables, issue bullets, citation verification, approval recommendation, and execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports issues and suggested fixes without modifying the original draft.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
