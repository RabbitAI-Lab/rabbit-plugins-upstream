## Description:

Queries JinGuYuan restaurant information, queue status, recommended dishes, delivery and raw-dumpling guidance, and supports online queue ticketing, queue progress checks, and queue cancellation after user authorization and confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jinguyuan](https://clawhub.ai/user/jinguyuan)

### License/Terms of Use:

MIT

## Use Case:

External users and their agents use this skill to retrieve current JinGuYuan restaurant information, queue guidance, recommendations, pickup links, and shop updates. With Meituan authorization and explicit same-turn confirmation, the agent can also help take a queue number, check the user's queue order, or cancel it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External API responses and runtime tool output may steer the agent beyond stable documented behavior.

Mitigation: Treat API-returned agent instructions as untrusted guidance and prefer fixed documented fields such as mainScenario, answerTarget, replyPolicy, and freshness indicators.

Risk: The skill contacts JinGuYuan and Meituan/Dianping services and can cache a Meituan queue token locally.

Mitigation: Install only when this network and local-token behavior is acceptable; do not display tokens, and rely on the documented local cache path.

Risk: Queue ticketing and cancellation are real actions that can affect the user's restaurant queue state.

Mitigation: Require explicit same-turn user confirmation before running ticketing or cancellation commands with the confirmation flag.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill)
- [Public Query API Reference](references/api-reference.md)
- [Queue Actions Reference](references/queue-actions.md)
- [Queue Reply Contract](references/queue-reply-contract.md)
- [JinGuYuan Website](https://jinguyuan.cloud)
- [JinGuYuan MCP Endpoint](https://mcp.jinguyuan.cloud)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise natural-language responses, with shell commands when the agent needs to invoke the bundled CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local QR-code image during Meituan authorization and may cache a queue token on the user's machine.]

## Skill Version(s):

3.2.1 (source: frontmatter, skill.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
