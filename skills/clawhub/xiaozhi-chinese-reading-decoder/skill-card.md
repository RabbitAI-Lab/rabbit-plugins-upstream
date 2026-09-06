## Description:

现代文阅读专项教练：先把文章真正读懂，再把话按阅卷规范说清楚，覆盖记叙文、散文、议论文、说明文和非连续性文本的读法与答题规范。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and tutoring agents use this skill to coach Chinese modern-text reading comprehension for upper-primary and middle-school contexts. It guides students through genuine text understanding, question analysis, evidence-based answer revision, and reading-error reflection without giving original-question answers before the student attempts the work.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: The skill can maintain a student reading profile, which may involve minor learner data and cross-session learning records.

Mitigation: Enable profile memory only with appropriate student or guardian consent, keep cross-skill sharing off unless needed, and preserve pause, delete, export, and correction controls.

Risk: Regional safety and crisis-contact guidance may be inappropriate outside the configured deployment region.

Mitigation: Configure local crisis-contact guidance and guardian-consent requirements before deploying outside the intended China mainland K12 context.

Risk: OCR or image-reading limits can cause incorrect tutoring feedback when article or question images are unclear.

Mitigation: Ask the student to provide the article and questions as text when images are unavailable or unreadable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-reading-decoder)
- [语文错因维度表](references/chinese-error-dimension-table.md)
- [阅读五坑专项训练策略](references/pit-training.md)
- [现代文各题型出题逻辑与答题模板详解](references/question-type-library.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Concise Chinese tutoring dialogue, structured Markdown feedback, and JSON-compatible profile handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are designed for short tutoring turns and may include consent-gated reading-profile update guidance.]

## Skill Version(s):

2.1.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
