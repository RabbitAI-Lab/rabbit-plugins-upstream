## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install, configure, and run Claude Code through the claudebox wrapper, or connect to its optional HTTP, MCP, Telegram, and scheduled-job interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default wrapper bypasses Claude permission prompts and can grant access beyond the selected project, including control of the host Docker daemon.

Mitigation: Use a disposable VM or deployment without the host Docker socket for untrusted work, and review a pinned installer and wrapper before execution.

Risk: API or MCP services may have no authentication when their mode tokens are unset; Telegram access may also be too broad.

Mitigation: Set separate API and MCP tokens and configure Telegram chat allowlists before enabling or exposing these services.

## Reference(s):

- [Setup guide](references/setup.md)
- [Claudebox project homepage](https://github.com/psyb0t/docker-claudebox)
- [Wrapper behavior](https://github.com/psyb0t/docker-claudebox/blob/master/docs/wrapper.md)
- [API mode documentation](https://github.com/psyb0t/docker-claudebox/blob/master/docs/modes/api.md)
- [MCP mode documentation](https://github.com/psyb0t/docker-claudebox/blob/master/docs/modes/mcp.md)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/claudebox)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup instructions and examples for local use and optional service modes.]

## Skill Version(s):

2.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
