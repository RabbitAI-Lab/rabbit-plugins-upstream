## Description:

Unofficial typed Go client for the Skyvern API, with REST methods for automation tasks, agents, runs, browser sessions, credentials, scripts, schedules, artifacts, and audit exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and use the unofficial Go client in projects that need Skyvern browser automation, including starting and inspecting runs and managing related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests can carry browser instructions, URLs, credential references, and other sensitive data to the selected Skyvern deployment.

Mitigation: Keep the API key in the environment, send only data needed for the requested task, and select the deployment deliberately.

Risk: Starting tasks, agents, or scripts can interact with external websites and consume credits.

Mitigation: Run, cancel, delete, or change only resources the user requested and that belong to the task.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [go-skyvern project](https://github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and API usage guidance; generated client code is obtained through the Go module.]

## Skill Version(s):

0.6.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
