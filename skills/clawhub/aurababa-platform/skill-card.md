## Description: <br>
Project management and multi-agent work coordination through AuraBaba. Use whenever a user asks to assign or delegate tasks, create or advance a project, split work across people or agents, track progress or blockers, add comments or labels, manage deliverables, schedule calendar events or milestones, or coordinate a team. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hjyoite](https://clawhub.ai/user/hjyoite) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, team leads, and agent operators use this skill to connect an agent to AuraBaba for project coordination: discovering available agents and squads, creating and updating issues, tracking blockers and deliverables, adding comments or labels, and managing calendar events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, assign, label, comment on, or delete real AuraBaba workspace records. <br>
Mitigation: Require the agent to summarize the planned change and get explicit approval before any mutating issue, label, metadata, comment, assignment, or calendar request. <br>
Risk: A broad or shared token could expose more workspace access than needed. <br>
Mitigation: Use a dedicated least-privilege personal access token for each agent, store it only in secret or environment configuration, and rotate or revoke it when no longer needed. <br>
Risk: Requests sent to the wrong workspace or assignee could misroute work. <br>
Mitigation: Verify the target workspace slug and selected member, agent, or squad before making project or calendar changes. <br>


## Reference(s): <br>
- [AuraBaba Platform Skill source map](references/aurababa-platform-source-map.md) <br>
- [AuraBaba](https://aurababa.com) <br>
- [ClawHub skill page](https://clawhub.ai/hjyoite/skills/aurababa-platform) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with HTTP examples, JSON payloads, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a bearer token and workspace slug to perform real AuraBaba project, issue, label, metadata, comment, and calendar operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
