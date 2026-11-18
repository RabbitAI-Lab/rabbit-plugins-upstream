## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this Go client to start and inspect Skyvern browser automation tasks and manage related agents, sessions, credentials, schedules, and artifacts. It suits Go projects that need Skyvern API access or already use go-skyvern.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found no issues in reviewed Markdown but could not resolve three references, so its confidence is medium.

Mitigation: Review the linked setup and dependency documentation, including any references that were unavailable during scanning.

Risk: Automation requests can include sensitive instructions or credential references, and starting runs can interact with websites or consume credits.

Mitigation: Keep API keys in environment variables, send only necessary request data, and start or change only resources requested by the user.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-skyvern repository](https://github.com/psyb0t/go-skyvern)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Skyvern API requests require a configured deployment and API key.]

## Skill Version(s):

0.8.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
