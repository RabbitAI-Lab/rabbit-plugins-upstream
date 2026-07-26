## Description: <br>
Builds automation workflows from repetitive tasks by planning execution steps, handling retries, monitoring progress, and reporting results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and individual builders use this skill to turn repetitive work into structured automation workflows with task planning, conditional execution, retry handling, logs, and status summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may request shell command execution while building or running automation workflows. <br>
Mitigation: Review each planned command before execution and require explicit approval for commands that change files, run jobs, call APIs, or affect user accounts. <br>
Risk: Scheduled jobs, email sending, and API-driven steps can run beyond the user's immediate review if they are not scoped. <br>
Mitigation: Use only non-sensitive accounts unless explicit approval, logging, and schedule limits are configured for the workflow. <br>
Risk: Automation output can be incorrect when the task description is ambiguous or the runtime environment is incomplete. <br>
Mitigation: Validate workflow plans, required environment settings, and final results before relying on them for operational decisions. <br>


## Reference(s): <br>
- [Auto Workflow ClawHub listing](https://clawhub.ai/thcjp/skills/auto-workflow) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped workflow results, execution logs, and optional command or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include workflow plans, status summaries, retry details, scheduled-task guidance, and file or command changes when approved.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
