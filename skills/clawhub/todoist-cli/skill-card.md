## Description: <br>
Manage Todoist tasks, projects, labels, and sections through the todoist CLI for task listing, creation, completion, search, and organization workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[buddyh](https://clawhub.ai/user/buddyh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Todoist users use this skill to operate Todoist from an agent workflow, including listing, adding, updating, completing, reopening, moving, and deleting tasks. It also supports project, label, section, comment, completed-task, authentication, and JSON-output workflows through the todoist CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Todoist API token can grant access to task data and should be treated as a secret. <br>
Mitigation: Store TODOIST_API_TOKEN only in trusted environments and revoke the token in Todoist settings when it is no longer needed. <br>
Risk: Commands such as delete, move, complete, reopen, and update can modify Todoist tasks. <br>
Mitigation: Verify task IDs and intended changes before running destructive or state-changing commands. <br>
Risk: The skill depends on an external Todoist CLI installation source. <br>
Mitigation: Install only if the external Todoist CLI source is trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/buddyh/skills/todoist-cli) <br>
- [Todoist Developer Token Settings](https://todoist.com/app/settings/integrations/developer) <br>
- [Todoist CLI Homepage](https://github.com/buddyh/todoist-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown with inline bash commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the todoist binary and Todoist API token; commands may read or change Todoist task data.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
