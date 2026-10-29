## Description:

Unofficial Go client for the Vectara API v2. Package vectara (github.com/psyb0t/go-vectara) has typed methods for corpora, documents, search, RAG queries, chats, agents, tools, pipelines and account administration. Use when Go code needs Vectara or already imports go-vectara.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can use this skill to integrate Vectara API v2 operations into a project through the go-vectara client. It guides installation, authentication, endpoint and response handling, pagination, streaming, and safe use of account-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials used for Vectara requests could be exposed if they are hardcoded, committed, or logged.

Mitigation: Read credentials from an environment variable, use credentials limited to needed operations, and never log authentication headers.

Risk: The Go dependency is unofficial and fetched separately from the skill release.

Mitigation: Review and pin a dependency version before adding or upgrading it.

Risk: Creating, updating, deleting, or resetting resources changes account data; queries and agent execution can consume resources or invoke configured tools.

Mitigation: Run account-changing operations only when requested, and review requested account changes carefully.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vectara package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)
- [Project homepage](https://github.com/psyb0t/go-vectara)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-vectara)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
