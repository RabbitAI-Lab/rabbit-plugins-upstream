## Description:

pibox helps agents and developers operate pi-coding-agent through Docker-based shell, REST, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to choose, configure, and call the appropriate pibox interface for scripted coding-agent runs, remote MCP access, OpenAI-compatible clients, Telegram workflows, or scheduled maintenance tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A mutable third-party Docker image can change between installs while receiving credentials and writable workspace access.

Mitigation: Use a trusted publisher, pin the image by digest, and mount only the smallest workspace needed for the task.

Risk: API and MCP services can be exposed without authentication when their bearer-token environment variables are unset.

Mitigation: Set both API and MCP tokens, bind services to localhost, or place them behind an authenticated proxy before exposing them to a network.

Risk: Delete, cancel, and scheduled cron behavior can remove or disrupt workspace state.

Mitigation: Treat destructive and scheduled operations as admin-only, require explicit user confirmation for the exact target, and avoid bulk deletion patterns.

## Reference(s):

- [pibox ClawHub page](https://clawhub.ai/psyb0t/skills/pibox)
- [Setup reference](references/setup.md)
- [pibox homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [docker-aicodebox](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, YAML, shell commands, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for configuring or invoking a remote coding-agent container and may include endpoint, token, workspace, model, and scheduling details.]

## Skill Version(s):

0.15.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
