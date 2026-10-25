## Description:

Guides Go developers in using the unofficial typed Together AI REST API client, including authentication and endpoint responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can install and integrate the typed Together AI client to call API endpoints, configure bearer authentication, and inspect typed responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Together AI API key could be committed, logged, or disclosed in request headers.

Mitigation: Read the key from an environment variable such as TOGETHER_API_KEY; do not hardcode, commit, log, or print request headers.

Risk: Prompts and files sent in API requests are processed by Together AI.

Mitigation: Send only data intended for Together AI processing and retain the documented Together AI base URL.

Risk: Fine-tuning jobs and dedicated endpoints or clusters can incur charges; delete operations remove data.

Mitigation: Request paid resource creation or deletion only when explicitly authorized.

Risk: An unpinned Go dependency version may change between builds.

Mitigation: Review and pin the Go dependency version.

## Reference(s):

- [Setup guide](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-togetherai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-togetherai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Go toolchain; covers bearer-token setup and typed API request and response handling.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
