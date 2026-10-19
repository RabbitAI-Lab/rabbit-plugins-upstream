## Description:

Guides Go developers in using an unofficial typed client for Vectara API v2, including retrieval, RAG, chats, agents, and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add and operate the unofficial go-vectara client in Go projects, including Vectara search, document management, and RAG queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vectara credentials could be exposed in source code or logs.

Mitigation: Use environment variables or normal secret handling; never hardcode, commit, or log credentials or authentication headers.

Risk: Create, update, delete, reset, API-key, user, agent, and tool actions can change account data; queries and agent execution can consume resources or invoke tools.

Mitigation: Review these operations and run account-changing actions only when explicitly requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vectara project](https://github.com/psyb0t/go-vectara)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-vectara)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover authentication, API calls, and response handling.]

## Skill Version(s):

0.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
