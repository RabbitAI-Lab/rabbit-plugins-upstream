## Description:

Helps contest organizers calculate weighted rubric scores and review pass-line results for UIBC entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and judges use this skill to score entries against weighted criteria and identify results needing review. It supports decisions but does not replace the organizing committee's final judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Treating a score as an official contest decision.

Mitigation: Have judges review the output; the organizing committee retains final authority.

Risk: Applying an outdated rubric or incorrect pass line.

Mitigation: Confirm criteria, weights, and pass line against current contest rules before use.

Risk: Misreading Chinese-language instructions or output.

Mitigation: Translate and check the full instructions and messages where needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhaoxinghua09-cell/skills/judging-rubric-grader)
- [LGD theory overview](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [JSON scoring result with per-criterion scores, weighted total, grade, pass status, warnings, and return code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inputs are criteria, scores, and an optional pass line; results require human review.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; artifact declares 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
