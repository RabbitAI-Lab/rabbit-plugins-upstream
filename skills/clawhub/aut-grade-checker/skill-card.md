## Description:

Classifies vehicle driving automation levels from user-supplied decision parameters using GB/T 40429-2021 Table 1 and returns deterministic JSON decision-support output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance reviewers, and vehicle automation teams use this skill to classify automation levels and review responsibility boundaries as decision support. Outputs require human review and are not legal or regulatory proof.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat classification output as legal or regulatory proof.

Mitigation: Require human review and verification against the current official GB/T 40429 text before relying on results.

Risk: The referenced automation-level standard or official interpretation may change after release.

Mitigation: Check the current official standard text and update the decision rules before deployment in regulated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/aut-grade-checker)
- [LGD theory reference](https://medxpert.cn/theory)
- [GB/T 40429-2021 Table 1](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [JSON decision-support output with return codes and warnings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zero-dependency local Python CLI; outputs are deterministic for the supplied parameters and include AIGC metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
