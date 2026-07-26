## Description: <br>
Reviews pull requests with scope validation, requirements compliance, and line comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review GitHub or GitLab pull requests against stated scope, requirements, version hygiene, and code quality expectations. It produces review findings, comments, and follow-up guidance for issues that should be fixed, suggested, or tracked separately. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use GitHub or GitLab credentials to post PR review comments or create follow-up issues. <br>
Mitigation: Use least-privilege repository credentials and require confirmation before posting comments or creating issues. <br>
Risk: Review findings may be posted or stored outside the immediate pull request through Discussions posting or knowledge capture. <br>
Mitigation: Disable or require explicit confirmation for knowledge capture and Discussions posting before routine use. <br>
Risk: The broad trigger set may invoke the skill in contexts where automatic PR review actions are not intended. <br>
Mitigation: Prefer a narrower explicit trigger such as pr-review and review planned actions before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-pr-review) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) <br>
- [OWASP Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal) <br>
- [Robustness principle](https://en.wikipedia.org/wiki/Robustness_principle) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review reports with inline shell command examples and platform comment guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitHub or GitLab review comments, backlog issue suggestions, and optional knowledge-capture summaries.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
