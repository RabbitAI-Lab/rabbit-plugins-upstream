## Description:

Supports Chinese middle-school physics teachers in drafting lesson plans organized around physics concepts, laws, models, application practice, classroom summaries, differentiated supports, and question chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators use this skill to draft Chinese middle-school physics lesson plans, including concept-building sequences, model-building activities, differentiated prompts, and teacher-reviewed experiment slots. The skill is intended for lesson planning support and does not replace teacher review, lab safety planning, or classroom judgment.

### Deployment Geography for Use:

China Mainland; other regions require localization of emergency contacts, curriculum alignment, and minor-data consent rules before deployment.

## Known Risks and Mitigations:

Risk: The skill can use persistent class learning records, which may include minor-related educational data.

Mitigation: Deploy only where privacy controls, consent fields, identity confirmation, correction, deletion, pause, sharing-control, and export flows are available and configured.

Risk: Experiment content in lesson plans could be mistaken for ready-to-run lab instructions.

Mitigation: Treat experiment content as teacher-reviewed lesson-planning drafts; require school-specific safety review and use a dedicated physics experiment guidance skill for equipment, procedures, and safety workflows.

Risk: AI-generated questions or lesson materials may contain mistakes.

Mitigation: Keep AI-generated items labeled for teacher verification and require human checking before classroom use, resource-bank entry, or assessment reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-lesson-planner)
- [教案里的实验位模板](artifact/references/lab-design-template.md)
- [初中物理模型案例库](artifact/references/model-examples.md)
- [初中物理概念图谱](artifact/references/physics-concepts-map.md)
- [班级物理档案模板](artifact/references/student-physics-profile-template.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [初中物理实验类型详解](artifact/shared/experiment-types.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown lesson-planning drafts with structured sections, question chains, safety-level labels, and teacher-review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are drafts for teacher review; AI-generated items should be checked before classroom or resource-bank use.]

## Skill Version(s):

2.1.6 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
