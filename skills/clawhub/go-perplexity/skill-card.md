## Description:

Unofficial Go client for the Perplexity REST API at https://api.perplexity.ai. Package perplexity (github.com/psyb0t/go-perplexity), generated with oapi-codegen from Perplexity's OpenAPI document, has one typed method per endpoint on the client from perplexity.NewClientWithResponses, covering Sonar chat completions (sync and async), web search, embeddings and contextualized embeddings, agents and their files, skills, decisions, models and usage analytics, with JSON bodies decoded into Go structs. Auth is a bearer API key set through a request editor. Use when Go code needs to call the Perplexity API or already imports go-perplexity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate Go applications with Perplexity's API, including Sonar chat, search, embeddings, agents, skills, decisions, and usage analytics. It provides typed Go client guidance, setup commands, and API-key configuration examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial Go dependency may change or introduce supply-chain risk.

Mitigation: Review and pin the dependency before adding it to a project.

Risk: API keys can be exposed if embedded in source code, committed, or logged.

Mitigation: Load the key from an environment variable and never commit it or log request headers.

Risk: API calls may incur charges or change account state.

Mitigation: Use the official Perplexity API URL and make paid or account-changing calls only when requested, specifying the resources involved.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-perplexity)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands to add, build, or test the Go dependency; live API requests require a user-provided API key.]

## Skill Version(s):

0.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
