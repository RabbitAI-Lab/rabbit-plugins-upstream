## Description:

AI电商专家｜TikTok Shop 图片视频全内容 helps ecommerce teams plan and submit IMIVA MCP tasks for TikTok Shop product images, detail content, and video assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, operators, designers, advertising teams, and agency teams use this skill to prepare TikTok Shop listing, seeding, ad, and conversion-oriented image and video content through IMIVA MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper runs an unpinned npm package for IMIVA MCP access.

Mitigation: Review and trust the IMIVA/@infimind package before installation, and prefer a pinned package version where the deployment environment allows it.

Risk: The helper passes the local environment to the MCP process, which may expose unrelated secrets if run from a broad shell environment.

Mitigation: Run it from a restricted shell that contains only the required MCP_TOKEN and API_URL or IMIVA_API_URL variables.

Risk: Generated ecommerce tasks can use credits or create billable content tasks.

Mitigation: Use dry runs, review estimatedCredits, set maxCredits, and confirm task details before creating paid tasks.

Risk: Product media, ecommerce assets, and tokens are sent to a remote IMIVA service.

Mitigation: Use the skill only when the publisher, service, and token handling are acceptable for the user's ecommerce media and data policies.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-tiktok-shop-ecommerce-content)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP tool arguments, task IDs, dry-run credit estimates, and follow-up checks.]

## Skill Version(s):

1.0.0 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
