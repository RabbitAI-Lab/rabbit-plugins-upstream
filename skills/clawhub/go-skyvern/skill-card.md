## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External developers use this skill to add or use the unofficial Go client in a Go project that needs to start, inspect, or manage Skyvern browser automation and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and request bodies may contain sensitive information sent to Skyvern.

Mitigation: Read the API key from the environment, never log credentials or authenticated requests, and send only the data needed for the requested task.

Risk: Automation can interact with external websites and consume credits or change Skyvern resources.

Mitigation: Authorize only the requested actions and resources owned by that task; use a staging or self-hosted deployment only when explicitly selected.

Risk: This is an unofficial client, and external module code was outside the security review.

Mitigation: Review and pin the Go dependency before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-skyvern)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance are selected for the requested Skyvern API operation.]

## Skill Version(s):

0.6.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
