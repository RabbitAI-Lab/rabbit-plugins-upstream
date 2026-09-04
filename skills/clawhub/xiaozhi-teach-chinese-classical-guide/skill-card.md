## Description:

面向语文老师的文言文与古诗词教学设计工具，支持诵读正音、训诂、串讲框架、主题讨论、文化背景联结和班级古文积累记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language teachers use this skill to design classical Chinese and poetry lessons for upper-primary and middle-school learners. It produces teaching frameworks, discussion prompts, recitation and exegesis guidance, homework suggestions, and class-record updates while leaving full translation, line-by-line exposition, and grading decisions to the teacher.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent class records could be saved or shared without the intended consent settings.

Mitigation: Confirm classWorkspace writeback, parent-sharing, and student-consent settings before saving or sharing records.

Risk: AI-generated lesson or homework items may contain inaccuracies or unsuitable examples.

Mitigation: Require teacher review before using generated lesson content, homework entries, or resource-library items.

Risk: Crisis-support resources in the package are specific to Mainland China and may not fit other regions.

Mitigation: Replace hotline and referral guidance with locally valid emergency and professional-support resources before classroom use outside Mainland China.

Risk: Textbook annotations, translations, teaching-aid questions, and exam items may be copyright-protected even when source classical texts are public domain.

Mitigation: Use framework-level guidance, avoid copying protected materials, and preserve copyrightStatus labeling for cited or adapted resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-classical-guide)
- [Classical accumulation profile template](artifact/references/classical-accumulation-profile-template.md)
- [Classical vocabulary quick reference](artifact/references/classical-vocab-quick-ref.md)
- [Exegesis method card](artifact/references/exegesis-method-card.md)
- [Poetry image catalog](artifact/references/poetry-image-catalog.md)
- [Recitation rhythm guide](artifact/references/recitation-rhythm-guide.md)
- [Serial explanation sample template](artifact/references/serial-explain-sample-template.md)
- [Theme discussion question bank](artifact/references/theme-discussion-question-bank.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Shared vocabulary](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-compatible classWorkspace record structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include teaching frameworks, discussion questions, recitation plans, homework suggestions, and class-record updates for teacher review.]

## Skill Version(s):

2.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
