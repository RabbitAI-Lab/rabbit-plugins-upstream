## Description:

Checks the chronological order, subject consistency, and linked hashes of an electronic evidence chain supplied as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: All rights reserved

## Use Case:

Developers and evidence reviewers use this skill to check a supplied electronic evidence chain for ordering, subject, and hash-link inconsistencies before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An evidence-chain consistency result could be mistaken for a legal determination.

Mitigation: Treat the result as a preliminary check and seek qualified human review for legal decisions.

Risk: Evidence-chain JSON may contain sensitive case information.

Mitigation: Provide only intentionally selected data and prefer running the local script without broad workspace access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable check result or JSON consistency report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports breaks, completeness, and subjects in JSON mode; exit status 0 for complete, 1 for detected breaks, or 2 for input errors.]

## Skill Version(s):

1.0.3 (source: ClawHub release; artifact version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
