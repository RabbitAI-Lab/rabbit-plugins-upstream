## Description:

Provides an unofficial, typed Go client for the Skyvern API to start and inspect browser automation tasks and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to integrate Go applications with Skyvern browser automation, including starting and inspecting tasks, agents, and runs. It provides setup guidance, typed client examples, and advice for handling responses and credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may send browser instructions, URLs, credential references, or other sensitive data to the selected Skyvern deployment.

Mitigation: Keep API keys in environment variables, never log authenticated requests, and send only data needed for the requested task.

Risk: Starting, cancelling, deleting, or changing Skyvern resources can affect external websites and consume service credits.

Mitigation: Perform these actions only when requested and only for resources owned by the task.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Source repository listed by the skill](https://github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples, shell commands, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
