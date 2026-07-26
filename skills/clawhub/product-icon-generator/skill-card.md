## Description: <br>
Renders deterministic PNG icons, sprites, and textures from bounded drawing instructions through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and agents use this skill to create product icons, UI iconography, brand badges, pixel-art sprites, and game textures as deterministic PNG files through AgentPMT. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid remote AgentPMT generation service. <br>
Mitigation: Confirm the intended AgentPMT account, enabled product, and credit spend before generating icons or sprites. <br>
Risk: Broad trigger terms may cause an agent to select the skill before the user intends remote generation. <br>
Mitigation: Ask for confirmation before sending proprietary design instructions or starting a paid render. <br>
Risk: Generated files and signed URLs are temporary. <br>
Mitigation: Download or transfer needed PNG outputs before the 3-day file retention period and 15-minute signed URL expiry. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/agentpmt/skills/product-icon-generator) <br>
- [AgentPMT Product Icon Generator marketplace page](https://www.agentpmt.com/marketplace/product-icon-generator) <br>
- [AgentPMT account MCP/REST setup skill](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Files] <br>
**Output Format:** [Markdown instructions with JSON request examples; the remote action returns PNG file metadata and a signed URL.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated PNG files are retained for 3 days; signed URLs expire after 15 minutes.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
