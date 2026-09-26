## Description:

帮助中文写作学习者保存并标记素材，按主题找回适用的句子和典故，并在获得同意后记录使用情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向小学高段和初中学生的中文写作学习工具，帮助学生积累、检索和运用写作素材；小学阶段须有家长或老师陪同。

### Deployment Geography for Use:

Mainland China (default; localize before use elsewhere)

## Known Risks and Mitigations:

Risk: Students' saved writing materials and usage history may be shared or retained without their understanding.

Mitigation: Explain memory and sharing controls; honor consent, pause, export, correction, and deletion requests before storing or sharing records.

Risk: Emergency contacts and minor-consent expectations may not fit deployments outside Mainland China.

Mitigation: Localize emergency contacts, curriculum assumptions, and minor-consent requirements before deployment outside Mainland China.

Risk: Cross-session materials and historical usage totals may be unavailable on platforms without persistent memory or statistics.

Mitigation: Tell students when records are session-only, offer a text export, and avoid presenting session totals as historical figures.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Platform and data controls](artifact/shared/platform-conventions.md)
- [Crisis response and regional guidance](artifact/shared/crisis-exception.md)
- [Learning profile schema](artifact/shared/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tagged material lists, suggested writing placements, text exports, and consent-dependent usage summaries.]

## Skill Version(s):

2.6.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
