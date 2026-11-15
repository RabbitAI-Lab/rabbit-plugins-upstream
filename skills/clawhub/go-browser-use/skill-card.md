## Description:

Writes Go code with go-browser-use (package browseruse, github.com/psyb0t/go-browser-use), an unofficial generated client for the Browser Use Cloud API v4. Use when a Go program creates or polls Browser Use agent runs, manages sessions, queues, workspaces, files, browsers, profiles, extensions or integrations, or when a project imports github.com/psyb0t/go-browser-use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go integrations with Browser Use Cloud API v4 for agent runs, sessions, queues, workspaces, files, browser sessions, profiles, extensions, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports partial Skillspector coverage because two local references were unresolved, with medium overall confidence.

Mitigation: Review the available setup guidance and consider whether you trust and need the Browser Use API integration before installing.

Risk: Starting runs or browsers can incur charges, and cancellation, deletion, purging, sharing, uploads, or integration changes can affect account state.

Mitigation: Use cost limits where appropriate and perform paid or state-changing actions only when requested.

Risk: API keys, task contents, secret bindings, CDP URLs, and presigned URLs may expose sensitive information if logged or sent to the wrong host.

Mitigation: Load credentials from the caller’s secret store, avoid logging sensitive values, and keep API keys off storage-host transfer requests.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Source repository](https://github.com/psyb0t/go-browser-use)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-browser-use)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-browser-use)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go source code and Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Integration details vary by the requested API operation.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
