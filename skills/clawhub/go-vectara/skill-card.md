## Description:

Unofficial Go client for the Vectara API v2. Package vectara (github.com/psyb0t/go-vectara) has typed methods for corpora, documents, search, RAG queries, chats, agents, tools, pipelines and account administration. Use when Go code needs Vectara or already imports go-vectara.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that integrates with Vectara's API for corpus and document management, search and RAG queries, chats, agents, tools, pipelines, and account administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vectara credentials could be exposed or granted broader access than needed.

Mitigation: Use minimally scoped credentials, read secrets from environment or a secret manager, and never hardcode, commit, or log credentials or authentication headers.

Risk: Resource-changing operations or agent execution can affect account data, invoke configured tools, or consume account resources.

Mitigation: Run account changes only when explicitly authorized by the user, and review configured tools and expected resource use before agent execution.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-vectara)
- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)
- [Skill-declared project homepage](https://github.com/psyb0t/go-vectara)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
