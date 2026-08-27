## Description:

AI电商专家｜快手电商 图片视频全内容 helps Kuaishou ecommerce merchants and operations teams prepare IMIVA MCP requests for product images, detail pages, seeding content, advertising creatives, and short videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, operators, designers, advertisers, and agency teams use this skill to turn product facts, media, channel goals, and budget constraints into IMIVA ecommerce content generation workflows. It is focused on Kuaishou ecommerce listing, seeding, advertising, and conversion materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a live npm package while handling an IMIVA MCP token and selected ecommerce media.

Mitigation: Install it only in an environment where the IMIVA/@infimind package is trusted, inject the MCP token through host-managed secrets, and avoid running it alongside unrelated secrets.

Risk: Using @infimind/ecom-content-cli@latest can change runtime behavior as the package updates.

Mitigation: Pin the npm package version before production use and re-review the package after upgrades.

Risk: Image and video task creation may consume credits or process business-sensitive product material.

Mitigation: Use dry-run and credit checks before paid tasks, confirm user budget limits, and share only product media that is appropriate to send to IMIVA.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-kuaishou-ecommerce-content)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides users through token setup, dry-run credit checks, task creation, task lookup, and result review.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
