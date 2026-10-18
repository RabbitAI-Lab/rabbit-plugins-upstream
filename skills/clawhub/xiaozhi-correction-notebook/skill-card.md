## Description:

帮助学生归档各科错题、定位常见错因，并跟踪反复出现的薄弱知识点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文 K12 学生：记录具体错题、分析错误原因、安排针对性练习，并生成薄弱点与学期复习报告。小学学段应有家长或老师陪同。

### Deployment Geography for Use:

中国大陆；在其他地区使用前须本地化课程、监护人同意要求和危机求助渠道。

## Known Risks and Mitigations:

Risk: Students' wrong-answer histories and parent-visible summaries may disclose sensitive learning information.

Mitigation: Review consent for long-term profiles, cross-skill sharing, reminders, and parent-visible summaries before enabling them; honor pause, correction, export, and deletion requests.

Risk: Mainland China curriculum, consent assumptions, and emergency contacts may be inappropriate elsewhere.

Mitigation: Limit use to the intended Chinese K12 context or localize the curriculum, legal consent assumptions, language, and crisis-support channels first.

Risk: Incomplete problem information can produce unreliable error diagnoses or practice questions.

Mitigation: Confirm the original question and student reasoning, mark uncertain diagnoses as insufficiently supported, and check generated questions before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](references/error-analysis-framework.md)
- [Shared vocabulary and counting rules](shared/vocab.md)
- [Platform and regional conventions](shared/platform-conventions.md)
- [Crisis exception guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational feedback, practice questions, Markdown reports, and structured handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term entries and sharing require consent; reports depend on confirmed records.]

## Skill Version(s):

2.11.2 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
