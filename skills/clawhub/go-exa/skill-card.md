## Description:

Guides Go developers in using an unofficial Exa API client for web search, page contents, cited answers, and research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the unofficial go-exa client to a project and write calls for Exa search, page contents, cited answers, and research tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exa API credentials could be exposed in source code or logs.

Mitigation: Read the API key from EXA_API_KEY and never hardcode, commit, or log it.

Risk: Search queries, URLs, and answer prompts sent to Exa may contain private data.

Mitigation: Review requests before sending and exclude secrets and private data.

Risk: The Go client is unofficial and sends requests to an external service.

Mitigation: Confirm the client is suitable for the project before installing it and sending an API key or requests.

## Reference(s):

- [go-exa skill release](https://clawhub.ai/psyb0t/skills/go-exa)
- [Setup and API reference](references/setup.md)
- [go-exa Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-exa)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authenticated Exa API calls and response handling.]

## Skill Version(s):

0.1.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
