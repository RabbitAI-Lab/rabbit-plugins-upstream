## Description:

AI电商专家｜批量商品视频变体 helps ecommerce content teams plan and submit IMIVA MCP video-generation tasks for up to 12 product-video variants for creative testing, channel adaptation, and multi-SKU workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand content teams, ad creators, video editors, and social commerce teams use this skill to convert product assets, audience goals, channel requirements, and budget limits into executable IMIVA video-generation requests. It emphasizes budget confirmation, task tracking, and review of generated product-video variants before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill launches an npm package resolved from the registry while using an IMIVA token.

Mitigation: Run it in a restricted environment, provide only the required IMIVA variables, and consider pinning the npm package version before use.

Risk: Formal video-generation requests may consume paid credits.

Mitigation: Use dry-run checks first, review estimated credits, and submit paid tasks only after the user confirms the budget.

Risk: Generated ecommerce videos can include inaccurate product claims or unauthorized visual references.

Mitigation: Use only user-confirmed product facts and authorized assets, then review product details, text, claims, and channel fit before publishing.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](artifact/references/mcp-config.example.json)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-batch-video-variations)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON MCP arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce IMIVA MCP task arguments for dry-run checks, paid video-generation submissions, and task-status queries.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
