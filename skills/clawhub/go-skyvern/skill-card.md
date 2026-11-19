## Description:

Provides an unofficial typed Go client for Skyvern API automation, including tasks, agents, runs, browser sessions, credentials, scripts, schedules, artifacts, and audit exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Skyvern by installing the unofficial typed client, configuring API authentication, and choosing the documented methods for tasks, agents, runs, browser sessions, and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and sensitive request data could be exposed through application code or logs.

Mitigation: Read SKYVERN_API_KEY from the environment, and do not hardcode, commit, or log credentials or authenticated requests. Send only the data needed for the requested task.

Risk: Starting Skyvern tasks, agents, or scripts can interact with external websites and consume credits.

Mitigation: Run, cancel, delete, or change resources only when requested, and only for resources owned by that task.

Risk: The security scan was partial and left three local references unresolved, so its clean result does not establish that every related file or behavior was assessed.

Mitigation: Review the unresolved references and related behavior when evaluating the scan coverage.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Project repository](https://github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples include client setup, API authentication, method selection, and response handling.]

## Skill Version(s):

0.8.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
