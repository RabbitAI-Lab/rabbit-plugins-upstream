## Description:

帮助初高中学生将生物错题归类到六个错因维度，并分析反复出现的薄弱点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

面向初高中学生，用于分析已收录的生物错题，定位概念、结构、图表、实验、表述或计算方面的根因，并按需形成弱项报告；错题收录和次数统计由通用错题本负责。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The handover schema permits subjects beyond biology, which could lead to unrelated learning data being handled as biology updates.

Mitigation: Have the host enforce consent and biology-only updates before accepting or sharing handovers.

Risk: Storage and receiving-service behavior was outside the security review.

Mitigation: Confirm those host services enforce the learner's consent choices before enabling saved records, sharing, reminders, or parent summaries.

## Reference(s):

- [ClawHub release: 生物错误DNA 2.12.5](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [生物错因维度表](artifact/references/biology-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance, Structured data]

**Output Format:** [Chinese conversational text, optional weakness reports and plain-text record exports, and consent-gated structured learning-record updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record access, sharing, and updates are consent-controlled; the skill does not diagnose health conditions or give treatment advice.]

## Skill Version(s):

2.12.5 (source: server-resolved release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
