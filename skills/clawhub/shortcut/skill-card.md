## Description: <br>
Manage stories on Shortcut.com kanban boards, including story creation, updates, listing, checklist task management, and comment support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[catwalksophie](https://clawhub.ai/user/catwalksophie) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and project teams use this skill to let an agent manage Shortcut project work: listing stories, creating and updating stories, moving work through states, and maintaining tasks and comments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify and delete Shortcut workspace data with limited safety prompts or scoping. <br>
Mitigation: Review create, update, and delete requests before execution, and use a minimally scoped Shortcut token when available. <br>
Risk: Shortcut API tokens grant workspace access and may be exposed if stored in repositories or shared logs. <br>
Mitigation: Store tokens outside repositories, prefer the documented user config path or environment variable, and rotate tokens if exposure is suspected. <br>
Risk: Workspace-specific workflow state IDs may differ from the documented defaults. <br>
Mitigation: Run the workflow initialization script before relying on state transitions, and confirm the generated state mapping for the target workspace. <br>


## Reference(s): <br>
- [Shortcut API v3 endpoint](https://api.app.shortcut.com/api/v3) <br>
- [ClawHub Shortcut skill page](https://clawhub.ai/catwalksophie/skills/shortcut) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and Shortcut API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Shortcut API token and workspace permissions; several operations can create, update, or delete Shortcut workspace data.] <br>

## Skill Version(s): <br>
1.4.1 (source: frontmatter, CHANGELOG, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
