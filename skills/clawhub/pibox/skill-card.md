## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use pibox to run the pi-coding-agent in a project workspace for interactive or one-shot coding tasks, or to connect automation through its HTTP, OpenAI-compatible, MCP, Telegram, and cron interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API or MCP service with an empty access token can allow reachable clients to run the agent and access workspace files.

Mitigation: Set distinct, nonempty API and MCP tokens, and bind services to loopback or place them behind an authenticated proxy before enabling remote access.

Risk: Project content may be sent to the configured upstream language-model provider, and broad workspace mounts can expose unintended files.

Mitigation: Choose an approved provider and mount only the intended project workspace.

Risk: Telegram access and persistent scheduled jobs can trigger agent activity beyond an interactive session.

Mitigation: Configure Telegram allowlists and review persistent startup scripts and scheduled jobs before enabling them.

## Reference(s):

- [Setup and configuration guide](references/setup.md)
- [pibox project](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox container project](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [Text, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell-command examples; downstream agent output depends on the requested task.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-dependent; running the agent may read or modify files in the mounted workspace.]

## Skill Version(s):

0.20.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
