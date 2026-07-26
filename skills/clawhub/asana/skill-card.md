## Description: <br>
Manage Asana via the Asana REST API. Use when you need to list workspaces, projects, tasks, search tasks, comment, update, complete, or create tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[k0nkupa](https://clawhub.ai/user/k0nkupa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect and manage Asana workspaces, projects, and tasks through authenticated Asana REST API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses reusable Asana credentials that can read and modify account data. <br>
Mitigation: Use a Personal Access Token or OAuth app with only the permissions needed for the intended workspace and keep ~/.openclaw/asana out of sync folders and repositories. <br>
Risk: The skill can create, update, comment on, and complete Asana tasks. <br>
Mitigation: Review any create, update, comment, or complete-task request before allowing the command to run. <br>


## Reference(s): <br>
- [Asana developer documentation](https://developers.asana.com/docs) <br>
- [Asana endpoints quick reference](references/asana-endpoints.md) <br>
- [ClawHub skill page](https://clawhub.ai/k0nkupa/skills/asana) <br>
- [Publisher profile](https://clawhub.ai/user/k0nkupa) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON outputs from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and Asana authentication through ASANA_PAT, local PAT config, or OAuth token files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
