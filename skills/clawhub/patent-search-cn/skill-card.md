## Description:

Search and analyze patents across PatentMax's supported jurisdictions, including similar patents, citations, and company portfolios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT

## Use Case:

Researchers, inventors, and patent analysts use the skill to find relevant patents, review individual publications, and explore citations, applicants, and filing trends. Results are research aids, not legal opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries or unpublished invention details may be sent to PatentMax.

Mitigation: Obtain approval for third-party processing before submitting confidential invention details.

Risk: A configured PatentMax endpoint may receive patent searches and bearer tokens.

Mitigation: Check that PATENTMAX_BASE_URL is unset or points to the intended service; keep live keys out of shared logs and synced configurations.

Risk: Small paid API calls may run without a hard prior-approval gate.

Mitigation: Require explicit user approval before any paid operation, including calls within the skill's default spending allowance.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-search-cn)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [API reference](references/api-reference.md)
- [Search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with patent search results, analysis, citations, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search scope, query terms, limitations, and estimated or incurred API charges where applicable.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
