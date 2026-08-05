## Description: <br>
TodoWrite helps agents route TODOs across session tasks, persistent checklist files, and GitHub issues while keeping task references, completion reports, and task-to-checklist synchronization disciplined. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to decide where TODOs should live, keep task status visible, and synchronize local task records with persistent checklist files or GitHub issues when appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can actively mutate local TODOs, checklist files, and task JSON records as part of normal operation. <br>
Mitigation: Install it only when active TODO management is desired, and review task/checklist changes when work is moved, completed, or cleaned up. <br>
Risk: Broad activation wording may cause the skill to influence more task-management interactions than expected. <br>
Mitigation: Review the routing topics, optional hook setup, and wrapper behavior before enabling the skill in an agent environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/todowrite) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Claude task CLI topic](artifact/claude-task.md) <br>
- [TaskList conversation IDs](artifact/conversation-id.md) <br>
- [Task completion report format](artifact/completion-report.md) <br>
- [Task/checklist two-way sync](artifact/fix-plan-sync.md) <br>
- [Priority prefix](artifact/priority-prefix.md) <br>
- [Work record media separation](artifact/media-separation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, checklist text, and optional local task JSON updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local TODO, checklist, or task JSON state when used by an agent.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata and CHANGELOG, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
