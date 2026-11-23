## Description:

Use when deploying, redeploying, or configuring the a2a-exposed Cloudflare Worker, a wake webhook, polling, or a public façade for an agent that already speaks A2A, or creating a hosted agent on a2a.exposed. Not for reading or replying to messages (use a2a-exposed).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to set up and configure hosted or self-hosted public A2A endpoints, including their wake delivery and polling options. It provides command and configuration guidance for confirming that an agent can receive and handle a real message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary marks this skill suspicious because it repeatedly uses unpinned packages and includes high-impact teardown guidance; the scan was partial.

Mitigation: Review the package source and commands before use, limit cloud permissions to the needed account and resources, and verify exact targets before teardown.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed-setup)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted MCP connector guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/mcp.md#hosted-connector)
- [Hosted inbox getting started](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Deployment guide](artifact/references/deploy.md)
- [Wake setup and delivery guide](artifact/references/wake.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may configure hosted services, Cloudflare resources, and protected secrets; secret values should remain in protected storage.]

## Skill Version(s):

0.8.75 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
