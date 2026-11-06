## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill in Go projects to install and work with the unofficial go-skyvern client for Skyvern API tasks, agents, runs, browser sessions, and related resources. It provides guidance for authentication, endpoint methods, and handling responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skyvern requests can include browser instructions, URLs, credential references, and other sensitive data.

Mitigation: Send only the data needed for the requested task, read the API key from the environment, and never hardcode, commit, or log credentials or authenticated requests.

Risk: Starting automation tasks, agents, or scripts can interact with external websites and consume credits.

Mitigation: Run, cancel, delete, or change resources only when requested, and limit actions to resources owned by the task.

Risk: The downloaded Go module and referenced upstream files are outside this bundle's review.

Mitigation: Review and pin the dependency version before production use.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-skyvern)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, API Calls]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and guidance for authentication, endpoint use, and response handling.]

## Skill Version(s):

0.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
