## Description:

Unofficial Go client for the Vectara API v2 with typed methods for corpora, documents, search, RAG queries, chats, agents, tools, pipelines, and account administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers working in Go use this skill to integrate Vectara API v2 for corpora, documents, search and RAG, chats, agents, tools, pipelines, and account administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vectara credentials can grant access to account resources, and account changes can alter or delete data.

Mitigation: Use credentials limited to the required resources and operations; perform account changes only when the user requests them.

Risk: Queries and agent execution may incur costs or invoke configured tools.

Mitigation: Confirm the requested query or agent action and its expected account impact before running it.

Risk: OAuth use adds a connection to auth.vectara.io.

Mitigation: Allow that endpoint only when OAuth is needed, and keep token acquisition and renewal under the caller's control.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)
- [Project repository](https://github.com/psyb0t/go-vectara)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration examples and guidance; the skill does not generate files itself.]

## Skill Version(s):

0.2.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
