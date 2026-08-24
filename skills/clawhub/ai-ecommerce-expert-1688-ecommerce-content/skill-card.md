## Description:

AI电商专家｜1688 批发电商 图片视频全内容 helps 1688 wholesale ecommerce teams prepare IMIVA-powered product images, detail-page content, seeding assets, ad creatives, and product video workflows from supplied product materials and confirmed business facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External 1688 wholesale merchants, factory sellers, ecommerce operators, designers, media buyers, and agencies use this skill to turn supplied product media, verified product facts, channel targets, and budget constraints into IMIVA content-generation tasks. The skill is intended for product listing, detail-page, KOC seeding, advertising creative, product video, and viral-creative recreation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an unpinned remote MCP package through npx, which can change between installations.

Mitigation: Pin the IMIVA npm package version during deployment and review package updates before allowing task execution.

Risk: The authenticated MCP workflow can read explicitly supplied local media files and upload them to the IMIVA service.

Mitigation: Use a minimal client environment, provide only intended media paths or HTTPS URLs, and avoid exposing unrelated local files or secrets.

Risk: Image and video creation can consume user credits when tasks are submitted.

Mitigation: Require explicit confirmation of model, quantity, resolution, duration, and maximum credits before creating any task.

Risk: Implicit invocation is enabled in the agent configuration.

Mitigation: Review prompts before execution and require confirmation before authenticated calls or credit-consuming task creation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-1688-ecommerce-content)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create authenticated, credit-consuming IMIVA content-generation tasks when the user confirms task details and budget.]

## Skill Version(s):

1.0.0 (source: server release evidence, skill frontmatter, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
