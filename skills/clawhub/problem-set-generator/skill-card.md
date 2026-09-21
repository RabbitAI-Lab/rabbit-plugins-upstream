## Description:

Generates UIBC contest problem-set drafts as structured JSON decision-support output for the TH-EVT-002 domain.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and developers use this skill to generate draft UIBC contest problems, difficulty variants, warnings, and review metadata. Outputs are decision-support material and require organizing committee review before publication or adjudication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated contest problems may be mistaken for final adjudication or publication-ready material.

Mitigation: Treat outputs as drafts and require organizing committee review before use, as stated in the artifact and security guidance.

Risk: Contest rules or UIBC guidance may change after the artifact was released.

Mitigation: Compare outputs against the latest applicable UIBC rules before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/problem-set-generator)
- [LGD theory reference](https://medxpert.cn/theory)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON IR with rc status, generated problem drafts, warnings, notes, and AIGC metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are draft decision-support material requiring human review.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
