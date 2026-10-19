## Description:

帮助初高中学生按六类化学错因定位错误根源，记录经确认的弱项并按需生成学习报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向使用中国课程的初高中学生及辅导者，分析化学错题的根本原因、制定弱项练习，并在学生请求时生成错误类型报告。

### Deployment Geography for Use:

Global; designed for the mainland China curriculum, with local adaptation needed elsewhere.

## Known Risks and Mitigations:

Risk: A minor's learning profile could be saved, shared with other skills or parents, or used for reminders without informed consent.

Mitigation: Enable platform consent controls and require the student's applicable permissions before saving, sharing or scheduling reminders.

Risk: China-specific curriculum, crisis contacts and consent assumptions may be unsuitable in other regions.

Mitigation: Adapt curriculum guidance, local emergency resources and minor-data consent rules before using the skill outside mainland China.

Risk: Chemistry experiment guidance could encourage unsafe activity.

Mitigation: Apply the included laboratory safety guidance and avoid directing students to perform hazardous experiments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-error-dna)
- [Chemistry error dimension table](artifact/references/chemistry-error-dimension-table.md)
- [Laboratory safety guidance](artifact/shared/lab-safety.md)
- [Crisis referral guidance](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language explanations and reports, with structured profile and handover data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are on request; profile updates, sharing and reminders require consent.]

## Skill Version(s):

2.11.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
