## Description: <br>
Structured Task Planning V2 helps an agent decompose a user task into confirmed steps, then run each step through asynchronous execution and verification subagents with heartbeat status tracking and interruption support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scotthuang](https://clawhub.ai/user/scotthuang) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to plan multi-step work, require user confirmation before execution, and keep the main session responsive while subagents execute and verify each step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spawn subagents and schedule recurring heartbeat jobs, which may leave background work running if a plan is approved without review. <br>
Mitigation: Use explicit /stp invocation, review the generated plan before confirmation, and interrupt the task if background execution should stop. <br>
Risk: The skill can inspect OpenClaw session history and perform cleanup that may terminate work or delete task records. <br>
Mitigation: Avoid placing sensitive data in task prompts and do not enable completion cleanup unless losing the task directory is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scotthuang/skills/stp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown plans and status text with inline shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates task plan/status files for step tracking when used in OpenClaw.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
