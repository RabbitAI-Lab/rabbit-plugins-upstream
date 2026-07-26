## Description: <br>
作业跟进管家 helps independent teachers manage the full homework lifecycle from assignment tracking through completion status, error reflow, persistent weakness flags, next-lesson diagnosis, and student homework profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Independent teachers use this skill to track homework status, route errors back into teaching decisions, and prepare next-lesson diagnostic guidance from homework evidence. The skill supports pseudonymous student records and coordinates with related teaching workspace skills for assignment design, student analysis, lesson logs, dashboards, and parent communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Homework tracking can expose student privacy if real names, contact details, full answers, or family supervision details are entered. <br>
Mitigation: Use pseudonymous records, avoid unnecessary sensitive details, and confirm workspace consent settings before profile creation or cross-skill sharing. <br>
Risk: Automated homework chasing or grading could create inappropriate teacher, student, or parent interactions. <br>
Mitigation: Keep reminder and parent-contact actions teacher-led, and keep scoring decisions with the teacher rather than the skill. <br>
Risk: Shared workspace records can carry incorrect or overly sensitive status information into other teaching workflows. <br>
Mitigation: Record only low-sensitivity progress fields and use the documented view, correct, delete, pause-recording, and cross-skill sharing controls when records need adjustment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker) <br>
- [作业状态追踪模板](references/homework-status-template.md) <br>
- [作业完成度追踪视图模板](references/completion-tracking-views.md) <br>
- [错题回流清单模板](references/error-reflow-checklist-template.md) <br>
- [顽固弱项档案模板](references/persistent-weakness-file-template.md) <br>
- [下节课预诊断输出模板](references/pre-diagnosis-output-template.md) <br>
- [学员作业画像模板](references/student-homework-profile-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown reports and structured workspace update guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses templates for homework status, completion tracking, error reflow, pre-diagnosis, persistent weakness records, and student homework profiles.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
