## Description: <br>
Code Quality Tool Free helps developers review code style, basic security issues, accessibility checkpoints, and small-project quality guidance through Markdown instructions and command examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, independent maintainers, and small teams use this skill to run quick code-quality checks, review common style conventions, look for simple secret and unsafe-pattern indicators, and produce lightweight remediation guidance before commits or reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect proprietary source code, credentials, or secret-like findings while running quality and security checks. <br>
Mitigation: Run checks on a limited path first, confirm your agent environment keeps code and command output local, and avoid exposing sensitive repositories unless that data handling posture is acceptable. <br>
Risk: The skill can propose shell commands, generated fixes, and git-hook changes that may affect repository behavior. <br>
Mitigation: Review commands and generated changes before execution or installation, and apply fixes deliberately after confirming they match the project context. <br>
Risk: The scanner identified inconsistent privacy and data-flow documentation. <br>
Mitigation: Treat local-only claims as unverified unless the runtime environment and agent configuration explicitly support them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-quality-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, Python, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured report fields such as status, message, data, issue categories, severity, logs, and fix suggestions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
