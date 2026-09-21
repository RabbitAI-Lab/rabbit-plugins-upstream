## Description:

A zero-dependency decision-support CLI that classifies contest anti-cheat identity and environment-consistency signals under UIBC event rules and emits JSON IR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and operations agents use this skill to triage identity and environment-consistency signals for anti-cheat review. Its outputs are decision support only and should be reviewed by a human organizer before any final ruling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contest author IDs and environment fingerprint hashes can be sensitive operational data.

Mitigation: Use the tool only in contest workflows where those inputs are appropriate to process, and prefer hashed environment fingerprints rather than plaintext device or network details.

Risk: Risk labels or warnings could be mistaken for proof of cheating.

Mitigation: Treat labels as triage advice and require human organizer review before penalties, freezes, or final adjudication.

Risk: Contest rules can drift from the UIBC rules assumed by the artifact.

Mitigation: Confirm the current event charter or organizing committee policy before relying on a classification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/anti-cheat-identity)
- [LGD theory reference](https://medxpert.cn/theory)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [JSON, guidance, shell commands]

**Output Format:** [JSON IR from a Python CLI, with risk level, flags, advice, result code, and AIGC metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result codes are 0 for completed checks, 1 for completed checks with warnings, and 2 for insufficient input.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
