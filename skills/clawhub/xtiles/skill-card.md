## Description: <br>
Create and manage structured visual pages, projects, tiles, tasks and workflows in xTiles via MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xtiles](https://clawhub.ai/user/xtiles) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to connect to a signed-in xTiles workspace, then read or update projects, pages, tiles, tasks, layouts, collections, planners, workflows, and user context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify the signed-in user's xTiles workspace. <br>
Mitigation: Install it only when workspace access is intended, prefer OAuth authentication, and review create or update actions before approval. <br>
Risk: Task deletion is irreversible. <br>
Mitigation: Confirm destructive intent and the specific resources before using deletion capabilities. <br>
Risk: Due dates and relative dates can be wrong if the user's timezone is not resolved. <br>
Mitigation: Call the xTiles timezone tool before creating or updating dated tasks and resolve relative dates against the returned IANA timezone. <br>


## Reference(s): <br>
- [xTiles](https://xtiles.app) <br>
- [xTiles MCP endpoint](https://mcp.xtiles.app/mcp) <br>
- [ClawHub xTiles skill page](https://clawhub.ai/xtiles/skills/xtiles) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls] <br>
**Output Format:** [Markdown with inline shell commands and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance includes OAuth setup, capability groups, date handling, workflow discovery, and confirmation before destructive workspace changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
