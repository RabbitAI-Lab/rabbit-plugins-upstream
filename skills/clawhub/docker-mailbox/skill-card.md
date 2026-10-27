## Description:

Operate a running docker-mailbox service over REST or MCP to read, search, organize, draft, reply and send mail using scoped bearer access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to operate a configured docker-mailbox instance through REST or MCP for authorized mailbox reading, search, organization, drafts, replies, and sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When the optional Cloudflare tunnel is enabled, Cloudflare can access proxied email traffic and bearer tokens.

Mitigation: Keep access local unless remote access is needed; if using the tunnel, account for Cloudflare's access to proxied traffic and tokens.

Risk: Configuration files and unpinned container images can expose credentials or reduce deployment integrity.

Mitigation: Protect configuration files and prefer a pinned image digest.

## Reference(s):

- [Setup and deployment guide](artifact/references/setup.md)
- [REST and MCP API guide](artifact/references/api.md)
- [Project homepage](https://github.com/psyb0t/docker-mailbox)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with REST/MCP examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific operational instructions and examples; does not itself perform mailbox operations.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
