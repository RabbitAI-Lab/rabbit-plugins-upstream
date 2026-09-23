## Description:

软考高级论文评分与诊断，支持全部 5 个高级资格：系统架构设计师（默认）、信息系统项目管理师、系统分析师、网络规划设计师、系统规划与管理师。当用户提到"帮我评分""给我的论文打分""论文评分""论文自查""论文诊断""看看我论文能得多少分"，或提交了论文内容希望评估时触发，先确认资格类型再执行对应评分标准。不适用于论文写作指导（那是 ruankao-essay-writing 的职责）、纯知识问答或非软考论文场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[nieen](https://clawhub.ai/user/nieen)

### License/Terms of Use:

MIT-0

## Use Case:

External Ruankao advanced-certificate candidates and tutors use this skill to score Chinese practice essays, diagnose weak dimensions, and get prioritized revision guidance against qualification-specific rubrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill declares Write/Edit tools and may revise files or drafts during scoring workflows.

Mitigation: Use Write/Edit only on files or drafts the user intentionally provides for scoring or revision.

Risk: The rubrics are designed for Chinese-language Ruankao advanced essay practice and may not fit other exams or languages.

Mitigation: Use the skill only for Ruankao advanced essay scoring, and route non-Ruankao writing tasks elsewhere.

Risk: Scoring can be inaccurate when the original essay prompt or qualification type is missing.

Mitigation: Ask for the original prompt, including subquestions, and confirm the qualification type before full scoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nieen/skills/ruankao-essay-scoring)
- [Scoring rubric](references/scoring-rubric.md)
- [Project management scoring rubric](references/scoring-rubric-pm.md)
- [Systems analysis scoring rubric](references/scoring-rubric-sa.md)
- [Network planning scoring rubric](references/scoring-rubric-ne.md)
- [Systems planning and management scoring rubric](references/scoring-rubric-sp.md)
- [Scoring report template](references/report-template.md)
- [Common errors and troubleshooting](references/common-errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured Markdown scoring report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the essay prompt and essay text; may ask for the Ruankao qualification type before scoring.]

## Skill Version(s):

1.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
