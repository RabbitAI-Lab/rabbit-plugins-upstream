## Description:

Use when reviewing a new, changed, migrated, or pre-merge RDK Model Zoo sample/demo for repository compliance or delivery completeness across RDK X3, X5, and RDK S branches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxma615](https://clawhub.ai/user/maxma615)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to assess RDK Model Zoo samples and demos for repository standards, delivery completeness, and branch-specific expectations before merge or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review can produce incorrect or incomplete findings when the target branch, sample path, or delivery source is ambiguous.

Mitigation: Provide the exact repository, branch, sample path, and delivery source; require path:line citations or command-output evidence for each finding.

Risk: Verification commands may execute code from an untrusted sample repository.

Mitigation: Review commands and relevant files before running them; do not claim host or board verification unless the command was actually run in the appropriate environment.

## Reference(s):

- [Review Checklist](references/review-checklist.md)
- [Branch and Family Matrix](references/branch-matrix.md)
- [Family Patterns](references/family-patterns.md)
- [Review Report Template](references/review-report-template.md)
- [ClawHub Skill Page](https://clawhub.ai/maxma615/skills/rdk-model-zoo-demo-review)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown review report with findings, passed checks, open questions, verification level, and verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings require path:line citations or command output evidence; verification level must distinguish static review, host verification, board verification, and unverified work.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
