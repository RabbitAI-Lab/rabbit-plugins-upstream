## Description:

求职简历三阶段优化引擎+效果对比报告：先全局评估（含JD匹配度雷达图），再简历改写（工作经验STAR+项目经验软性叙述+数据补全追问），最后效果对比+Word/PDF导出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tuobadaidai](https://clawhub.ai/user/tuobadaidai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents assisting job seekers use this skill to evaluate resumes against optional job descriptions, rewrite resume sections with STAR, JD-tailoring, and ATS guidance, and produce comparison reports plus optional DOCX/PDF exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export helper writes generated resume files and has insufficiently constrained file-writing behavior.

Mitigation: Use the skill only in a controlled workspace, avoid shared directories for sensitive resumes, and choose plain output filenames without slashes or '..'.

Risk: The export helper uses unpinned document-export dependencies.

Mitigation: Pin and audit python-docx and reportlab before running the export helper.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tuobadaidai/skills/resume-optimizer)
- [ATS 兼容性优化指南](references/ats-optimization.md)
- [JD 定向定制方法](references/jd-tailoring.md)
- [STAR 方法论与强动词库](references/star-methodology.md)
- [边界场景与容错处理](references/edge-cases.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, files, guidance]

**Output Format:** [Markdown reports and rewritten resume content; optional DOCX/PDF files from an export helper.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces resume evaluations, JD keyword mappings, before/after rewrites, score comparisons, radar-chart guidance, and optional export commands.]

## Skill Version(s):

1.5.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
