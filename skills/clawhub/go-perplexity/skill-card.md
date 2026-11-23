## Description:

Unofficial Go client for the Perplexity REST API at https://api.perplexity.ai. Package perplexity (github.com/psyb0t/go-perplexity), generated with oapi-codegen from Perplexity's OpenAPI document, has one typed method per endpoint on the client from perplexity.NewClientWithResponses, covering Sonar chat completions (sync and async), web search, embeddings and contextualized embeddings, agents and their files, skills, decisions, models and usage analytics, with JSON bodies decoded into Go structs. Auth is a bearer API key set through a request editor. Use when Go code needs to call the Perplexity API or already imports go-perplexity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with Perplexity API endpoints, including Sonar chat, search, embeddings, and account operations, using typed Go client methods and setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign but has medium confidence because one local reference was unavailable to the partial scan.

Mitigation: Review the installation instructions and endpoint usage before installing if those details affect your decision.

Risk: Some API calls can incur charges or change account state, including creating, updating, or deleting skills and managing agent runs.

Mitigation: Make these calls only when requested and only for resources the user created or named.

Risk: Exposing a bearer API key can give others access to the associated Perplexity account.

Mitigation: Read the key from an environment variable such as PERPLEXITY_API_KEY; never hardcode, commit, log, or print request headers.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [go-perplexity source repository](https://github.com/psyb0t/go-perplexity)
- [Go package API reference](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-perplexity)
- [Publisher profile](https://clawhub.ai/user/psyb0t)

## Skill Output:

**Output Type(s):** [Go code, API calls, Shell commands, Configuration instructions, Technical guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and calls depend on the caller's project, API key, and request inputs.]

## Skill Version(s):

0.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
