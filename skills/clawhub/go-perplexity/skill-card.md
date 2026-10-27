## Description:

Provides a typed Go client and usage guidance for Perplexity API endpoints, including Sonar, search, embeddings, agents, skills, decisions, models and usage analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install and integrate a typed Perplexity API client for chat, search, embeddings and other supported endpoints. They can also use it to inspect endpoint types, handle responses and configure bearer authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Go dependency may introduce supply chain risk.

Mitigation: Review and pin the third-party Go dependency before use.

Risk: Requests may expose sensitive data to Perplexity, and API credentials could be exposed if mishandled.

Mitigation: Consider what data is sent, read the API key from an environment variable, and do not hardcode, commit or log it.

Risk: Some API calls incur charges or change account state.

Mitigation: Make paid or account-changing calls only when requested, and scope them to resources created or named by the user.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [Perplexity API](https://api.perplexity.ai)
- [Project homepage](https://github.com/psyb0t/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
