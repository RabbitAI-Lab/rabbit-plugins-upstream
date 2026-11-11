## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and operate the unofficial typed Skyvern API client for browser automation, including tasks, runs, agents, and related resources. It guides setup, authentication, endpoint lookup, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign but incomplete because three local references could not be resolved.

Mitigation: Review the referenced material or verify its absence before installation.

Risk: Authenticated requests may carry API keys and sensitive browser instructions or request data to Skyvern.

Mitigation: Load the API key from the environment, never log or commit it, and send only data needed for the requested task.

Risk: Starting Skyvern tasks, agents, or scripts can affect external websites and consume credits.

Mitigation: Run actions only when requested and only for resources owned by that task.

## Reference(s):

- [Project repository](https://github.com/psyb0t/go-skyvern)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Setup and reference](references/setup.md)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Go code and Markdown setup guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require Go 1.26.10 or newer and a Skyvern API key.]

## Skill Version(s):

0.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
