## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use pibox to run a coding agent in a container against a chosen workspace, or connect clients through its API, MCP, Telegram, and scheduled-run interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A containerized coding agent can read, modify, or delete files in its mounted workspace.

Mitigation: Mount only the intended workspace and review agent actions before use.

Risk: API and MCP services without tokens can expose agent execution and workspace access to anyone who can reach them.

Mitigation: Set separate non-empty API and MCP tokens, and bind services to localhost or protect them behind an authenticating proxy.

Risk: Unreviewed installation scripts, mutable container images, or public network exposure increase deployment risk.

Mitigation: Inspect the installer before running it, pin image versions or digests, and avoid host networking or public exposure without additional controls.

## Reference(s):

- [pibox on ClawHub](https://clawhub.ai/psyb0t/skills/pibox)
- [pibox setup guide](references/setup.md)
- [pibox project documentation](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent documentation](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with command and configuration examples; connected services can return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent runs may read or change files in the mounted workspace.]

## Skill Version(s):

0.20.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
