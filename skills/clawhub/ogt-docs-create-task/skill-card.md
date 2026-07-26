## Description: <br>
Create and manage task documents in the docs/todo/ workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduardou24](https://clawhub.ai/user/eduardou24) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to create, update, and move task folders through a docs-first workflow with progress, review, blocking, completion, rejection, and implementation records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and move task-tracking files under docs/todo, which may change repository workflow state. <br>
Mitigation: Install it only in repositories that use this docs-first workflow and review generated file changes before accepting status transitions. <br>
Risk: Tasks can be marked done, rejected, or implemented through documentation and signal files. <br>
Mitigation: Require verification notes and human review before treating those workflow states as authoritative. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eduardou24/skills/ogt-docs-create-task) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with file templates and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, update, or move task-tracking files under docs/todo.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
