## Description:

Guides Chinese middle-school students through translating math word problems into equations with a three-step quantity-relation modeling process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, tutors, and education agents use this skill to help Chinese middle-school students identify quantities, state relationships in plain language, and convert those relationships into equations. It focuses on equation setup and hands off equation solving, calculation, concept remediation, and non-math physics applications to other skills.

### Deployment Geography for Use:

China Mainland by default; localize crisis contacts, curriculum assumptions, and minor-data consent requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: Optional student learning records and cross-skill profile sharing can expose sensitive learning data if enabled without informed consent.

Mitigation: Use the documented pause, delete, export, correction, and sharing-control phrases; confirm consent before memory or sharing behavior is enabled.

Risk: China Mainland crisis contacts, curriculum framing, and minor-data consent assumptions may be unsuitable in other regions.

Mitigation: Localize emergency contacts, curriculum expectations, and consent rules before deploying outside China Mainland; if region is unknown, ask for the user's location before giving hotline numbers.

Risk: Generated practice or transfer problems can be mathematically invalid or outside the intended grade band.

Mitigation: Apply the bundled item self-check before presenting generated problems and mark teacher-facing generated items for human verification.

Risk: Unclear images or missing OCR support can lead to incorrect modeling guidance.

Mitigation: When an image is unclear or unavailable, ask the learner to type the known conditions and question before giving modeling help.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-word-problem-coach)
- [五大应用题题型建模框架与数量关系速查表](artifact/references/modeling-patterns.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Markdown tutoring guidance in Simplified Chinese]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include short prompts, equation setup scaffolds, same-type worked examples, session summaries, privacy-control responses, and handoff guidance.]

## Skill Version(s):

2.1.6 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
