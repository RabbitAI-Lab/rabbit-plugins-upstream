## Description:

Writes Go code with go-browser-use (package browseruse, github.com/psyb0t/go-browser-use), an unofficial generated client for the Browser Use Cloud API v4. Use when a Go program creates or polls Browser Use agent runs, manages sessions, queues, workspaces, files, browsers, profiles, extensions or integrations, or when a project imports github.com/psyb0t/go-browser-use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Go integrations with Browser Use Cloud API v4 for runs, sessions, workspaces, browsers, files, profiles, and integrations. It guides setup, authentication, generated method selection, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task contents and uploaded files may be sent to Browser Use Cloud and its storage provider.

Mitigation: Tell users what data may leave their environment, limit uploads to approved content, and avoid logging credentials, task contents, secret bindings, CDP URLs, or presigned URLs.

Risk: Security analysis was partial because two local path-like references were unresolved.

Mitigation: Review the unresolved references and the skill's cloud data handling before installing or using it.

Risk: Starting runs or browsers can incur charges, and account-changing operations can cancel, delete, purge, share, upload, or alter integrations.

Mitigation: Set an appropriate cost limit and perform account-changing actions only when requested by the user.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-browser-use source repository](https://github.com/psyb0t/go-browser-use)
- [go-browser-use package documentation](https://pkg.go.dev/github.com/psyb0t/go-browser-use)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
