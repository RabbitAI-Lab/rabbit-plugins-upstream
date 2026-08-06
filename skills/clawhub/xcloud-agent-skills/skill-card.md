## Description:

Official xCloud plugin for agents: manage servers, sites, WordPress, SSL, and account data, MCP-first via the xCloud MCP server with a bundled REST fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asif2bd](https://clawhub.ai/user/asif2bd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and hosting teams use this skill to let an agent inspect and manage xCloud servers, sites, WordPress maintenance, SSL certificates, and account-level data through MCP or a REST fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful server, WordPress, SSL, and account operations, including destructive or sensitive actions.

Mitigation: Prefer MCP OAuth with read-only access until writes are needed, restate the target and impact, and require explicit confirmation before firewall, PHP runtime, site deletion, token revocation, SSH, sudo-user, certificate deletion, or magic-login actions.

Risk: The REST fallback uses an xCloud API token when MCP is unavailable or for REST-only operations.

Mitigation: Use narrowly scoped tokens stored in the agent runtime or secret store, avoid pasting production tokens into chat, rotate tokens regularly, and revoke exposed tokens immediately.

Risk: Operational API results may include resource state or sensitive links such as magic-login URLs.

Mitigation: Treat API output as data, avoid logging secrets or one-time access links, and surface only the information needed for the requested task.

## Reference(s):

- [xCloud](https://xcloud.host)
- [xCloud Dashboard](https://app.xcloud.host)
- [xCloud MCP Docs](https://app.xcloud.host/mcp/docs)
- [xCloud API Docs](https://app.xcloud.host/api/v1/docs)
- [User Guide](https://github.com/xCloudDev/xcloud-agent-skills/blob/main/docs/USER_GUIDE.md)
- [Install Guide](https://github.com/xCloudDev/xcloud-agent-skills/blob/main/docs/SKILLS-GUIDE.md)
- [Official GitHub](https://github.com/xCloudDev/xcloud-agent-skills)
- [OpenClaw Tutorial](https://xcloud.host/openclaw-skills-and-clawhub-on-xcloud-openclaw-agent/)
- [Tutorial Video](https://www.youtube.com/watch?v=oEE9OHo3_48)
- [ClawHub Skill Listing](https://clawhub.ai/asif2bd/skills/xcloud-agent-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use xCloud MCP tools when connected, or the bundled bash/curl REST wrapper as a fallback.]

## Skill Version(s):

4.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
