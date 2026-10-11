## Description:

Guides agents in editing and creating images through AgentPMT's hosted image editor, including resizing, cropping, overlays, and chained transformations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to create and edit images for thumbnails, branded graphics, watermarks, and other visual assets using AgentPMT's remote tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs and referenced URLs are sent to AgentPMT-hosted infrastructure.

Mitigation: Avoid sensitive, regulated, or private-link images unless remote processing is approved.

Risk: Edited outputs are stored remotely by default.

Mitigation: Set store_file=false when persistent storage is not needed.

## Reference(s):

- [Image Editor action schema](schema.md)
- [Image Editor on ClawHub](https://clawhub.ai/agentpmt/skills/image-editor)
- [AgentPMT Image Editor marketplace page](https://www.agentpmt.com/marketplace/image-editor)
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)

## Skill Output:

**Output Type(s):** [Guidance, JSON request examples]

**Output Format:** [Markdown instructions with JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote tool can return image metadata, a stored file link, or inline base64 output; stored files expire after seven days and inline base64 is limited to 10 MB.]

## Skill Version(s):

1.0.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
