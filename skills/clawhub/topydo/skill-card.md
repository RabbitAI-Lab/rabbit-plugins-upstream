## Description: <br>
topydo helps agents manage todo.txt tasks with the topydo CLI, including adding, listing, completing, prioritizing, tagging, and organizing tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bastos](https://clawhub.ai/user/bastos) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to have an agent propose and run topydo CLI commands for todo.txt task management, including organization, scheduling, dependencies, and task state changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands that delete, edit, sort, archive, or bulk-complete tasks can change local todo.txt data unexpectedly. <br>
Mitigation: Before execution, list the affected tasks and confirm the exact task IDs or filter expression with the user. <br>
Risk: Installing the topydo CLI from an untrusted package source can expose the environment to supply-chain risk. <br>
Mitigation: Install topydo only from a package source the user trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bastos/skills/topydo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that alter local todo.txt data; destructive or bulk operations should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact metadata.version: 2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
