## Description:

Finds likely IPC classifications for a described technology by analyzing similar patents and provides plain-language meanings, examples, and a classification reference table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, patent researchers, and project teams use this skill to identify candidate IPC codes for a technology, compare keyword and classification searches, and prepare a reference table for further review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PatentMax receives potentially sensitive search terms, invention descriptions, applicant names, and patent numbers.

Mitigation: Do not submit confidential, pre-filing, export-controlled, or trade-secret details without approval; disclose the external service before use.

Risk: The bundled PatentMax tool supports more than IPC classification and can incur charges.

Mitigation: Limit use to the requested IPC task and explain expected paid calls before running them.

Risk: Service keys and cache data may be stored locally.

Mitigation: Keep PATENTMAX_API_KEY and PATENTMAX_BASE_URL under your control and protect locally stored credentials and cache data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/ipc-code-finder)
- [IPC query syntax](references/query-syntax.md)
- [Search workflow](references/search-workflow.md)
- [PatentMax API reference](references/api-reference.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Files]

**Output Format:** [Chinese-language summary and UTF-8 CSV reference table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists candidate IPC codes, occurrence counts, plain-language meanings, representative patents, and search coverage comparisons; not an official classification.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
