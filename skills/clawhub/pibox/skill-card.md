## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use pibox to run pi-coding-agent in a workspace through its local wrapper or to connect it to HTTP, OpenAI-compatible, MCP, Telegram, and scheduled workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because its setup guidance includes an unverified remote installer, host-networked services, and mutable container images; no clear malicious intent was reported.

Mitigation: Review and verify the installer source and pin container images to verified digests before installation. For deployed services, review network exposure and authentication settings. Scanner coverage is incomplete and does not establish that the skill is safe.

## Reference(s):

- [Setup and configuration](references/setup.md)
- [pibox project homepage](https://github.com/psyb0t/docker-pibox)
- [Pi coding agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration instructions, Files]

**Output Format:** [Agent responses and workspace files in formats requested by the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command output, generated or edited workspace files, and configuration examples.]

## Skill Version(s):

0.21.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
