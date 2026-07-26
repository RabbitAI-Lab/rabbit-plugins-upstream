## Description: <br>
Code Quality provides coding style standards, security guidelines, and accessibility requirements for code generation, debugging, testing, and development workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to generate code, test and debug, review codebases against style and security expectations, and receive issue lists and remediation suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest shell commands that modify files, install packages, deploy code, or use secrets. <br>
Mitigation: Review or constrain proposed commands before execution, especially commands with write access, deployment effects, package installation, or secret handling. <br>
Risk: Quality, security, or accessibility recommendations can be incomplete or misleading when the task lacks a concrete technology stack or review context. <br>
Mitigation: Provide specific project context and review generated code, tests, issue lists, and remediation suggestions before merging or deploying. <br>
Risk: The artifact includes a generic API_KEY environment variable example, which could lead users to expose secrets if copied carelessly. <br>
Mitigation: Use the agent platform or operating system secret-management approach and avoid committing environment variables or credentials to version control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-quality) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured responses with inline code or shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include code files, test results, issue lists, remediation suggestions, and configuration values depending on the agent task.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
