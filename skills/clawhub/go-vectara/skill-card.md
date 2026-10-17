## Description:

Guides Go developers in using an unofficial typed client for Vectara API v2, including search, RAG queries, chats, agents, and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and operate the unofficial go-vectara client in Go applications, including authenticated retrieval, queries, and resource management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or bearer tokens could be exposed in source code or logs.

Mitigation: Use a minimally scoped credential and keep secrets and authentication headers out of source control and logs.

Risk: Mutating or administrative requests can change account data, while agent or tool execution may incur costs.

Mitigation: Run create, update, delete, reset, account-admin, and agent or tool operations only when explicitly intended.

## Reference(s):

- [go-vectara ClawHub release](https://clawhub.ai/psyb0t/skills/go-vectara)
- [go-vectara project homepage](https://github.com/psyb0t/go-vectara)
- [Setup and API usage reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for handling authentication, responses, pagination, and streaming]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
