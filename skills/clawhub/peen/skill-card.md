## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and configure Peen, connect coding-agent workspaces to a provider, and send, monitor, inspect, or resume durable agent sessions. It also guides setup of project instructions and harness rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup command pipes an installer fetched from a changeable online source into a shell, where it runs with the installer's account privileges.

Mitigation: Review the installer from a source you trust before running it, and use a pinned, verified release when one is available.

## Reference(s):

- [Setup, providers, WebSocket, and REST](references/setup.md)
- [Peen project homepage](https://github.com/psyb0t/peen)
- [Deployment documentation](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [Configuration documentation](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)
- [HTTP API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)
- [Agent session recovery](https://github.com/psyb0t/peen/blob/main/docs/agents.md#recovery-after-a-crash)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown instructions with shell commands, configuration examples, JSON, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for the user's Peen installation and workspace.]

## Skill Version(s):

0.50.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
