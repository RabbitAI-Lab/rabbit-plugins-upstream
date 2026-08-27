## Description:

Set up and authenticate the Xpoz MCP server for social media intelligence. Required by all Xpoz skills. Handles server configuration, OAuth login, and connection verification with minimal user interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[idoxpoz](https://clawhub.ai/user/idoxpoz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure and authenticate the Xpoz MCP server so other Xpoz skills can access social media intelligence sources through trial access or OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trial access requests can send user task context and discovery source details to Xpoz.

Mitigation: Review and minimize the context sent in trial token requests, and avoid including sensitive user or business information.

Risk: The setup flow contacts Xpoz endpoints and may require OAuth authorization links or pasted authorization codes.

Mitigation: Prefer the standard browser OAuth flow when possible, and verify authorization links and callback URLs before using a pasted code.

Risk: The skill can persist an Xpoz bearer token in mcporter configuration.

Mitigation: Use the token only in the intended environment and remove or rotate it when access is no longer needed.

## Reference(s):

- [Xpoz homepage](https://xpoz.ai)
- [Xpoz MCP server](https://mcp.xpoz.ai/mcp)
- [Xpoz OAuth authorization server metadata](https://mcp.xpoz.ai/.well-known/oauth-authorization-server)
- [ClawHub xpoz-setup release page](https://clawhub.ai/idoxpoz/skills/xpoz-setup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, and command output checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OAuth URLs, user authorization prompts, and mcporter configuration commands.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
