## Description: <br>
Automates code review by retrieving repositories, running code quality checks, and generating structured Markdown review reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinycen](https://clawhub.ai/user/tinycen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review local or remote codebases, run language-specific quality checks, and produce Markdown issue reports with severity levels and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify repositories, write review reports, and commit or push report files in remote workflows. <br>
Mitigation: Use a disposable workspace or read-only repository access unless publishing behavior is explicitly desired; review git changes before any commit or push. <br>
Risk: The skill can install analysis tools and interact with SSH key setup while preparing checks. <br>
Mitigation: Review commands before execution and use scoped credentials that grant only the repository access needed for the review. <br>
Risk: Scheduled workflows can clean local repository state before reviewing updates. <br>
Mitigation: Avoid scheduled runs unless destructive cleanup behavior is understood and limited to disposable clones or controlled workspaces. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tinycen/skills/code-review) <br>
- [Review Process](references/review_process.md) <br>
- [Report Template](references/report_template.md) <br>
- [Repository Access](references/repository_access.md) <br>
- [Installation](references/installation.md) <br>
- [Python Type Checks](references/language_checks/python_type_check.md) <br>
- [Python Dependency Checks](references/language_checks/python_dependency.md) <br>
- [TypeScript and JavaScript Checks](references/language_checks/typescript_javascript_check.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review report with issue details, severity levels, remediation guidance, and optional inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may be saved under docs/code_reviews/ and, in remote workflows, may be committed and pushed when configured.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
