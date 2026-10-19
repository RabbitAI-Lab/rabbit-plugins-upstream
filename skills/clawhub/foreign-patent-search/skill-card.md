## Description:

Searches US, European, Japanese, Korean, and PCT patents using translated search terms and summarizes relevant results in Chinese with original-language titles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers, product teams, and other external users can find and compare foreign patents relevant to a technical idea and export a Chinese-language patent list for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search terms and technical descriptions are sent to PatentMax; unpublished inventions or business secrets may be sensitive.

Mitigation: Only submit sensitive material if external processing is acceptable, and omit unnecessary confidential details.

Risk: Changing the service endpoint could redirect API keys and patent queries to an untrusted destination.

Mitigation: Do not set PATENTMAX_BASE_URL unless you fully trust the endpoint.

Risk: Trial keys, cached patent data, budgets, and candidate ledgers may remain on the local machine.

Mitigation: Review and clear ~/.patentmax when that information should not be retained.

Risk: Translated search terms can miss patents, and foreign legal-status data may lag official records.

Mitigation: Check relevant local-language terms and verify consequential legal status against official patent registers.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/foreign-patent-search)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Search workflow](references/search-workflow.md)
- [PatentMax API reference](references/api-reference.md)

## Skill Output:

**Output Type(s):** [Text, CSV files]

**Output Format:** [Chinese-language Markdown summary and UTF-8 CSV patent list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes original-language titles, Chinese explanations, search terms, and publication numbers.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
