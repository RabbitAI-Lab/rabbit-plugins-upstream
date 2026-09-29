## Description:

Helps contest reviewers compare a submission fingerprint with known fingerprints and assess potential duplication for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and reviewers use this skill to flag exact or similar submission fingerprints for further originality review, not to make final adjudications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Illustrative hash-similarity results may be mistaken for a definitive originality finding.

Mitigation: Treat matches as advisory and require human review before any contest decision.

Risk: Chinese-language documentation and unclear bundled license terms may impede review or redistribution.

Mitigation: Confirm the documentation is usable for the team and resolve license terms before redistribution.

## Reference(s):

- [Originality Check on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/originality-check)
- [LGD theory background](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON decision-support result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes similarity, duplicate and exact-match flags, up to five matches, warnings or errors, and a return code.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
