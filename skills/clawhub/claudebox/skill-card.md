## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use claudebox to run Claude Code inside a Docker-backed wrapper for interactive sessions, scripted jobs, HTTP or OpenAI-compatible service access, MCP tool use, Telegram bots, and cron jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Powerful local agent container with broad shell, file, and Docker access may cause unintended changes if exposed to untrusted prompts or users.

Mitigation: Use claudebox only for trusted workloads, isolate the container when handling untrusted input, and review the requested workspace and permissions before execution.

Risk: API and MCP server modes can be unauthenticated when their bearer tokens are unset.

Mitigation: Set strong API and MCP tokens, bind services to localhost, or place them behind an authenticated proxy before any network exposure.

Risk: Mounting /var/run/docker.sock gives the container host-level container control.

Mitigation: Avoid mounting the Docker socket unless the workload requires it, and only enable it on a trusted host.

Risk: Downloaded installers, container images, cron jobs, init hooks, SSH state, always-active skills, and extra mounts can expand the skill's effective authority.

Mitigation: Pin and verify installers or images where possible, inspect downloaded scripts before running them, and review cron, init hook, SSH, always-active skill, and mount configuration before use.

## Reference(s):

- [Setup guide](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-claudebox)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, JSON examples, and API call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to run local commands, start services, edit files, call HTTP or MCP endpoints, and configure environment variables.]

## Skill Version(s):

2.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
