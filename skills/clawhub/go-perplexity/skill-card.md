## Description:

Unofficial Go client for the Perplexity REST API at https://api.perplexity.ai. Package perplexity (github.com/psyb0t/go-perplexity), generated with oapi-codegen from Perplexity's OpenAPI document, has one typed method per endpoint on the client from perplexity.NewClientWithResponses, covering Sonar chat completions (sync and async), web search, embeddings and contextualized embeddings, agents and their files, skills, decisions, models and usage analytics, with JSON bodies decoded into Go structs. Auth is a bearer API key set through a request editor. Use when Go code needs to call the Perplexity API or already imports go-perplexity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Perplexity APIs, including Sonar chat, search, embeddings, and agent endpoints. It guides installation, client configuration, authentication, endpoint selection, and response/error handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party Go dependency may change or introduce unwanted behavior.

Mitigation: Review the dependency and pin the version used by the project.

Risk: API credentials or sensitive request content could be exposed through application handling or API requests.

Mitigation: Keep the API key private, avoid logging request headers, and consider what data is sent to Perplexity.

Risk: Perplexity API calls may incur charges or change account state.

Mitigation: Make paid or account-changing calls only when requested and only for resources the task created or named.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-perplexity source repository](https://github.com/psyb0t/go-perplexity)
- [go-perplexity package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
