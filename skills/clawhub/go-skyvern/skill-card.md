## Description:

Unofficial Go client generated from Skyvern's published OpenAPI document, with typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to add and call the unofficial Skyvern API client for browser automation tasks, agents, runs, sessions, and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skyvern requests can contain sensitive browser instructions, URLs, credential references, and other data.

Mitigation: Keep the API key in the environment, never hardcode, commit, or log it, and send only data needed for the task.

Risk: Starting automation can interact with external websites and consume credits.

Mitigation: Run, cancel, delete, or change only resources owned by the task and only when requested; use the intended Skyvern deployment.

Risk: The security review was marked partial and does not guarantee zero risk.

Mitigation: Review the skill and its permissions before use.

## Reference(s):

- [Setup and Reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Go toolchain and a Skyvern API key supplied through the environment.]

## Skill Version(s):

0.8.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
