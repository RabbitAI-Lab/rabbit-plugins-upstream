## Description:

赛事作品提交合规校验器——基于 UIBC 赛事规范的零依赖决策支持工具，JSON IR 输出，覆盖TH-EVT-001域。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Contest organizers and developers use this skill to check submitted contest artifacts against UIBC submission rules and return advisory JSON results for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI's contest submission result is advisory and may not reflect the final organizer decision or the latest UIBC rules.

Mitigation: Use the JSON result as decision support only and have organizers review the submission against the current contest rules before taking action.

Risk: The interface and messages are Chinese-first, which may affect operators who cannot review the output language confidently.

Mitigation: Have a Chinese-fluent reviewer or localized operating procedure validate outputs before relying on them in contest workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/contest-submission-portal)
- [LGD Theory](https://medxpert.cn/theory)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON IR from a Python CLI, with advisory status codes and warning text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zero-dependency Python command-line execution; outputs rc=0 for pass, rc=1 for warnings, and rc=2 for insufficient input.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
