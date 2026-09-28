## Description:

Checks an LGD badge certificate's required fields and fingerprint, with an optional local registry match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); MIT for Python code only, with documentation and theory all rights reserved

## Use Case:

Developers and governance teams use this skill to check local LGD badge certificates before relying on badge claims. A passing result does not establish issuer authenticity or revocation status without a trusted registry or stronger signed-certificate workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passing local check can be mistaken for proof that a badge is authentic or not revoked.

Mitigation: Use a trusted registry or stronger signed-certificate workflow and review badge trust decisions before relying on them.

Risk: Using a verification result as an access-control or compliance gate may grant unwarranted trust.

Mitigation: Keep a human review step for consequential decisions and do not treat the current verified result as conclusive proof.

## Reference(s):

- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/lgd-badge-verify)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable verification report or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports check results and a verified flag; command exits 0 on pass and 1 on failure.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled SKILL.md says 1.1.0 and manifest.json says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
