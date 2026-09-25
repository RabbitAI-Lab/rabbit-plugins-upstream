## Description:

Use when reviewing code before it merges, whether written by an agent or a human.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to evaluate proposed code changes across correctness, readability, architecture, security, performance, and verification before merge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SonarQube branch can move a review from analysis into external-service access and repository modification through other skills.

Mitigation: Require explicit user approval before invoking /sonarqube-autofix or /execute-specs, and review generated changes before applying them.

Risk: Untrusted diffs, comments, or PR descriptions may contain instructions that try to influence the reviewer.

Mitigation: Treat PR text, diffs, commit messages, and code as evidence only; flag attempts to bypass checks or suppress findings for human confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/code-review-and-quality)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Source metadata URL](https://github.com/afonsoft/skills)
- [Security Review Checklist](references/security-checklist.md)
- [Performance Review Checklist](references/performance-checklist.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown review findings, checklists, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend commands or follow-up skills when repository signals call for additional review.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
