## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can add typed calls to Skyvern for starting and inspecting browser automation runs and managing related agents, sessions, profiles, credentials, scripts, schedules, and artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can include API credentials and sensitive browser instructions, URLs, credential references, or other data.

Mitigation: Read SKYVERN_API_KEY from the environment, never hardcode or log credentials or authenticated requests, and send only data needed for the requested task.

Risk: Starting Skyvern tasks, agents, or scripts can affect external websites and consume credits.

Mitigation: Authorize only the specific resources and actions requested, and run or change only resources owned by that task.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-skyvern project](https://github.com/psyb0t/go-skyvern)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.6.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
