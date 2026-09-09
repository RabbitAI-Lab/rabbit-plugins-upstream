## Description:

Assists teachers for the 49 Days Success Formula training camp with module-by-module assignment review, scoring-table generation, and coaching orientation letter drafting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiongjianchang](https://clawhub.ai/user/xiongjianchang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and training facilitators use this skill to review participant assignments against the provided course rubrics, confirm final comments and scores one module at a time, and produce editable scoring records. It also helps collect confirmed content for a coaching orientation letter before generating a filled PPTX copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Teacher-provided student submissions or company-sensitive course materials may contain sensitive information.

Mitigation: Use the skill only in environments where uploading or processing those materials is appropriate, and limit inputs to the materials needed for the review.

Risk: Generated comments and scores may be incomplete or incorrect if the source submission lacks visible evidence or if a rubric item is misapplied.

Mitigation: Treat all generated comments and scores as drafts; require the teacher to confirm each module's final feedback and score before producing the scoring file.

Risk: The agent could appear to fill gaps in a student's work or a coaching letter when information is missing.

Mitigation: Keep missing evidence explicitly marked as unavailable or pending, and do not invent names, cases, goals, commitments, or student work details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiongjianchang/skills/49-days-teacher-review)
- [Skill definition](artifact/SKILL.md)
- [First-week teacher review rubric](artifact/assets/teacher-source/第一周作业点评要点（教员用）.xlsx)
- [Second-week teacher review rubric](artifact/assets/teacher-source/第二周作业点评要点（教员用）.xlsx)
- [Third-week teacher review rubric](artifact/assets/teacher-source/第三周作业点评要点（教员用）.xlsx)
- [Fourth-week teacher review rubric](artifact/assets/teacher-source/第四周作业点评要点（教员用）.xlsx)
- [Fifth-week teacher review rubric](artifact/assets/teacher-source/第五周作业点评要点（教员用）.xlsx)
- [Graduation scoring sheet, company level](artifact/assets/teacher-source/毕业考评分表（教员用）（公司级）.xlsx)
- [Graduation scoring sheet, department level](artifact/assets/teacher-source/毕业考评分表（教员用）（部门级）.xlsx)
- [Coaching orientation letter template](artifact/assets/teacher-source/教练定向书.pptx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Conversational Markdown plus generated XLSX or PPTX files when all required teacher confirmations are complete]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated comments, scores, and filled templates are drafts for teacher confirmation; the skill is designed to preserve source rubrics and avoid overwriting prior scoring files without explicit authorization.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
