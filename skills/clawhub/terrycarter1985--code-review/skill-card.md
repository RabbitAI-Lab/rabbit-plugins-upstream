## Description: <br>
Code Review helps agents perform systematic pull request and code reviews across CI status, code quality, security, tests, performance, and maintainability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to review pull requests or changed code, check CI failures, and produce prioritized review feedback. When reviewing the user's own PR, the skill may also guide or perform fixes for failed checks before pushing updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect GitHub pull request and CI state and includes instructions to fix, commit, and push changes on the user's own PRs. <br>
Mitigation: Use explicit read-only review prompts when no changes are desired, and require confirmation before commits, pushes, dependency updates, or CI-remediation actions. <br>
Risk: Review guidance or proposed fixes may be incorrect or incomplete. <br>
Mitigation: Review generated findings and any file changes before relying on them or deploying the reviewed code. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/terrycarter1985/code-review) <br>
- [Detailed review criteria](reference.md) <br>
- [Review examples](examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown review findings with optional inline code snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CI status summaries, prioritized issues, remediation suggestions, and commands for GitHub PR inspection.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
