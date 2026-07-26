## Description: <br>
File-based todo and task tracking in the todos/ directory for creating, triaging, listing, managing, and checking todo status and dependencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project teams use this skill to maintain persistent markdown todo files for backlog tracking, triage, dependencies, work logs, and completion status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can add, rename, and update project todo files under todos/. <br>
Mitigation: Review the resulting file changes before committing, especially when todo files may contain sensitive project details. <br>
Risk: Todo status, priority, and issue IDs can drift if filenames and frontmatter are not kept consistent. <br>
Mitigation: Verify unique sequential issue IDs and confirm status and priority values match both the filename and YAML frontmatter. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-file-todos) <br>
- [Todo Workflows](references/workflows.md) <br>
- [Quick Reference Commands](references/quick-reference.md) <br>
- [Todo Template](assets/todo-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown todo files with YAML frontmatter, structured sections, checklists, work logs, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Designed for project-local todo files under todos/; review generated file changes before committing when todo content may include sensitive project details.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
