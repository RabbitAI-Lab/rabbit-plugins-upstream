## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Skyvern by installing the typed client, configuring API authentication, and calling documented Skyvern operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skyvern requests may transmit sensitive data and can interact with external websites or consume credits.

Mitigation: Use a trusted deployment, protect the API key, send only data needed for the task, and authorize specific actions.

Risk: The Go client is unofficial, and its implementation and referenced upstream files are outside this artifact review.

Mitigation: Review and pin the dependency before deployment.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Project repository (listed homepage)](https://github.com/psyb0t/go-skyvern)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.7.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
