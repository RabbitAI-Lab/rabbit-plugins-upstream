## Description: <br>
Helps physics teachers turn classroom experiments into structured teaching workflows for experiment goals, design, implementation, data handling, conclusions, lab reports, and student experiment profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External physics teachers use this skill to plan, scaffold, and review classroom experiments without delegating real-world experiment execution or final grading to the agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Classroom or extracurricular physics experiment suggestions could be used without adequate safety boundaries. <br>
Mitigation: Require teacher review, safetyLevel labels, adult supervision, and explicit exclusion of hazardous experiments before using any generated plan. <br>
Risk: Electrical experiment examples could be adapted into unsafe home activities. <br>
Mitigation: Do not reuse extracurricular electrical examples unless strict safety limits are added and there is no direct interaction with household mains circuits. <br>
Risk: Rubrics and report examples could be mistaken for automatic grading instructions. <br>
Mitigation: Use rubrics as teacher-only assessment references and require human review before any student-facing feedback or score is recorded. <br>
Risk: Student experiment profiles and lab reports may contain personal or classroom-sensitive information. <br>
Mitigation: Use pseudonyms, remove identifying details from reports, and follow school data-handling rules before storing or sharing outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-experiment-coach) <br>
- [物理实验类型详解](references/experiment-types.md) <br>
- [物理实验数据处理评分](references/data-processing-rubric.md) <br>
- [实验报告评分细则](references/lab-report-template.md) <br>
- [实验设计样板](references/experiment-design-sample.md) <br>
- [数据处理样板](references/data-record-samples.md) <br>
- [实验结论样板](references/conclusion-sample.md) <br>
- [实验报告样板](references/lab-report-sample.md) <br>
- [学员实验能力档案模板](references/student-lab-profile-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-style teaching guidance, rubrics, checklists, and classroom experiment templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Teacher-facing outputs; no API calls, shell commands, credentials, or live experiment execution are produced.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
