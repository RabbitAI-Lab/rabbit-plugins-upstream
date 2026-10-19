## Description:

Screens a technology area or company portfolio for high-value patents using maintenance history, citations, search ranking, and claim breadth, with a reason for each selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers and business teams use this skill to shortlist active granted invention patents for protection, acquisition, portfolio review, or pre-valuation screening. It provides a scored, source-backed shortlist rather than a formal appraisal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent search terms and selected patent identifiers are sent to the external PatentMax service.

Mitigation: Avoid confidential unpublished invention details unless external processing is acceptable.

Risk: An untrusted custom API endpoint could receive the API token.

Mitigation: Set PATENTMAX_BASE_URL only to a trusted destination.

Risk: A scored shortlist may be mistaken for a formal valuation or definitive legal-status check.

Mitigation: Use it for preliminary screening; seek a professional valuation for transactions and verify legal status against the official register.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ip930/skills/high-value-patents)
- [PatentMax API reference](references/api-reference.md)
- [Search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Text, CSV file]

**Output Format:** [UTF-8 CSV shortlist and concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked patent records include selection reasons and the source of each checked indicator; unverified indicators are marked as unchecked.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
