## Description:

Identifies out-of-region companies with strong and growing patent activity in a chosen industry and prepares an investment-promotion lead list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial-park and investment-promotion teams use patent activity to identify companies outside their province, assess recent patent growth and geographic presence, and prioritize outreach candidates.

### Deployment Geography for Use:

China-focused; patent searches may include international companies

## Known Risks and Mitigations:

Risk: Patent and business-intelligence queries are sent to PatentMax/ip930.com and may contain sensitive plans.

Mitigation: Avoid trade secrets or unpublished technical details unless external processing is acceptable; use only trusted endpoints.

Risk: Trial credentials and session data are cached locally.

Mitigation: Protect the local cache and remove it when no longer needed.

Risk: Company analysis and other API requests may incur charges.

Mitigation: Estimate costs and obtain user approval before optional paid analysis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/patent-investment-leads)
- [PatentMax API reference](references/api-reference.md)
- [Search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [CSV file, Text guidance]

**Output Format:** [Excel-compatible UTF-8 CSV and a concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranks company leads by recent patent activity and notes growth, provincial presence, and outreach considerations.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
