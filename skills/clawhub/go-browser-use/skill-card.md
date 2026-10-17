## Description:

Guides Go developers in using an unofficial client for Browser Use Cloud API v4 to manage runs, sessions, browsers, files, and integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to build and test integrations with Browser Use Cloud API v4 for agent runs, sessions, browsers, workspaces, files, profiles, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, task contents, CDP URLs, or presigned URLs could be exposed through logs or forwarded to storage hosts.

Mitigation: Use a scoped API key from a secret store, avoid logging sensitive values, and use a separate client for presigned file transfers.

Risk: Starting paid runs or browsers, deleting data, uploading or sharing files, or changing integrations can affect account state or incur charges.

Mitigation: Review these actions before execution and perform them only when the user requests them.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go client repository](https://github.com/psyb0t/go-browser-use)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-browser-use)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
