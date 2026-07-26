## Description: <br>
Sofagent adds workflow guardrails, reflection, task decomposition, and closure checks to help agents stay aligned on complex or risky tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kongfangxun](https://clawhub.ai/user/kongfangxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add behavioral constraints, risk gates, task planning, local reflection notes, and completion checks for multi-step agent work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may persist task history and internal reflections to local files, which can capture sensitive prompts or project context. <br>
Mitigation: Use it only in trusted workspaces, review generated local logs and reflection notes, and constrain or disable persistence for sensitive work. <br>
Risk: The skill may reuse cached workflow plans and fetch role templates from GitHub. <br>
Mitigation: Review external templates and cached plans before acting on them, and require user confirmation for network access or cache reuse. <br>
Risk: The skill references local check scripts and shell or PowerShell commands. <br>
Mitigation: Allowlist scripts, inspect commands before execution, and require confirmation for destructive or privileged operations. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/kongfangxun/skills/sofagent-publish) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Task awareness workflow](artifact/task-aware.md) <br>
- [Loop check workflow](artifact/loop-check.md) <br>
- [FDE configuration template](artifact/data/fde.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell and PowerShell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to read or write local workflow state such as task logs, reflection notes, scoring records, and orchestration plans.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
