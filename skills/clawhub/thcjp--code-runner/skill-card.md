## Description: <br>
Code Runner helps development teams coordinate batch and concurrent code-execution tasks, CI/CD automation, and execution audit logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to run and coordinate code tasks across projects, generate review or execution reports, and integrate automated work into CI/CD workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Code-execution automation can affect real development workspaces, CI jobs, or multiple repositories. <br>
Mitigation: Review before installing in real development or CI environments, use isolated workspaces, and be especially cautious when running with sudo or root privileges. <br>
Risk: Broad automatic prompt responses and generic password-prompt behavior can approve unintended actions or expose secrets. <br>
Mitigation: Disable or tightly allowlist automatic prompt responses and avoid EXEC_PASSWORD-style generic secret entry. <br>
Risk: Execution audit logs may capture sensitive stdout, stderr, file changes, or task context. <br>
Mitigation: Configure audit logs to redact secrets and reduce retention before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-runner) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with code blocks, shell commands, configuration snippets, and structured result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution status, result data, audit log locations, and improvement guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
