## Description:

Unofficial Go client for the Perplexity REST API at https://api.perplexity.ai.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use the skill to install and integrate a typed client for the Perplexity API, including Sonar chat, web search, embeddings, agents, and other documented endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because a path-like reference in the skill was reported missing, so some evidence may not have been reviewed.

Mitigation: Review the referenced material and confirm the path before installing.

Risk: The security summary reports a tool misuse concern in an API method listing, and the guidance calls out the DELETE endpoint description for review.

Mitigation: Review the DELETE method before use; only make state-changing calls when requested and only for resources the task created or named.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-perplexity)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, API usage guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes setup and endpoint usage guidance; API requests require a Perplexity API key.]

## Skill Version(s):

0.6.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
