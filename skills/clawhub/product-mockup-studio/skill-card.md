## Description:

Product Mockup Studio creates branded product mockup images, refines approved stills, and animates them into short videos through AgentPMT-hosted remote tool calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce teams, marketers, and agencies use this skill to turn product photos into marketplace-ready still images, branded visual variations, and short product videos. Agents use it to call the Product Mockup Studio actions, check job status, and retrieve managed PNG or MP4 outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable live schemas or instructions could change tool behavior before paid image or video generation.

Mitigation: Review the live schema or instruction response before allowing it to alter behavior or trigger paid generation.

Risk: Unpinned installation commands can retrieve different code over time.

Mitigation: Install from trusted ClawHub or OpenClaw routes and prefer pinned releases when available.

Risk: Product photos, prompts, and generated media may be processed by AgentPMT and external providers.

Mitigation: Avoid submitting secrets, private keys, payment headers, or unnecessary sensitive product material.

Risk: Generated product images or videos can distort logos, labels, colors, dimensions, or product details.

Mitigation: Visually review generated media before use and refine or regenerate outputs when product fidelity is insufficient.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/product-mockup-studio)
- [AgentPMT Product Mockup Studio Marketplace Page](https://www.agentpmt.com/marketplace/product-mockup-studio)
- [Product Mockup Studio Schema](./schema.md)
- [File Management Skill](https://clawhub.ai/agentpmt/file-management)
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [guidance, API Calls, configuration, shell commands, markdown]

**Output Format:** [Markdown guidance with JSON request examples and action schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creation actions return task IDs; completed jobs produce managed File Manager PNG image or MP4 video outputs with file IDs and preview URLs.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
