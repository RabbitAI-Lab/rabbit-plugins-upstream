## Description:

AI电商专家｜Shopify 独立站 图片视频全内容 helps Shopify, DTC, marketing, design, and agency teams prepare IMIVA MCP tasks for product images, product detail pages, seeding content, ad creatives, and video assets from user-provided product materials and confirmed requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce merchants, Shopify independent-site operators, marketing teams, designers, and agencies use this skill to turn product assets, channel goals, audience notes, budget constraints, and output specifications into executable IMIVA ecommerce-content workflows. The skill supports task setup, budget checking, MCP tool calls, task lookup, and result review for product imagery, detail-page content, social commerce material, and video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper invokes a mutable npm package while passing through the local environment.

Mitigation: Use a dedicated shell or client profile with only the IMIVA token and required variables, and pin the npm package to a reviewed version before production use.

Risk: Product media and task inputs may be uploaded to the IMIVA service.

Mitigation: Provide only media and product information that the user is comfortable sharing with the service.

Risk: Image and video task creation may consume paid credits.

Mitigation: Confirm credits, generation counts, model choices, and task parameters before submitting paid generation tasks.

## Reference(s):

- [IMIVA AI Ecommerce Expert Homepage](https://imiva.ecpro.com/)
- [MCP configuration example](artifact/references/mcp-config.example.json)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-shopify-ecommerce-content)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include IMIVA MCP task arguments, budget checks, task IDs, status queries, and review criteria for generated ecommerce assets.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
