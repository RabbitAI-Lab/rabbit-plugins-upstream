## Description:

AI电商专家｜3C 数码电商图片视频 helps ecommerce teams prepare IMIVA MCP tasks for consumer-electronics product detail images, listing visuals, seeding content, and product videos using confirmed product assets and specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce brands, merchants, operators, designers, ad buyers, and content teams use this skill to turn verified 3C/digital product materials, channel goals, budget, and output specs into IMIVA MCP task parameters for product images, detail pages, social commerce content, and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill launches an unpinned external npm MCP helper that receives service credentials.

Mitigation: Pin the @infimind package version where possible, use a scoped and revocable MCP token, and run with only MCP_TOKEN and API_URL in the environment.

Risk: Image or video task creation may consume credits or upload sensitive product media.

Mitigation: Confirm model, quantity, credit budget, and media authorization before creating tasks; use dry-run budget checks for video when available.

Risk: Generated ecommerce assets can contain inaccurate product details, claims, or unauthorized third-party creative elements.

Mitigation: Use only user-confirmed product facts and authorized references, then review generated text, product appearance, claims, and channel requirements before publication.

## Reference(s):

- [IMIVA AI Ecommerce Expert homepage](https://imiva.ecpro.com/)
- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-consumer-electronics-ecommerce-content)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON MCP arguments and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an IMIVA MCP token and user-confirmed product facts, media authorization, model choices, quantities, and credit budget before task creation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
