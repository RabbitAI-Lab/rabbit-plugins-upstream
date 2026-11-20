## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this unofficial typed client to call Skyvern APIs for browser automation, including starting and inspecting tasks and agents and managing related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request bodies may contain browser instructions, URLs, credential references, or other sensitive data.

Mitigation: Send only data needed for the requested task, and keep API keys and authenticated requests out of source control and logs.

Risk: Starting automation can interact with external websites and consume Skyvern credits.

Mitigation: Run, cancel, delete, or change resources only when the user requested the action and the resources belong to that task.

Risk: The security review is incomplete because three references in SKILL.md could not be resolved.

Mitigation: Review the unresolved references and install only if comfortable with the remaining uncertainty.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-skyvern source repository](https://github.com/psyb0t/go-skyvern)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Go toolchain and a Skyvern API key; the client does not poll runs or retry rate limits automatically.]

## Skill Version(s):

0.8.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
