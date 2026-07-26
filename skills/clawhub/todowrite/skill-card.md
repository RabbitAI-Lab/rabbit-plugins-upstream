## Description: <br>
Todowrite routes agent TODOs to session tasks, persistent checklist files, or GitHub Issues while enforcing task-reporting and synchronization discipline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Todowrite to decide whether TODO work belongs in session tracking, persistent checklist files, or team-shared GitHub Issues, and to keep related task records synchronized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update task and checklist records during task transfers, so ambiguous transfer language could move or close the wrong work item. <br>
Mitigation: Confirm ambiguous transfer scope, require explicit direction before creating issues, and report both the source and destination updates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite) <br>
- [Task Completion Report Format](completion-report.md) <br>
- [TaskList Conversation IDs](conversation-id.md) <br>
- [Task-Checklist Two-Way Sync](fix-plan-sync.md) <br>
- [Priority Prefix](priority-prefix.md) <br>
- [Work Record Media Separation](media-separation.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with checklist and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update TaskList state, checklist files, and GitHub issue records when the user explicitly directs those routes.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata and changelog, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
