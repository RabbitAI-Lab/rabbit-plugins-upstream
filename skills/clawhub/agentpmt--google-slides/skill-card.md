## Description: <br>
Google Slides lets agents create, edit, and manage Google Slides presentations through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workflow operators use this skill to automate Google Slides deck creation, template filling, slide editing, thumbnails, and presentation maintenance through AgentPMT MCP or REST calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes broad write and delete capabilities for Google Slides presentations. <br>
Mitigation: Install only when that level of access is acceptable, keep inputs scoped, and review target presentation IDs before execution. <br>
Risk: Raw batch_update and delete_object actions can make broad or destructive changes. <br>
Mitigation: Prefer high-level edit actions and use raw batch_update or delete_object only when the intended change is explicit. <br>
Risk: Image insertion requires publicly accessible image URLs. <br>
Mitigation: Use approved public assets and avoid URLs that expose confidential or access-controlled material. <br>


## Reference(s): <br>
- [ClawHub Google Slides skill](https://clawhub.ai/agentpmt/skills/google-slides) <br>
- [AgentPMT Google Slides marketplace page](https://www.agentpmt.com/marketplace/google-slides) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>
- [Generated action schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, JSON] <br>
**Output Format:** [Markdown instructions with JSON MCP and REST call bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote AgentPMT calls return JSON responses and may create, update, duplicate, reorder, or delete Google Slides presentation content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
