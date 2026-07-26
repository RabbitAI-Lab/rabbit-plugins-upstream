## Description: <br>
Manage family todo lists with multi-user support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thurendous](https://clawhub.ai/user/thurendous) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Families and household agents use this skill to add, list, complete, delete, and review shared or person-specific todo items from a local Node.js command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Todo entries are stored as plain local JSON data and may contain household or personal information. <br>
Mitigation: Avoid storing highly sensitive information and protect the local memory/todo.json file with appropriate filesystem access controls. <br>
Risk: Configured user IDs support routing and filtering but are not real access control. <br>
Mitigation: Do not rely on the configured user IDs for authorization; use separate platform-level controls for access to the skill and its data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thurendous/skills/family-todo-management) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text command output and JSON file storage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores tasks in memory/todo.json and prints task lists, confirmations, briefings, and review summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
