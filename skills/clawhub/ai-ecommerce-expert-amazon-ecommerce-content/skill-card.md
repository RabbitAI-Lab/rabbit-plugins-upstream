## Description:

AI电商专家｜Amazon 亚马逊 图片视频全内容 helps Amazon sellers, operators, designers, ad teams, and ecommerce agencies prepare IMIVA MCP tasks for product images, detail-page content, and product video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams use this skill to turn product assets, selling points, target audience, channel requirements, and budget constraints into executable IMIVA MCP workflows for Amazon listing images, detail pages, advertising creatives, and product videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a dynamically fetched MCP package and passes the local environment to that process.

Mitigation: Install only when the IMIVA service and npm package publisher are trusted, pin a specific package version where possible, and restrict environment variables exposed to the MCP process.

Risk: Product images, videos, prompts, and MCP tokens are sent to IMIVA during task execution.

Mitigation: Use approved product assets, keep the MCP token in local environment variables or a client secret store, and avoid placing tokens in skills, screenshots, chats, or repositories.

Risk: Image tasks may consume credits on submission and video tasks may consume credits after budget confirmation.

Mitigation: Check available credits first, use dry-run credit estimates for video tasks, set explicit maximum credits, and confirm model, count, resolution, and duration before creating tasks.

Risk: Generated ecommerce content can contain inaccurate claims, copied third-party creative elements, or channel-unsuitable text and layout.

Mitigation: Verify all product facts against user-provided evidence, use third-party references only for general structure, and review output for authorization, accuracy, safe areas, copy, aspect ratio, and platform fit before publishing.

## Reference(s):

- [IMIVA AI Ecommerce Expert](https://imiva.ecpro.com/)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-amazon-ecommerce-content)
- [MCP Configuration Example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce IMIVA MCP task arguments, budget-confirmation steps, task-query commands, and quality-review checklists.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
