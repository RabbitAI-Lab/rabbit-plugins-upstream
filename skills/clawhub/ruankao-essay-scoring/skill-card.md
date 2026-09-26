## Description:

软考高级论文评分与诊断，支持全部 5 个高级资格：系统架构设计师（默认）、信息系统项目管理师、系统分析师、网络规划设计师、系统规划与管理师。

This skill is ready for commercial/non-commercial use.

## Publisher:

[nieen](https://clawhub.ai/user/nieen)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and exam-preparation users use this skill to score and diagnose Ruankao advanced essay drafts across five qualification tracks, including structure, topic fit, practice depth, expression quality, and pass-line readiness. The skill asks for the exam topic when needed, selects the relevant rubric, and returns a structured scoring report with improvement advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The manifest grants Write/Edit even though the documented scoring workflow only needs to read rubrics, ask clarifying questions, and produce a report.

Mitigation: Keep normal approval boundaries for proposed file edits and treat scoring output as advisory feedback unless the user explicitly requests changes to files.

## Reference(s):

- [Default Architect Scoring Rubric](references/scoring-rubric.md)
- [Project Management Scoring Rubric](references/scoring-rubric-pm.md)
- [System Analyst Scoring Rubric](references/scoring-rubric-sa.md)
- [Network Planning Scoring Rubric](references/scoring-rubric-ne.md)
- [System Planning and Management Scoring Rubric](references/scoring-rubric-sp.md)
- [Scoring Report Template](references/report-template.md)
- [Common Errors and Troubleshooting](references/common-errors.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown scoring report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language essay score, dimension-level diagnosis, seven-question checklist, and prioritized improvement advice]

## Skill Version(s):

1.5.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
