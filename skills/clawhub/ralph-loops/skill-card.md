## Description: <br>
Runs autonomous iterative AI loops for requirements, planning, or building phases using structured prompts and fresh context per iteration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qlifebot-coder](https://clawhub.ai/user/qlifebot-coder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to run structured autonomous loops that gather requirements, produce implementation plans, and build one task per iteration with fresh context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority to edit files, run commands, commit changes, and push remotely. <br>
Mitigation: Run it only in an isolated repository or VM with minimal credentials, and review or disable automatic push and tag behavior before use. <br>
Risk: Autonomous operation relies on bypassing normal permission prompts. <br>
Mitigation: Review the prompts and templates before running, scope the workspace narrowly, and keep only task-required API keys available. <br>
Risk: The dashboard exposes loop controls and status and is not described as authenticated. <br>
Mitigation: Keep the dashboard local and do not expose it to a network without authentication. <br>


## Reference(s): <br>
- [Ralph Loops on ClawHub](https://clawhub.ai/qlifebot-coder/skills/ralph-loops) <br>
- [Geoffrey Huntley: Ralph](https://ghuntley.com/ralph/) <br>
- [Clayton Farr Ralph Playbook](https://github.com/ClaytonFarr/ralph-playbook) <br>
- [Geoffrey Huntley Ralph Wiggum Fork](https://github.com/ghuntley/how-to-ralph-wiggum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, prompt templates, JavaScript utilities, and dashboard files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can generate requirements specs, implementation plans, code changes, validation steps, commits, and loop status summaries.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
