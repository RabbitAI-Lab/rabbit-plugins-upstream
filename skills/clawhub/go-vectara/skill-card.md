## Description:

Unofficial Go client for the Vectara API v2. Package vectara (github.com/psyb0t/go-vectara) has typed methods for corpora, documents, search, RAG queries, chats, agents, tools, pipelines and account administration. Use when Go code needs Vectara or already imports go-vectara.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add and use the unofficial Go Vectara client in Go projects for Vectara corpus, document, search, RAG, chat, agent, tool, pipeline, and account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review coverage was partial, so the clean verdict does not guarantee safety.

Mitigation: Review the release and resolve or check the local references that were outside scanner coverage before relying on it.

Risk: VECTARA_API_KEY or other authentication credentials could be exposed if placed in source code, logs, or committed configuration.

Mitigation: Read credentials from the environment, keep them out of source and logs, and send them only in the required authentication header.

Risk: Create, update, delete, and reset operations can change Vectara account data; queries and agent execution can consume account resources or invoke configured tools.

Mitigation: Run mutating operations only when requested, and review the operation and its account or tool effects before execution.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)
- [Go module repository](https://github.com/psyb0t/go-vectara)

## Skill Output:

**Output Type(s):** [Code, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code with Markdown guidance, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the Go Vectara client; credentials are supplied by the caller.]

## Skill Version(s):

0.3.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
