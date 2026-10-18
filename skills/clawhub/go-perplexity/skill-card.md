## Description:

Guides Go developers in using an unofficial typed client for Perplexity chat, search, embeddings, and other API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go client to a project and write typed Perplexity API calls, including chat completions, web search, and embeddings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party Go module introduces dependency risk.

Mitigation: Review and trust the module before adding it to a project.

Risk: Exposing the Perplexity API key could allow unauthorized API use.

Mitigation: Provide the key through an environment variable; do not hardcode, commit, or log it.

Risk: Some API calls incur charges or change account resources, including skill deletion and agent cancellation.

Mitigation: Confirm user intent and the target resource before making chargeable or account-changing calls.

## Reference(s):

- [go-perplexity setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [go-perplexity source repository](https://github.com/psyb0t/go-perplexity)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the Go toolchain and require a Perplexity API key for live requests.]

## Skill Version(s):

0.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
