## Description:

Finds competitors’ newly published and granted patents, highlights notable filings, and summarizes emerging technical directions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to monitor competitors’ newly published or granted patents, review technical trends, and prepare periodic briefings.

### Deployment Geography for Use:

Global; patent coverage includes China, the United States, Europe, Japan, Korea, and WIPO.

## Known Risks and Mitigations:

Risk: API credentials may reach unapproved hosts or be sent over unencrypted connections.

Mitigation: Prefer the free trial until credential handling is hardened. Before using a paid key, require an approved HTTPS destination and redirects that cannot forward credentials elsewhere; avoid sharing keys in chat, check for an existing shared key, and set a spending limit.

Risk: Patent queries may contain confidential technical details that are sent to PatentMax.

Mitigation: Approve confidential details before searching, and omit sensitive information unless it is authorized for disclosure.

## Reference(s):

- [PatentMax API reference](references/api-reference.md)
- [Patent search workflow](references/search-workflow.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [ClawHub skill page](https://clawhub.ai/ip930/skills/competitor-patent-brief)

## Skill Output:

**Output Type(s):** [CSV files, Text]

**Output Format:** [Excel-compatible CSV patent brief with concise written highlights]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The brief lists relevant patent activity and highlights notable filings and technical directions.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
