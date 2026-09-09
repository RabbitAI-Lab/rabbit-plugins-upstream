## Description:

Reviews working-tree or branch code changes for production readiness, including correctness, DRY issues, tests, security, build health, and actionable findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review uncommitted changes, pull requests, or branches before release. It produces prioritized findings and asks for permission before applying fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review-like requests may trigger repository inspection and test or build execution.

Mitigation: Confirm the intended review scope before using the skill for lightweight advice.

Risk: Branch reviews may fetch the configured base branch remote.

Mitigation: Use branch-scope review only when remote fetch activity is acceptable for the repository.

Risk: Automated review output can include incorrect or incomplete recommendations.

Mitigation: Treat findings as proposals and review them before applying any suggested fix.

## Reference(s):

- [Branch Review Reference](references/branch-review.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with findings, command results, and recommended fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are categorized as blocking, suggestion, question, nit, or praise; fixes require explicit user permission.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
