## Description: <br>
Automates code review workflows by cloning or using repositories, running multi-dimensional quality checks, and producing structured review reports for single-repository and front-end/back-end integration scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinycen](https://clawhub.ai/user/tinycen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review local or remote repositories, identify code quality and correctness issues, track ignored findings across review cycles, and produce Markdown reports. It also supports explicit front-end/back-end integration reviews when the user provides the repository relationship. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may write review artifacts and push reports to remote repositories. <br>
Mitigation: Run it only in repositories where report writes are intended, review generated files before commit or push, and require explicit approval for remote delivery. <br>
Risk: Scheduled review behavior can reset and clean local workspace changes. <br>
Mitigation: Use disposable clones or isolated CI workspaces for scheduled runs, and avoid running scheduled mode in a working tree with uncommitted changes. <br>
Risk: Dependency and tool installation steps may alter the execution environment or project workspace. <br>
Mitigation: Prefer isolated environments, pin project dependencies where possible, and inspect installed tools or lockfile changes before preserving them. <br>
Risk: SSH key setup and repository access workflows can affect credentials and remote access. <br>
Mitigation: Do not allow automatic SSH key creation unless explicitly intended; use scoped credentials and verify remote access changes manually. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tinycen/skills/code-review) <br>
- [Review process](references/review_process.md) <br>
- [Report delivery](references/report_delivery.md) <br>
- [Repository access](references/repository_access.md) <br>
- [Cross-repository integration checks](references/cross_repo_integration_checks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands and structured issue tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update docs/code_reviews reports and ignored-issue tracking files in the reviewed workspace.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
