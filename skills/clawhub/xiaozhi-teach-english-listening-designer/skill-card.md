## Description:

英语听力材料设计 helps teachers design Chinese K12 English-listening lessons with goals, material selection, pre-listening prediction, layered while-listening tasks, post-listening work, micro-skill training, and classroom workspace writeback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn English-listening classes from answer-checking drills into structured lessons with source-aware materials, listening strategies, micro-skill practice, and teacher-reviewed classroom records.

### Deployment Geography for Use:

China mainland by default; other regions require localized safety, privacy, curriculum, and copyright handling.

## Known Risks and Mitigations:

Risk: Generated listening materials or questions may be inaccurate or unsuitable for formal classroom use.

Mitigation: Keep teacher review enabled and require human verification before storing generated items or using them in exams.

Risk: Listening materials may include copyrighted or unauthorized audio or text.

Mitigation: Verify copyrightStatus before storage and keep unauthorized or source-unknown materials out of shared resources.

Risk: Student listening-profile writeback could store classroom data without proper consent.

Mitigation: Only write back student-profile updates when teacherWritebackConsent is present and use low-sensitivity facts rather than real names or evaluative labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-listening-designer)
- [英语听力材料来源清单](references/listening-material-sources.md)
- [听力微技能训练法](references/micro-skill-training.md)
- [英语听力评估评分细则](references/listening-rubric.md)
- [听前预测样板](references/pre-listening-prediction-sample.md)
- [听中任务设计样板](references/while-listening-task-sample.md)
- [学员听力档案模板](references/student-listening-profile-template.md)
- [AI 出题自检协议](shared/ai-item-check.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机例外](shared/crisis-exception.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance and structured classroom workspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated listening items require teacher review; stored materials require copyrightStatus; student-profile writeback requires teacherWritebackConsent.]

## Skill Version(s):

2.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
