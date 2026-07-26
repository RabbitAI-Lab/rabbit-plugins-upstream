## Description: <br>
Task tracking for async/multi-step work. Use dex to create, track, and complete tasks that span multiple sessions or require coordination (e.g., coding agent dispatches, PR reviews, background jobs). Tasks stored as JSON files in .dex/tasks/. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gricha](https://clawhub.ai/user/gricha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to keep track of asynchronous or multi-step work, including coding-agent dispatches, PR reviews, background jobs, and follow-up tasks across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task descriptions, context, and results may persist sensitive information on disk under .dex/tasks/. <br>
Mitigation: Do not put secrets, credentials, or other sensitive data in task fields before running dex commands. <br>
Risk: The skill assumes the local dex command is the intended task tracker. <br>
Mitigation: Confirm the installed dex command on the machine before using the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gricha/skills/dex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in local JSON task files under .dex/tasks/ when the dex commands are run.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
