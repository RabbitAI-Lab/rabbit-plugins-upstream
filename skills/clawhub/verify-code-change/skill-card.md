## Description: <br>
Run application to verify code changes meet expectations. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[dkgee](https://clawhub.ai/user/dkgee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to run explicit application or test commands after code changes and review pass, failure, timeout, and log output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided or project-defined test commands can execute arbitrary code in the current project. <br>
Mitigation: Use the skill only in trusted repositories and run explicit verification commands that have been reviewed before execution. <br>
Risk: Long-running tests or applications can hang during verification. <br>
Mitigation: Set an appropriate timeout and increase it only when the expected test duration justifies the change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dkgee/skills/verify-code-change) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal text and logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports command success, failure, timeout, stdout, stderr, and diagnostic suggestions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
