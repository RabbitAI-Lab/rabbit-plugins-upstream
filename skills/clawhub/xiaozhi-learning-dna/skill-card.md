## Description:

在明确授权下，帮助中国大陆中小学生建立、查看、更新、导出和删除长期学习档案，并按需记录学习情绪与成长里程碑。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文 K12 场景的学生及其监护人和教育工作者，在征得适当同意后管理个人学习档案，并为个性化辅导提供受控的学习记录。

### Deployment Geography for Use:

中国大陆（中文 K12 场景）；在其他地区使用前需本地化危机联系方式、课程假设和未成年人同意规则。

## Known Risks and Mitigations:

Risk: Long-term learning and emotion records may expose sensitive information about minors.

Mitigation: Deploy only with per-student isolation, verified identity, applicable guardian consent, field-level sharing controls, and export/deletion support; use only current-session information without consent.

Risk: Crisis referrals or minor-consent procedures may be inappropriate outside the intended locale.

Mitigation: Restrict deployment to Chinese K12 settings until crisis contacts, curriculum assumptions, and consent rules have been localized.

## Reference(s):

- [ClawHub release: 学习DNA](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [学习DNA填写模板](artifact/references/dna-template.md)
- [成长里程碑参考标准](artifact/references/growth-milestones.md)
- [危机识别与转介协议](artifact/references/crisis-referral-protocol.md)
- [学习档案结构与授权说明](artifact/schemas/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational text and structured learning-profile JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term profile use requires consent; sensitive fields and sharing have separate opt-ins.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
