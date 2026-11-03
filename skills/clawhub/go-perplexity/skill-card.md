## Description:

Unofficial Go client for the Perplexity REST API, providing typed methods for chat completions, search, embeddings, agents, skills, decisions, models, and usage analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or work with a typed Go client for Perplexity API endpoints, including guidance for authentication, requests, response handling, and errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests send their inputs to Perplexity, may incur charges, and some endpoints can change account state.

Mitigation: Keep the API key out of code and logs, review and pin the external Go dependency, and authorize account-changing calls only for intended resources.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [Project homepage](https://github.com/psyb0t/go-perplexity)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes endpoint, authentication, response, and error handling guidance.]

## Skill Version(s):

0.3.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
