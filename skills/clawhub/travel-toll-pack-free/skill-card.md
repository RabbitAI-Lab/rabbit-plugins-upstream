## Description:

A local checker for travel standard and toll expense worksheets that runs two built-in checks per department and reports one conclusion line per department with source file and line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill before monthly or quarterly reimbursement review to check department travel and toll materials for arithmetic, table consistency, duplicates, missing fields, and insufficient evidence. It supports local review workflows but does not replace company policy, tax, audit, or approval decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could treat rule-based arithmetic and table checks as audit, tax, policy, or approval decisions.

Mitigation: Use the output as review support only, and have the appropriate finance, tax, or approval owner make final decisions.

Risk: The free version intentionally excludes some checks and cross-department reporting features.

Mitigation: Review the listed checks that were not run before relying on a clean result for reimbursement review.

Risk: Running the skill on the wrong folder or incomplete department materials can produce insufficient-input results or incomplete review coverage.

Mitigation: Run it only on the intended expense folders or files, with one department per directory and required travel, toll, and vehicle-roster tables included.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/travel-toll-pack-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text stdout by default, with optional JSON output when invoked with --json.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese output; reads selected local files or directories and does not write result files.]

## Skill Version(s):

1.0.18 (source: server release metadata; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
