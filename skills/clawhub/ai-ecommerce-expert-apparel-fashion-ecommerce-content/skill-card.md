## Description:

AI电商专家｜服装时尚电商图片视频 helps apparel and fashion ecommerce teams prepare IMIVA MCP workflows for product images, detail pages, social/KOC content, and product video from provided product media and confirmed selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External apparel and fashion ecommerce teams use this skill to turn product assets, channel goals, and verified selling points into IMIVA ecommerce content generation tasks. It supports configuration, budget confirmation, task creation, task lookup, and output review for commercial marketplace and social commerce workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an IMIVA MCP token and may send product media or task inputs to the IMIVA ecommerce generation service.

Mitigation: Install it only when intending to use IMIVA, keep MCP_TOKEN in a local environment variable or client secret store, and avoid sharing tokens in skill files, screenshots, chats, or repositories.

Risk: Image and video jobs may consume paid credits when submitted.

Mitigation: Check credits and confirm model, count, duration, resolution, and channel specs before creation; use video dry-run estimates, maxCredits, and idempotency keys where supported.

Risk: The example MCP configuration uses @latest, which may change package behavior over time.

Mitigation: Pin @infimind/ecom-content-cli to a tested package version for production deployments.

Risk: Generated ecommerce assets can misstate product facts or misuse unauthorized third-party references.

Mitigation: Use only verified product facts and review output text, claims, trademarks, packaging, people, channel specs, and reference rights before publishing.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-apparel-fashion-ecommerce-content)
- [MCP configuration example](artifact/references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with JSON arguments and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include IMIVA MCP tool arguments, local or HTTPS media paths, task IDs, and budget-confirmation steps.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
