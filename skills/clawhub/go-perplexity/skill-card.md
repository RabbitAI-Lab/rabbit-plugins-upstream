## Description:

Guides Go developers in using an unofficial typed client for Perplexity's API, including chat completions, search, embeddings, and agent operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and operate a Go client for Perplexity chat, search, embeddings, and other API endpoints in their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Perplexity API requests use a sensitive bearer key.

Mitigation: Keep the key in an environment variable or secret manager; do not commit, log, or expose it.

Risk: API calls can incur charges or create, update, or delete Perplexity resources.

Mitigation: Review account-changing call paths and make them only when the user requests them, on specified resources.

## Reference(s):

- [go-perplexity setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Perplexity API key; decoded-response methods do not support streaming.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
