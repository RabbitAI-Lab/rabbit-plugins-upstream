## Description: <br>
Project management and multi-agent work coordination through AuraBaba for assigning tasks, tracking project progress, managing deliverables, and scheduling milestones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hjyoite](https://clawhub.ai/user/hjyoite) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and team leads use this skill to coordinate AuraBaba workspaces through an agent: discovering agents and squads, creating and updating issues, tracking blockers, preserving comments and deliverables, and managing calendar events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on authenticated AuraBaba project data broadly, including issue, label, metadata, token, and calendar operations. <br>
Mitigation: Use a dedicated least-privilege token where possible, keep credentials out of chats and logs, and require explicit user confirmation before destructive changes. <br>
Risk: Deletion-capable API surfaces can remove issues, labels, metadata, tokens, or calendar events without strong guardrails in the skill text. <br>
Mitigation: Review planned delete operations with the target workspace, resource identifier, and impact before execution. <br>


## Reference(s): <br>
- [AuraBaba Platform Skill on ClawHub](https://clawhub.ai/hjyoite/skills/auramanager-platform) <br>
- [AuraBaba](https://aurababa.com) <br>
- [auramanager-platform source map](references/auramanager-platform-source-map.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration, shell commands] <br>
**Output Format:** [Markdown with inline HTTP, JSON, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include bearer-token setup guidance, workspace routing details, issue and calendar API examples, and agent/squad coordination steps.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
