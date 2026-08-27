## Description:

AI电商专家｜达人 UGC 商品图 helps ecommerce, brand, KOC/KOL, and social commerce teams prepare IMIVA MCP tasks that generate natural-looking influencer and user-generated product visuals from confirmed product assets, selling points, channel goals, and output specifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce brands, merchants, Xiaohongshu operators, KOC/KOL teams, brand content teams, and social media operators use this skill to turn product materials, audience goals, channel requirements, and budget constraints into IMIVA MCP task parameters for influencer-style UGC product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill launches an unpinned external npm MCP helper while service credentials are present.

Mitigation: Pin the @infimind package version where possible, use a scoped and revocable IMIVA token, and run with only MCP_TOKEN and API_URL in the environment.

Risk: Image task creation may consume IMIVA credits or upload sensitive product media.

Mitigation: Confirm model, quantity, resolution, credit budget, and media authorization before creating tasks.

Risk: Generated ecommerce assets can contain inaccurate product details, claims, text, or unauthorized third-party creative elements.

Mitigation: Use only user-confirmed product facts and authorized references, then review generated product appearance, claims, copy, and channel requirements before publication.

## Reference(s):

- [IMIVA AI Ecommerce Expert homepage](https://imiva.ecpro.com/)
- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-influencer-ugc-product-image)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON MCP arguments, configuration snippets, and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an IMIVA MCP token plus user-confirmed product facts, media authorization, model choices, quantities, specifications, and credit budget before task creation.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
