## Description:

AI电商专家｜母婴童装电商图片视频 helps ecommerce teams use IMIVA MCP workflows to generate product images, detail-page assets, KOC seeding visuals, and product video content for mother, baby, and children's apparel listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce brands, merchants, operators, designers, advertisers, and content teams use this skill to turn product assets, selling points, target audiences, channel requirements, and budget constraints into IMIVA MCP tasks for listing-ready images and videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script runs a mutable npm package with inherited environment access, which could expose unrelated local secrets.

Mitigation: Run it from a dedicated terminal or MCP client profile that only exposes the required MCP_TOKEN and API_URL environment variables.

Risk: Local product images or videos provided to the workflow may be uploaded to IMIVA for processing.

Mitigation: Use only assets the user is authorized to process and avoid providing confidential media unless IMIVA processing is acceptable.

Risk: Image and video generation tasks may consume platform credits, especially when repeated or submitted without budget checks.

Mitigation: Check credits before submission, use dry-run budget estimates for video where supported, set confirmed credit limits, and query existing task IDs instead of blindly recreating tasks.

## Reference(s):

- [IMIVA AI Ecommerce Expert Homepage](https://imiva.ecpro.com/)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-mother-baby-ecommerce-content)
- [IMIVA MCP Configuration Example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with JSON MCP arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP tool arguments, configuration snippets, task IDs, budget checks, and validation steps for generated ecommerce content.]

## Skill Version(s):

1.0.0 (source: target metadata, release evidence, and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
