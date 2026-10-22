## Description:

Unofficial Go client for the xAI (Grok) REST API at https://api.x.ai. `xai.NewClientWithResponses` from `github.com/psyb0t/go-xai` gives one typed method per endpoint, generated with oapi-codegen from xAI's OpenAPI document - chat completions, the Responses API, Anthropic style messages, embeddings, tokenization, image and video generation, files, skills, document search, models and API key info - with JSON 200 bodies decoded into Go structs. Auth is a bearer API key set through a request editor. Use when Go code needs to call the xAI API or already imports go-xai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can follow this skill to add the go-xai package to a project and call xAI API endpoints through typed Go methods, including handling authentication and responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing an xAI API key could compromise the account.

Mitigation: Read the key from an environment variable; do not hardcode, commit, or log it, and do not print request headers.

Risk: API requests can incur costs or change account state, including uploads, deletions, and public sharing.

Mitigation: Consider costs and data sensitivity, and perform state-changing requests only when requested and only for specifically identified resources.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-xai package documentation](https://pkg.go.dev/github.com/psyb0t/go-xai)
- [xAI API](https://api.x.ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes typed Go usage examples and endpoint/error-handling guidance.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
