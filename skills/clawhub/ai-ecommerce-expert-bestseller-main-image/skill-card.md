## Description:

AI电商专家｜爆款主图复刻与改造 helps ecommerce design, photography, operations, brand visual, and advertising teams prepare IMIVA MCP visual-migration tasks that turn authorized product and reference materials into original bestseller-style main images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce creators, brand teams, agencies, and marketplace operators use this skill to organize product facts, authorized reference media, output specs, budget checks, and IMIVA MCP calls for bestseller-style product image migration. It is intended for commercial ecommerce content workflows where generated images are reviewed before listing, advertising, or social commerce use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The IMIVA MCP token and selected product or customer media are sent to IMIVA's MCP service.

Mitigation: Use a scoped token in a client secret or clean shell environment, and submit only media intended for IMIVA processing.

Risk: The MCP package is referenced with @latest, so runtime behavior can change as the package is updated.

Mitigation: Pin the npm package version before controlled production deployment to reduce supply-chain drift.

Risk: Generated ecommerce visuals may include inaccurate product details or improperly reuse protected third-party creative elements.

Mitigation: Review product facts, reference-media authorization, channel requirements, and final image details before publishing.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-bestseller-main-image)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an IMIVA MCP token and authorized local or HTTPS media inputs; configured runs can return task IDs, task status, and generated-result references.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
