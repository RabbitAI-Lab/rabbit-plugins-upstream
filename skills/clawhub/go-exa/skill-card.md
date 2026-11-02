## Description:

Provides a typed Go client for Exa's web search, content retrieval, cited answers, and research task APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add Exa search, similar-page discovery, page content retrieval, cited answers, and research tasks to Go applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exa API keys could be exposed if they are hardcoded, committed, or logged.

Mitigation: Read the key from EXA_API_KEY and keep it out of source code, commits, and logs.

Risk: Search queries, URLs, and answer prompts are sent to Exa and could disclose private information.

Mitigation: Do not include secrets or private data in requests to the Exa API.

Risk: API calls incur charges, and research tasks can take longer and cost more.

Mitigation: Consider the account charges before making requests and start research tasks only when requested.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [go-exa package documentation](https://pkg.go.dev/github.com/psyb0t/go-exa)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the Go exa package and EXA_API_KEY environment variable.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
