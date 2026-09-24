## Description:

智能错题本 helps Chinese K12 students record wrong answers, classify root causes across four common error dimensions, track recurring weak spots, and coordinate deeper subject-specific analysis when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners, guardians, tutors, and tutoring agents use this skill to turn specific wrong answers into structured records, root-cause labels, weak-point counters, review reports, and consent-gated handoffs to subject-specific skills.

### Deployment Geography for Use:

China Mainland by default; localize emergency referral channels, curriculum assumptions, and minor-data consent rules before deployment elsewhere.

## Known Risks and Mitigations:

Risk: The skill handles minors' academic records and wrong-answer history, which can expose sensitive learning patterns.

Mitigation: Confirm who can view the notebook, whether parent-visible summaries are enabled, and whether cross-skill sharing is allowed before using long-term records.

Risk: The skill is designed around Chinese Mainland K12 curricula, consent norms, and crisis referral channels.

Mitigation: Localize curriculum assumptions, emergency contacts, and minor-data consent requirements before use outside China Mainland.

Risk: A student may ask for help during an active exam or timed assessment.

Mitigation: Do not explain or hint on active assessments; ask whether the assessment is over when unclear and resume only for post-exam review.

Risk: Image or OCR failures can cause incorrect problem interpretation and misleading root-cause analysis.

Mitigation: Ask the student to provide or confirm the problem text, known conditions, question, and their answer before recording or analyzing uncertain items.

Risk: Generated practice questions or review exercises can be invalid, off-level, or not aligned to the original mistake.

Mitigation: Self-solve and check generated items for uniqueness, sufficient conditions, grade fit, and alignment with the recorded error type before presenting them.

Risk: Emotional distress or safety signals can be masked as ordinary study pressure.

Mitigation: Stop learning workflows when crisis signals appear, avoid diagnosis, direct the student to a trusted adult and local emergency resources, and avoid storing sensitive incident details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [各科错因判定线索与子类型对照](artifact/references/error-analysis-framework.md)
- [全库统一词表](artifact/shared/vocab.md)
- [提示阶梯与完整示例出口](artifact/shared/hint-ladder.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [危机例外](artifact/shared/crisis-exception.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)
- [交接协议 schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Chinese-language conversational guidance, structured notebook entries, Markdown-style reports, and JSON handoff payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference image/OCR input, cross-session memory, reminder queues, and cross-skill handoff only when the platform and user consent support those capabilities.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
