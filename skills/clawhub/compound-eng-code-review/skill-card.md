## Description: <br>
Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing code quality, and critiquing PRs, MRs, or diffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to perform structured code reviews that check intended behavior first, then assess correctness, maintainability, security, reliability, performance, and test coverage. It supports standard reviews and deeper multi-agent review for large or sensitive diffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deep or external review modes may expose repository diffs and PR discussion to local tools, gh, and configured agent or model providers. <br>
Mitigation: Use those modes only when the repository and PR discussion are appropriate for the configured tools and providers. <br>
Risk: Auto-applied safe fixes can still affect the working tree. <br>
Mitigation: Review any auto-applied changes before committing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Skill specification](artifact/SPEC.md) <br>
- [Action Routing](artifact/references/action-routing.md) <br>
- [Deep Review Process](artifact/references/deep-review.md) <br>
- [Scope & comparison-range resolution](artifact/references/scope-resolution.md) <br>
- [Security Detection Patterns](artifact/references/security-patterns.md) <br>
- [Severity Levels and Confidence Rubric](artifact/references/severity-and-confidence.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review reports with severity-ranked findings, residual risks, verdicts, and inline shell commands when verification is needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask scope or review-mode questions; may propose or apply safe local fixes according to the skill's action-routing rules.] <br>

## Skill Version(s): <br>
4.3.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
