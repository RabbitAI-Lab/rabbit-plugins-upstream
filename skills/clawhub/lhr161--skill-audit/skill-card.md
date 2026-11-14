## Description:

Audit an Agent Skill for spec compliance, security and quality — 0-100 score, A-F grade, file:line findings. Use when reviewing, validating, linting, grading or security-checking a SKILL.md, before publishing or installing a third-party skill. 检查 skill 规范性并评分。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lhr161](https://clawhub.ai/user/lhr161)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill reviewers use this skill to check Agent Skill directories before publishing, installing, or after making changes. It reports a 0–100 score, grade, dimension breakdown, and findings tied to file names and lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a blocker-handling weakness in the audit script, so pass/fail results may not be fully reliable.

Mitigation: Review the reported blocker behavior and findings, and confirm the host runtime's permissions before relying on the audit result.

## Reference(s):

- [Skill Audit on ClawHub](https://clawhub.ai/lhr161/skills/skill-audit)
- [Scoring rubric](references/scoring-rubric.md)
- [Security checks](references/security-checks.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Text or JSON audit report with score, grade, dimension scores, and file:line findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic 0–100 scoring with A–F grades; supports single-skill and batch reports, verbose scoring details, and CI exit codes.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
