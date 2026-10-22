## Description:

Reviews skill packages before installation or release, reporting graded security findings, a gate verdict, and package fingerprints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to screen third-party or in-house skills before installation or release and record findings with package hashes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accepted-risk approvals stored inside the scanned package can undermine the gate.

Mitigation: Keep approvals outside the scanned package and require independent review before relying on an accepted risk.

Risk: Batch scanning can fail open when a package has a BLOCK finding.

Mitigation: Do not use batch results as a CI blocker until BLOCK findings reliably fail the batch gate.

Risk: Symlinks can lead scanning outside the intended package.

Mitigation: Contain or reject symlinks before scanning untrusted packages.

Risk: Declared permissions do not match local execution and file access, and include unnecessary WebFetch.

Mitigation: Correct the permission manifest to reflect actual behavior and remove unnecessary WebFetch access.

Risk: A pattern-based PASS does not establish that a skill is secure.

Mitigation: Review source and scan results manually before installation or deployment.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-admission-gate)
- [LGD theory (related project; not verified release provenance)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text scan report; optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes graded findings, a gate verdict, package fingerprint, and file hashes.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; packaged frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
