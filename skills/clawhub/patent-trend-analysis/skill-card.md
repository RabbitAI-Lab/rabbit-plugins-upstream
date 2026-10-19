## Description:

Analyzes annual patent filing trends, changes in leading applicants, and new entrants for a technology using PatentMax data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, researchers, and business teams use this skill to chart patent filing volumes, assess a technology's patent activity stage, and compare leading applicants and new entrants over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and technical descriptions are sent to PatentMax/ip930.com, which may expose confidential unpublished inventions.

Mitigation: Use only when external sharing of the submitted technical details is acceptable; avoid confidential unpublished inventions otherwise.

Risk: A custom API endpoint can receive the provided PatentMax API key.

Mitigation: When supplying PATENTMAX_API_KEY, leave PATENTMAX_BASE_URL unset or verify it points to the legitimate PatentMax API.

Risk: Trial credentials and task data can remain in the local PatentMax cache.

Mitigation: Review access to and retention of the ~/.patentmax cache after use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-trend-analysis)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax query syntax](artifact/references/query-syntax.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [UTF-8 CSV trend table and text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports filing-year counts, year-over-year changes, leading applicants, and new entrants; notes recent-year publication lag and search scope.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
