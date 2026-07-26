## Description: <br>
Image Editor helps agents edit and transform PNG, JPEG, and WebP images through AgentPMT-hosted remote actions such as resize, crop, rotate, blur, invert, text overlay, drawing, compositing, background transparency, and multi-step workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to automate image-editing tasks such as thumbnail creation, watermarking, screenshot annotation, branded graphics, image format conversion, and chained transformations through AgentPMT remote tool calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image inputs are sent to AgentPMT-hosted infrastructure and may include sensitive or regulated visual data. <br>
Mitigation: Avoid confidential screenshots, IDs, private photos, and regulated data unless account and retention requirements allow it. <br>
Risk: Stored image outputs are enabled by default and return file links. <br>
Mitigation: Use return_base64 or store_file=false where supported when persistent stored output links are not needed. <br>
Risk: Account secrets or payment credentials could be exposed if included in prompts or logs. <br>
Mitigation: Use the AgentPMT setup skills for credential handling and keep tool inputs scoped to the minimum content needed. <br>


## Reference(s): <br>
- [AgentPMT Image Editor marketplace page](https://www.agentpmt.com/marketplace/image-editor) <br>
- [ClawHub Image Editor skill page](https://clawhub.ai/agentpmt/skills/image-editor) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Files, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [JSON tool-call arguments and JSON responses that may include file IDs, signed URLs, or base64 image data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces edited image outputs in png, jpeg, or webp; stored files are enabled by default, inline base64 is optional and limited to 10 MB, and stored files expire after 7 days.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
