## Description:

Writes Go code with go-browser-use (package browseruse, github.com/psyb0t/go-browser-use), an unofficial generated client for the Browser Use Cloud API v4. Use when a Go program creates or polls Browser Use agent runs, manages sessions, queues, workspaces, files, browsers, profiles, extensions or integrations, or when a project imports github.com/psyb0t/go-browser-use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go integrations with Browser Use Cloud API v4, including agent runs, sessions, workspaces, files, browser sessions, profiles, extensions, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted tasks, uploaded files, and supplied secret bindings go to Browser Use or its storage provider.

Mitigation: Share only task-authorized data, scope secret bindings to the task, and never log credentials or sensitive task content.

Risk: Runs and browser sessions can incur charges, while cancellation, deletion, purging, sharing, uploads, and integration changes affect account state.

Mitigation: Account for cloud usage charges and perform account-changing actions only when requested by the user.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-browser-use)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-browser-use)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-browser-use)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
