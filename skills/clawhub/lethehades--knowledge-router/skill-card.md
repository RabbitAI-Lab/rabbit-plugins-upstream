## Description:

Knowledge Router builds a lightweight routing layer across existing knowledge sources such as MEMORY.md, daily memory files, self-improving notes, skill references, and audit records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lethehades](https://clawhub.ai/user/lethehades)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to decide which local knowledge source to read first for a query, then generate a short routing report with primary sources, secondary sources, reasoning, and promotion hints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default-scope routing may preview local memory files, skill references, audit logs, and ~/self-improving notes.

Mitigation: Use narrower --scope values for sensitive workspaces or when a query only needs one knowledge layer.

Risk: The --output option writes to a caller-provided local path and could overwrite an important file.

Mitigation: Choose an explicit non-critical report path and review the target before writing output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lethehades/skills/knowledge-router)
- [source-types.md](artifact/references/source-types.md)
- [routing-rules.md](artifact/references/routing-rules.md)
- [promotion-rules.md](artifact/references/promotion-rules.md)
- [report-format.md](artifact/references/report-format.md)
- [release-minimal.md](artifact/references/release-minimal.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown routing report with source recommendations and promotion hints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report to a caller-provided local output path.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
