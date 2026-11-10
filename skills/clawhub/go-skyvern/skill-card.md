## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can integrate with Skyvern to start and inspect browser automation tasks, agents, runs, sessions, and related resources through typed API methods. Use this skill when a Go project needs Skyvern API access or already imports go-skyvern.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review has medium confidence and partial coverage; three local references could not be resolved.

Mitigation: Review the setup and referenced material before installing if you need stronger assurance.

Risk: Authenticated requests can carry sensitive automation instructions and data, and starting tasks can affect external sites or consume credits.

Mitigation: Read the API key from the environment, never hardcode or log it, send only task-required data, and run or change resources only when requested for resources owned by that task.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [go-skyvern project page](https://github.com/psyb0t/go-skyvern)
- [Skyvern API key settings](https://app.skyvern.com/settings)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, configuration instructions, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a Skyvern API key and Go toolchain; API requests and automation actions depend on the caller.]

## Skill Version(s):

0.8.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
