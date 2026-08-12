## Description:

Official xCloud plugin for agents that manages servers, sites, WordPress, SSL, and account data through the xCloud MCP server, with a bundled REST fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asif2bd](https://clawhub.ai/user/asif2bd)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, hosting operators, and agent users use this skill to connect agents to xCloud accounts, inspect hosting resources, and perform server, site, WordPress, SSL, and account operations via MCP or a REST fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent manage hosting resources and perform destructive actions when the user grants write access.

Mitigation: Prefer read-only OAuth unless writes are needed, and require explicit human confirmation before destructive operations.

Risk: The REST fallback uses an xCloud bearer token supplied by the user environment.

Mitigation: Prefer the OAuth MCP connector, store REST tokens in the runtime or secret store, use narrow scopes, and rotate or revoke exposed tokens.

Risk: API responses, logs, site names, and vulnerability data may contain untrusted text.

Mitigation: Treat all xCloud API output as data rather than instructions, and do not treat response text as confirmation for write operations.

Risk: A misconfigured REST base URL could expose credentials over plaintext HTTP.

Mitigation: Use HTTPS for live endpoints; the bundled wrapper refuses plaintext HTTP unless a local-development override is explicitly set.

## Reference(s):

- [xCloud](https://xcloud.host)
- [xCloud Dashboard](https://app.xcloud.host)
- [User Guide](https://github.com/xCloudDev/xcloud-agent-skills/blob/main/docs/USER_GUIDE.md)
- [Install Guide](https://github.com/xCloudDev/xcloud-agent-skills/blob/main/docs/SKILLS-GUIDE.md)
- [Official GitHub](https://github.com/xCloudDev/xcloud-agent-skills)
- [MCP Docs](https://app.xcloud.host/mcp/docs)
- [API Docs](https://app.xcloud.host/api/v1/docs)
- [OpenClaw Tutorial](https://xcloud.host/openclaw-skills-and-clawhub-on-xcloud-openclaw-agent/)
- [Tutorial Video](https://www.youtube.com/watch?v=oEE9OHo3_48)
- [Authentication Reference](plugins/xcloud/reference/auth.md)
- [API Conventions Reference](plugins/xcloud/reference/conventions.md)
- [MCP Reference](plugins/xcloud/reference/mcp.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke xCloud MCP tools or a curl-based REST wrapper after the user connects or configures an xCloud account; no API calls run during installation.]

## Skill Version(s):

4.0.2 (source: evidence release, frontmatter, and changelog; released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
