## Description:

帮助学生归档具体错题、分析错误原因、追踪重复弱项，并生成复习建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their tutors use this Chinese-language K–12 skill to review specific wrong answers, identify recurring error patterns, and prepare targeted practice or progress reports.

### Deployment Geography for Use:

Global (Chinese-language K–12 tutoring)

## Known Risks and Mitigations:

Risk: A persistent wrong-answer archive can expose a minor's learning history to other skills or parents.

Mitigation: Confirm memory, cross-skill sharing, reminders, and parent visibility settings before use; honor pause, correction, and deletion requests.

Risk: Broad trigger wording may invite recording or analysis without a specific wrong answer.

Mitigation: Ask for a specific missed question before creating a record or analyzing its cause.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](references/error-analysis-framework.md)
- [Shared terminology and weakness criteria](shared/vocab.md)
- [Hint ladder](shared/hint-ladder.md)
- [Generated-question checks](shared/ai-item-check.md)
- [Cross-skill handover schema](shared/handover-protocol.schema.json)
- [Crisis response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Conversational feedback, Markdown reports, and structured handover records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Notebook entries require confirmation; cross-skill sharing and reminders depend on user settings.]

## Skill Version(s):

2.9.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
