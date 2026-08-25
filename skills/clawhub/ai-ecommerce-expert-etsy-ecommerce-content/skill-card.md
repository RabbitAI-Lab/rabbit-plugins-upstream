## Description:

AI电商专家｜Etsy 图片视频全内容 helps Etsy merchants and ecommerce teams turn product assets, selling points, channel goals, and requested specs into IMIVA MCP tasks for product images, detail-page content, and video materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External Etsy merchants, ecommerce operators, designers, advertising teams, and agency teams use this skill to prepare and run IMIVA ecommerce content generation workflows for listing images, product-detail content, seeding creatives, ad materials, and product videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper runs an unpinned npm package with the full local environment, which can expose unrelated secrets if the package or its dependencies change or are compromised.

Mitigation: Pin the npm package version, review updates before use, and run it with a minimal environment containing only the required IMIVA token, API URL, and file paths.

Risk: IMIVA tasks may upload local media or spend platform credits.

Mitigation: Require explicit user confirmation before tasks that upload media or create paid generations, including model, output count, specs, and credit limit.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-etsy-ecommerce-content)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare IMIVA MCP calls that upload user-provided media and consume platform credits after confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
