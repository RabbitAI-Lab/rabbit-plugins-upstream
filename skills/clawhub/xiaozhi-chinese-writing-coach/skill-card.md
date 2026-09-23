## Description:

语文写作教练 helps Chinese K12 learners develop their own作文思路, drafts, and revisions through a five-step coaching flow, genre-specific feedback, Socratic questioning, debate practice, and consent-gated writing-style profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, guardians, and teachers use this skill to coach Chinese composition for upper-primary and middle-school learners. It opens ideas, checks outlines and drafts, supports narration, argument, exposition, and debate practice, and avoids ghostwriting by keeping the student's own words central.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for K12 learners and may handle minors' writing, profile data, and learning summaries.

Mitigation: Use it only in Chinese-language K12 writing-coaching contexts with guardian or teacher oversight for younger students, and enforce the documented consent gates before profile reads, writes, cross-skill sharing, or parent-visible summaries.

Risk: Writing-style and grammar-profile records could be retained or shared without the student's intended consent if platform permissions are misconfigured.

Mitigation: Confirm that profileEnabled, crossSkillSharing, parentSharingConsent, and writeback permissions are checked before each relevant action, and treat lack of consent as no permission to read, write, or share.

Risk: Student writing can include self-harm, bullying, family-safety, or severe-distress signals outside normal learning support.

Mitigation: Stop the writing workflow when crisis signals appear, avoid storing sensitive details, and follow the bundled crisis referral path to encourage immediate support from trusted adults or local emergency channels.

Risk: The skill could be misused to ghostwrite assignments or assist during exams.

Mitigation: Keep the output to prompts, feedback, and direction rather than finished essay text; refuse active exam or test help and invite the student to return after the assessment for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-writing-coach)
- [写作5步流程 · 状态机定义](references/writing-5step-statemachine.md)
- [三文体批改维度与追问问题库](references/writing-rubric.md)
- [AI 辩论赛话术与赛制详解](references/debate-script-guide.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [危机例外](shared/crisis-exception.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)
- [学习DNA 档案结构](shared/dna-profile.schema.json)
- [交接协议结构](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Conversational Markdown with optional structured profile handoff JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps draft authorship with the student, uses consent-gated profile reads and writes, and routes suspected grammar issues or crisis signals to the appropriate companion workflow.]

## Skill Version(s):

2.2.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
