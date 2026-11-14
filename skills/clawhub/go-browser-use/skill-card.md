## Description:

Writes Go code with go-browser-use (package browseruse, github.com/psyb0t/go-browser-use), an unofficial generated client for the Browser Use Cloud API v4. Use when a Go program creates or polls Browser Use agent runs, manages sessions, queues, workspaces, files, browsers, profiles, extensions or integrations, or when a project imports github.com/psyb0t/go-browser-use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Browser Use Cloud API v4 for agent runs, browser and session management, files, profiles, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had partial coverage because two local references could not be resolved.

Mitigation: Review the skill and its references before installing or using it.

Risk: Starting runs or browsers can incur charges, and cancellation, deletion, purging, sharing, uploads, or integration changes can affect account state.

Mitigation: Run only actions the user requested, set an appropriate run cost limit, and confirm account-changing operations before making them.

Risk: API keys, task contents, secret bindings, and presigned URLs can expose sensitive information if logged or sent to the wrong host.

Mitigation: Load credentials from a secret store, avoid logging sensitive values, and send presigned transfers through a separate client without forwarding the API key.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-browser-use)
- [Project page](https://github.com/psyb0t/go-browser-use)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-browser-use)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
