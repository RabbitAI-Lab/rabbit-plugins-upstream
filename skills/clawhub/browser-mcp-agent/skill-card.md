## Description:

Browser MCP Agent lets an AI agent control a real, fingerprinted browser over MCP to launch, navigate, click, fill forms, capture screenshots, extract text, and run JavaScript while keeping a persistent logged-in profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antibrow](https://clawhub.ai/user/antibrow)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to give an agent a scoped browser session for authorized site operation, dashboard checks, content extraction, form interaction, and debugging browser actions without writing custom Playwright or SDK code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent operating a persistent logged-in browser can take actions inside real accounts.

Mitigation: Use separate or throwaway profiles for untrusted sites and require human approval before purchases, deletions, posts, or other sensitive actions.

Risk: JavaScript execution and browser page content can expand the impact of indirect prompt injection or unsafe page behavior.

Mitigation: Expose only the MCP tools needed for the task, treat returned page content as untrusted data, and avoid unnecessary JavaScript execution.

Risk: Live view can expose whatever the browser profile is logged into through a shareable screen stream.

Mitigation: Avoid live view on sensitive accounts and stop any live view session when the task ends.

Risk: The integration uses an external browser binary and API key.

Mitigation: Use pinned package versions, review the vendor binary before deployment, and keep API keys in environment variables rather than configuration files.

## Reference(s):

- [Browser MCP Agent on ClawHub](https://clawhub.ai/antibrow/skills/browser-mcp-agent)
- [AntiBrow dashboard](https://antibrow.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MCP setup guidance, tool exposure recommendations, and operational safety notes.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
