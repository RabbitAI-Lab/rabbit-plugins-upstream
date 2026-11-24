## Description:

Unofficial Go client for the Vectara API v2 with typed methods for corpora, documents, search, RAG queries, chats, agents, tools, pipelines and account administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the Vectara API v2 through the go-vectara package. It provides installation, authentication, endpoint, pagination and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth setup may contact auth.vectara.io, outside the declared api.vectara.io network scope.

Mitigation: Review and allow the authentication host in your network policy before using OAuth; keep the API host and OAuth token host in the configuration scope you approve.

Risk: The security analysis is partial because two local references could not be resolved.

Mitigation: Review the unresolved references and relevant skill content before installation.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-vectara)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
