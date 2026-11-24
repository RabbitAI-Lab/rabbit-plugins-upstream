## Description:

Configure and operate Peen, the durable coding-agent backend. Use when setting up a provider and Docker workspace, sending work over WebSocket, adding project harness rules, or inspecting and controlling durable sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and configure Peen, open project workspaces, send and follow coding-agent tasks, and inspect or control retained sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance runs an installer from a mutable URL, and the security scan reports partial analysis and setup behavior outside declared permissions.

Mitigation: Verify and review the installer contents or use a trusted pinned release before running it; review user-level configuration changes and limit the workspace and credentials available to the agent.

## Reference(s):

- [Setup and use Peen](references/setup.md)
- [Project documentation](https://github.com/psyb0t/peen)
- [Deployment](https://github.com/psyb0t/peen/blob/main/docs/deployment.md)
- [Where Peen runs](https://github.com/psyb0t/peen/blob/main/docs/where-it-runs.md)
- [HTTP API reference](https://github.com/psyb0t/peen/blob/main/docs/http-api.md)
- [Configuration](https://github.com/psyb0t/peen/blob/main/docs/configuration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands, configuration examples, and API snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.51.0 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
