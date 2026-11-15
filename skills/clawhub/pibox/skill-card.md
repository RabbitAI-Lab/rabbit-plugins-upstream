## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use pibox to run pi-coding-agent in a workspace interactively or for one-off tasks, and to expose it through HTTP, OpenAI-compatible, MCP, Telegram, or scheduled interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guide installs a host wrapper by piping a remote installer directly to a shell.

Mitigation: Review the installer and verify its source before running it on the host.

Risk: Examples use mutable container image tags and host networking.

Mitigation: Pin a reviewed image digest and restrict network exposure to the required interfaces and ports.

Risk: An unset API or MCP token leaves the corresponding agent and workspace access unauthenticated.

Mitigation: Set explicit API and MCP bearer tokens and limit access to trusted clients.

Risk: A Telegram bot with an empty or missing chat allowlist responds to every chat.

Mitigation: Configure and verify an explicit allowed_chats list before enabling the bot.

## Reference(s):

- [Setup and configuration guide](artifact/references/setup.md)
- [pibox project homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox container project](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with inline shell commands, configuration examples, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage depends on Docker, a configured LLM endpoint, and a target workspace.]

## Skill Version(s):

0.21.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
