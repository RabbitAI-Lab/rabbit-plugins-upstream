## Description:

Checks citation-marker coverage in sentences containing numbers or dates and lists sentences missing a source marker when coverage falls below a threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); All rights reserved (documentation and theory)

## Use Case:

Writers, editors, and developers use this skill to spot number- and date-bearing sentences in reports that lack obvious source markers before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The heuristic can miss unsupported non-numeric claims or treat an unverified source marker as sufficient evidence.

Mitigation: Review important claims and verify their underlying sources manually; do not treat the coverage score as fact-checking.

Risk: Scanning unintended files could expose sensitive document text to the local checker.

Mitigation: Limit file access to documents you intend to scan.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/citation-coverage-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage counts, missing-source candidates, and pass/fail exit status.]

## Skill Version(s):

1.0.3 (ClawHub release; bundled SKILL.md states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
