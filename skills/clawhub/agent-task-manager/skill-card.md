## Description: <br>
Agent Task Manager helps agents build and run multi-step, stateful workflows with task dependencies, persistent state, error recovery, and external rate-limit handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dobbybud](https://clawhub.ai/user/dobbybud) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to create multi-agent workflows that can resume from saved state, sequence role-based steps, and manage rate-limited external actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The cooldown wrapper executes a supplied command and should only receive trusted commands. <br>
Mitigation: Review commands before passing them to the wrapper and do not pass user-supplied text as a command. <br>
Risk: Workflow state remains on disk and may contain task details. <br>
Mitigation: Avoid storing sensitive task data in workflow state and review local state files before sharing or retaining them. <br>


## Reference(s): <br>
- [Task Structure Schema](references/task_schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dobbybud/skills/agent-task-manager) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and shell script assets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local workflow templates and state files when its scripts are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
