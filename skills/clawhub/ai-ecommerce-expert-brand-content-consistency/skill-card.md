## Description:

AI电商专家｜品牌电商视觉一致性 helps brand ecommerce, creative, and marketplace content teams use IMIVA MCP workflows to align product visuals with brand references while preserving product facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, and content operations teams use this skill to prepare IMIVA visual migration tasks for product images, videos, listings, and social commerce assets. The skill guides users through素材确认, budget checks, MCP configuration, task creation, task lookup, and channel-specific quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs external MCP software and uses environment variables for IMIVA access, which can expose broader local secrets than needed.

Mitigation: Run it in an environment without unrelated cloud, CI, database, or API secrets; prefer a pinned package version; use a scoped and revocable IMIVA token.

Risk: Generated ecommerce visuals may introduce inaccurate product details, claims, pricing, certifications, or brand elements.

Mitigation: Check all product facts, claims, text, logos, packaging, and channel requirements against user-provided source material before publishing.

Risk: Reference or competitor media can create intellectual property, likeness, or deceptive imitation concerns.

Mitigation: Use authorized references and copy only general composition, information hierarchy, or visual rhythm rather than protected marks, identities, packaging, or creative expression.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-brand-content-consistency)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [IMIVA homepage](https://imiva.ecpro.com/)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces IMIVA MCP task parameters, setup steps, and result-review guidance; it does not directly publish generated commerce assets.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
