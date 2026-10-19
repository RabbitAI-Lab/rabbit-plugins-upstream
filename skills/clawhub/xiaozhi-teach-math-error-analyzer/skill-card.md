## Description:

帮助初中和高中数学教师分析作业与测评错题，识别班级和个体的知识薄弱点，并提出教学干预建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use anonymized wrong answers and item scores to identify common error patterns, map weak knowledge points, and draft class-wide or individual teaching interventions for review.

### Deployment Geography for Use:

Chinese Mainland

## Known Risks and Mitigations:

Risk: Student work and error profiles may reveal personal information or be shared beyond the teacher's intended audience.

Mitigation: Use student aliases; obtain consent before record writeback and check permissions before cross-skill or parent sharing.

Risk: Some reference templates describe junior-high scope even when analyzing high-school classes.

Mitigation: Have a math teacher check grade-level fit and review the generated analysis before classroom use.

Risk: Small samples can make class-wide error rates misleading.

Mitigation: Label sampled and whole-class findings separately, and avoid percentages when fewer than ten responses are sampled.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Error classification rubric](artifact/references/error-classification-rubric.md)
- [Knowledge map template](artifact/references/knowledge-map-template.md)
- [Class error report template](artifact/references/class-error-report-template.md)
- [Teaching intervention design](artifact/references/intervention-design.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown reports and teaching recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts for teacher review; sampled findings are distinguished from whole-class results.]

## Skill Version(s):

2.11.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
