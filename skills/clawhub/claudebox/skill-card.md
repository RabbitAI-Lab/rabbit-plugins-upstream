## Description:

claudebox helps agents install, configure, launch, and script a Docker-hosted Claude Code environment through CLI, HTTP, OpenAI-compatible, MCP, Telegram, and cron interfaces, with optional bearer-token authentication for exposed server modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and operate claudebox as a containerized Claude Code wrapper or service endpoint. It supports interactive sessions, scripted one-shot execution, HTTP and OpenAI-compatible APIs, MCP tool access, Telegram workflows, and scheduled cron jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server modes can be unauthenticated when their per-mode tokens are unset.

Mitigation: Set API and MCP bearer tokens before enabling server modes, and bind services to trusted networks or place them behind an authenticating proxy.

Risk: The containerized Claude Code runtime can have broad local authority, especially when Docker access or host paths are mounted.

Mitigation: Use claudebox only for intended self-hosted Claude Code workloads, avoid mounting /var/run/docker.sock unless necessary, and isolate the container when handling untrusted input.

Risk: The documented quick installer can run a downloaded shell script with local user privileges.

Mitigation: Download and inspect the installer before running it, especially in agent-driven or CI environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox)
- [claudebox setup](references/setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON/API examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker, HTTP API, OpenAI-compatible API, MCP, Telegram, and cron examples.]

## Skill Version(s):

2.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
