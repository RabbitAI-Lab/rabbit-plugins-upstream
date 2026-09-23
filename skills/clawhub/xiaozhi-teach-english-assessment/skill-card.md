## Description:

英语综合测评帮助英语教师设计听说读写四维测评、依据 CSE 描述语形成能力画像，并生成教学干预建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K12 English teachers use this skill to design comprehensive English assessments, summarize listening, speaking, reading, and writing performance, and prepare teacher-reviewed intervention guidance. It is intended for Chinese-language teaching contexts where teachers confirm any assessment record writeback.

### Deployment Geography for Use:

China mainland education contexts unless localized for local legal, crisis, and curriculum assumptions.

## Known Risks and Mitigations:

Risk: Assessment records can involve real student data and may be written to the class workspace.

Mitigation: Verify consent settings, prefer aliases over real names, and require teacher confirmation before any record writeback.

Risk: The skill is written for Chinese K12 English teaching assumptions and may not fit other legal, crisis-response, or curriculum contexts.

Mitigation: Do not deploy outside the China-mainland curriculum and safety context until local legal, crisis, and curriculum assumptions are reviewed and localized.

Risk: Teachers could overstate ability levels if scores are treated as direct CSE or CEFR conversions.

Mitigation: Use scores to locate strengths and weaknesses, and have teachers assign levels only by comparing evidence with CSE descriptors.

Risk: AI-generated assessment items may contain errors or unsuitable content.

Mitigation: Apply the included AI item self-check and require teacher verification before adding generated items to a resource bank or test paper.

Risk: Unreleased examination materials and personal information are sensitive.

Mitigation: Do not input confidential exam papers, answers, grading standards, or unnecessary personal information into the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment)
- [英语综合测评设计模板](references/assessment-template.md)
- [英语 4 维（听说读写）综合评分细则](references/four-skill-rubric.md)
- ["能做什么"语句与定级流程](references/cefr-can-do-statements.md)
- [CEFR 4 维对照速查](references/cefr-four-skill-descriptors.md)
- [学员能力画像模板](references/student-ability-profile-template.md)
- [教学干预建议样板](references/intervention-suggestion-sample.md)
- [班级教学工作空间 Schema](shared/class-teaching-workspace.schema.json)
- [AI 出题自检协议](shared/ai-item-check.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured teaching-record guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose class-workspace assessment records only after teacher confirmation.]

## Skill Version(s):

2.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
