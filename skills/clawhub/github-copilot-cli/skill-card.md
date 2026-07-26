## Description: <br>
Efficient daily use of GitHub Copilot CLI for senior engineers. Use when planning, prompting, reviewing, or chaining Copilot CLI commands (gh copilot) to explore codebases, draft changes, debug issues, or accelerate workflows without losing architectural intent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wilsonle](https://clawhub.ai/user/wilsonle) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to plan, prompt, review, and chain GitHub Copilot CLI commands while keeping human control over architecture, risk acceptance, and merge decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest gh copilot commands that operate on code or use the user's authenticated GitHub session. <br>
Mitigation: Review each suggested command before execution, especially commands that modify files or depend on authenticated GitHub access. <br>
Risk: Copilot CLI output can contain incorrect or incomplete implementation guidance. <br>
Mitigation: Use the skill's human-review posture: compare proposals, inspect affected code, and keep final risk acceptance and merge decisions with the developer. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown with inline bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill provides human-reviewed Copilot CLI workflow guidance and command examples.] <br>

## Skill Version(s): <br>
0.1.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
