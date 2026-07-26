## Description: <br>
Google Drive enables an AgentPMT-connected agent to search, upload, download, organize, move, copy, share, and export files in Google Drive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs to manage Google Drive documents through AgentPMT, including file search, transfer, folder organization, sharing, permission review, and Google Workspace export workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can permanently delete Google Drive files or folders. <br>
Mitigation: Confirm file IDs before deletion and prefer the recoverable trash action when recovery may be needed. <br>
Risk: The skill can change file and folder sharing permissions. <br>
Mitigation: Use user or group sharing for intended recipients, review permission roles, and avoid anyone or domain sharing unless explicitly intended. <br>
Risk: Shared drives are included by default in supported actions. <br>
Mitigation: Set shared-drive inclusion to false when the workflow should be limited to My Drive. <br>
Risk: Uploads can fetch content from public URLs. <br>
Mitigation: Upload only from trusted public URLs or known AgentPMT storage file IDs. <br>


## Reference(s): <br>
- [AgentPMT Google Drive marketplace page](https://www.agentpmt.com/marketplace/google-drive) <br>
- [ClawHub Google Drive skill page](https://clawhub.ai/agentpmt/skills/google-drive) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, JSON, API calls] <br>
**Output Format:** [Markdown instructions with JSON action payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses AgentPMT-hosted remote tool calls; no local command runtime is declared.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
