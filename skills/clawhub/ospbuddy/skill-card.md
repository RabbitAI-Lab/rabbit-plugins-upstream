## Description:

OpsBuddy helps users configure an API-key-backed MCP connection for an operations assistant that supports asset discovery, monitoring, diagnostics, log search, and alert analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hatjs880328s](https://clawhub.ai/user/hatjs880328s)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect OpsBuddy as a WorkBuddy MCP server, apply an MCP token, and route monitoring platform setup through the OpsBuddy portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose API keys or bearer tokens by pasting full MCP configuration into chat.

Mitigation: Use a secure local import or manually edit local configuration with restrictive permissions; do not paste API keys, bearer tokens, or full MCP config JSON into chat.

Risk: The OpsBuddy portal is served over plain HTTP at an IP address, which can expose credentials or verification codes in transit.

Mitigation: Be cautious about entering account credentials or verification codes, use a trusted network, and verify the portal with the publisher before entering sensitive information.

Risk: Bearer-token configuration is stored persistently in a local MCP config file.

Mitigation: Restrict local file permissions, revoke leaked or expired tokens, and rotate the token when updating the configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hatjs880328s/skills/ospbuddy)
- [OpsBuddy portal](http://119.45.243.120:45321)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-supplied OpsBuddy MCP token; downloaded configuration may contain a bearer token.]

## Skill Version(s):

1.0.3 (source: server release metadata, artifact frontmatter, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
