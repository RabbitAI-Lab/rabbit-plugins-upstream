## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this client to call Skyvern APIs for browser automation, including starting and inspecting tasks, agents, runs, browser sessions, and related resources. It is an unofficial client and requires a Skyvern API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation requests may include sensitive data, interact with external websites, or consume credits.

Mitigation: Protect the Skyvern API key, send only data needed for the requested task, and run or change only resources the user requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Project repository](https://github.com/psyb0t/go-skyvern)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown setup and reference guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The client requires Go and a Skyvern API key; requests can start automation runs that interact with external websites.]

## Skill Version(s):

0.6.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
