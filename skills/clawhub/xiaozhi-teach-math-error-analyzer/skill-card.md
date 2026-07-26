## Description: <br>
Helps math teachers turn wrong-answer review into structured class and student error analysis by classifying mistakes, linking them to a knowledge map, and producing teaching intervention suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External math teachers use this skill to analyze homework, test, or classroom mistakes across a class and individual students. It produces error categories, knowledge-map links, class and student profiles, and intervention suggestions for teacher review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Student performance data or real names could be exposed in reports or downstream profiles. <br>
Mitigation: Use aliases or student IDs by default, avoid real names unless authorized, and review reports before sharing or writing them to downstream systems. <br>
Risk: Error analysis and intervention suggestions could be mistaken for grading, ranking, or final teaching decisions. <br>
Mitigation: Keep outputs as teacher-reviewed analysis and suggestions; do not use the skill to replace teacher grading, rank students, or make unsupervised instructional decisions. <br>
Risk: Cross-skill handoff fields could fail or lose meaning if the seven teacher-side error categories are not mapped to the supported four-category schema. <br>
Mitigation: Map teacher-side categories to the documented standard categories before writing data into downstream student-analysis or handoff workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer) <br>
- [Error Classification Rubric](references/error-classification-rubric.md) <br>
- [Knowledge Map Template](references/knowledge-map-template.md) <br>
- [Intervention Design Template](references/intervention-design.md) <br>
- [Class Error Report Template](references/class-error-report-template.md) <br>
- [Student Error Profile Template](references/student-error-profile-template.md) <br>
- [Error-Knowledge Link Template](references/error-knowledge-link-template.md) <br>
- [Intervention Report Template](references/intervention-report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Analysis, Guidance, Files] <br>
**Output Format:** [Markdown reports, structured teaching profiles, and text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses teacher-provided mistake data and should use aliases or IDs for student records.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
