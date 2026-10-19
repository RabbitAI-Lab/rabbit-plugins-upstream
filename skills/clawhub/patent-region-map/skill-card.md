## Description:

Maps patents for a technology by province, city, or country and identifies leading applicants in each region.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Industry researchers, business development teams, and developers use this skill to compare regional patent activity, identify leading applicants, and prepare a spreadsheet-friendly regional distribution table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries or technical descriptions are sent to the PatentMax API, potentially exposing unpublished or confidential information.

Mitigation: Do not submit confidential unpublished material; obtain approval before sending sensitive queries.

Risk: Paid API requests can accrue charges, and the client supports more patent-search and analysis actions than regional CSV generation.

Mitigation: Set a task budget and confirm the planned calls and scope before running paid commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-region-map)
- [PatentMax API reference](references/api-reference.md)
- [PatentMax query syntax](references/query-syntax.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [CSV, Text, Markdown]

**Output Format:** [UTF-8 CSV with BOM and a brief written summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes regional patent counts, shares, leading applicants, and recent application volumes when available.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
