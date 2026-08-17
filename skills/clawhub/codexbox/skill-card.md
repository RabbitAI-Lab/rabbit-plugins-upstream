## Description:

codexbox packages OpenAI Codex CLI in a Docker-based service so developers can run Codex through shell, HTTP, OpenAI-compatible chat, MCP, Telegram, or cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install, configure, and operate Codex through Docker-backed service surfaces instead of only a local terminal. It is useful for scripted runs, CI jobs, OpenAI-compatible clients, MCP-aware agents, Telegram workflows, cron automation, and workspace file operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTP API or MCP services can provide run execution and workspace file access if exposed without tokens.

Mitigation: Set CODEXBOX_API_MODE_TOKEN and CODEXBOX_MCP_MODE_TOKEN before exposing ports, and bind services to localhost or place them behind an authenticated proxy.

Risk: The installer can execute remote shell code if run directly from a pipe.

Mitigation: Download the installer, inspect it, and then run it only when the source and channel are trusted.

Risk: File deletion, scheduled runs, Telegram access, and mounted auth/session directories can affect workspace data or credentials.

Mitigation: Limit enabled modes to the intended workflow, restrict who can call them, and treat mounted workspace and auth directories as sensitive.

## Reference(s):

- [codexbox ClawHub page](https://clawhub.ai/psyb0t/skills/codexbox)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [codexbox setup](references/setup.md)
- [codexbox project homepage](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API request examples]

**Output Format:** [Markdown with inline shell, JSON, YAML, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational setup steps, environment variables, endpoint examples, and security cautions.]

## Skill Version(s):

0.5.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
