## Description:

AI电商专家｜电商全内容一站式生成 helps ecommerce merchants, brand teams, agencies, designers, and content teams prepare IMIVA MCP tasks for product main images, detail pages, seeding content, marketing visuals, and product videos from supplied product assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and content teams use this skill to turn product materials, selling points, channel goals, and output specifications into IMIVA ecommerce content generation workflows. It supports task setup, budget confirmation, MCP command examples, result querying, and quality review for commercial product imagery and video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a freshly downloaded IMIVA npm MCP package with an account token and inherited environment variables.

Mitigation: Install only when the IMIVA service and package are trusted; prefer a dedicated environment with no unrelated secrets and pin the package version when possible.

Risk: Submitting generation tasks may send selected product assets and prompts to imiva.ecpro.com and spend account credits.

Mitigation: Require explicit user confirmation for model, quantity, resolution, duration, and budget before creating tasks; use dry-run credit estimates for video tasks when available.

Risk: Generated ecommerce content may contain unsupported product claims, inaccurate product details, or unauthorized copied creative elements.

Mitigation: Use only user-confirmed product facts, verify generated text and visuals before publication, and avoid copying protected trademarks, identities, packaging, or distinctive creative expression from reference material.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-ecommerce-content-studio)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided product facts and assets to prepare task parameters, query existing tasks, and review generated ecommerce outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
