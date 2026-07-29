## Description: <br>
Structured code reviews with severity-ranked findings and deep multi-agent mode for reviewing code, auditing code quality, and critiquing PRs, MRs, or diffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to run structured code reviews that first verify intent, then examine correctness, maintainability, security, reliability, performance, and test coverage. It supports standard reviews and deeper multi-agent review for larger or higher-risk changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read repository diffs and source code under review, which can include private or sensitive project information. <br>
Mitigation: Use it only in repositories where the selected agent and any configured external reviewers are permitted to process the diff content. <br>
Risk: The skill may propose or classify fixes, including gated changes that cross behavior, API, permission, or contract boundaries. <br>
Mitigation: Keep gated changes under explicit human approval and review proposed changes before applying them. <br>
Risk: Long-running external review agents or test commands may be invoked during deep review workflows. <br>
Mitigation: Confirm the command surface and destination of any external reviewer before use, especially for private codebases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-code-review) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [SPEC.md](artifact/SPEC.md) <br>
- [Action Routing](artifact/references/action-routing.md) <br>
- [Check Categories](artifact/references/check-categories.md) <br>
- [Deep Review](artifact/references/deep-review.md) <br>
- [External Review Subprocess](artifact/references/external-review-subprocess.md) <br>
- [False Positive Suppression](artifact/references/false-positive-suppression.md) <br>
- [Language Profiles](artifact/references/language-profiles.md) <br>
- [PR Sizing](artifact/references/pr-sizing.md) <br>
- [Reliability Patterns](artifact/references/reliability-patterns.md) <br>
- [Review Traps Catalog](artifact/references/review-traps-catalog.md) <br>
- [Scope Resolution](artifact/references/scope-resolution.md) <br>
- [Security Patterns](artifact/references/security-patterns.md) <br>
- [Security Test Coverage](artifact/references/security-test-coverage.md) <br>
- [Severity and Confidence](artifact/references/severity-and-confidence.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review report with severity-ranked findings, evidence, fix guidance, residual risks, and a merge verdict] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include concrete shell commands for scope resolution, test execution, or review verification when appropriate.] <br>

## Skill Version(s): <br>
4.3.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
