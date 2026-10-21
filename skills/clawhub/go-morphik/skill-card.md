## Description:

Guides Go developers using the unofficial go-morphik client for Morphik document ingestion, management, retrieval, and queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the unofficial Morphik client into projects that ingest, find, retrieve, or query documents and inspect related models and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Morphik API key could be exposed in source code, logs, or requests to an unintended service.

Mitigation: Keep the key in an environment variable, avoid logging authorization headers, and confirm the Morphik base URL before sending credentials.

Risk: Document ingestion or deletion can transfer sensitive content or change remote state.

Mitigation: Use only user-approved documents and task-owned resources; review ingestion and deletion operations before running them.

## Reference(s):

- [go-morphik setup and reference](references/setup.md)
- [go-morphik package documentation](https://pkg.go.dev/github.com/psyb0t/go-morphik)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-morphik)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go projects need the Go toolchain and a Morphik API key for authenticated operations.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
