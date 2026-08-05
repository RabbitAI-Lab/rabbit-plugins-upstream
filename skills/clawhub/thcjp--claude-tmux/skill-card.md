## Description: <br>
Claude Tmux is an instruction-only tmux helper for session and window management guidance in agent terminals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Claude Tmux to get tmux session, window, and troubleshooting guidance inside coding or automation workflows. It is most appropriate where terminal commands and local file operations are acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent into broad terminal, file, and API handling beyond narrowly scoped tmux help. <br>
Mitigation: Review the skill before installing and use it only in workspaces where shell execution, file writes, and API activity are acceptable. <br>
Risk: API-key handling may expose secrets through commands, environment variables, logs, or conversation context. <br>
Mitigation: Keep secrets in environment variables, avoid echoing or logging them, and review proposed commands before execution. <br>


## Reference(s): <br>
- [Claude Tmux ClawHub release page](https://clawhub.ai/thcjp/skills/claude-tmux) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable payload is bundled; outcomes depend on the agent and local tmux environment.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
