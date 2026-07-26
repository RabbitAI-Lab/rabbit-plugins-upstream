## Description: <br>
Manage and organize KanbanFlow board tasks by adding, moving, coloring, and deleting tasks across columns to track work progress. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abakermi](https://clawhub.ai/user/abakermi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to guide an agent in listing KanbanFlow boards, columns, and tasks, and in adding, moving, coloring, or deleting tasks during workflow management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward task-changing KanbanFlow operations, including move, color, add, and delete. <br>
Mitigation: Require explicit confirmation before delete or other task-changing commands. <br>
Risk: Commands may affect the wrong KanbanFlow board if the underlying integration is misconfigured. <br>
Mitigation: Verify that the trusted kanbanflow command or integration is connected to the intended board before use. <br>


## Reference(s): <br>
- [Kanbanflow Skill on ClawHub](https://clawhub.ai/abakermi/skills/kanbanflow-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses KanbanFlow command examples for board, column, task, add, move, color, and delete operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
