## Description:

Writes Go code with go-browser-use (package browseruse, github.com/psyb0t/go-browser-use), an unofficial generated client for the Browser Use Cloud API v4, for programs that create or poll agent runs and manage sessions, queues, workspaces, files, browsers, profiles, extensions, or integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go integrations with the unofficial Browser Use Cloud API v4 client, including agent runs, sessions, workspaces, files, browsers, profiles, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser Use API keys, task contents, secret bindings, and presigned URLs could be exposed through code or logs.

Mitigation: Load credentials from the caller's environment or secret store, restrict secret access, and never hardcode or log credentials or sensitive task data.

Risk: Starting runs or browsers can incur charges, and cancellation, deletion, purging, sharing, uploads, or integration changes affect account state.

Mitigation: Limit costs and perform account-changing actions only when the user requested them.

Risk: The package is an unofficial generated client, and the assessment does not cover downloaded library code or unbundled upstream examples.

Mitigation: Review and pin the dependency before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-browser-use on GitHub](https://github.com/psyb0t/go-browser-use)
- [go-browser-use on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-browser-use)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go integration guidance for the Browser Use Cloud API v4 client]

## Skill Version(s):

0.1.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
