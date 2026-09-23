## Description:

英语写作进化教练为中文 K12 学生提供整段或整篇英语写作反馈，从语法、用词和逻辑三个维度指出核心问题，并用追问引导学生自己修改。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 students and their teachers or guardians use this skill to review full English paragraphs or essays, prioritize a small number of grammar, vocabulary, and logic improvements, and practice revision through guided prompts rather than direct rewriting.

### Deployment Geography for Use:

Chinese mainland K12 context by default; localize curriculum assumptions, emergency resources, and minor-data consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for simplified-Chinese mainland-China K12 English-writing support and includes region-specific curriculum, emergency-resource, and minor-data consent assumptions.

Mitigation: Install it only in that intended context unless curriculum mappings, emergency contacts, and consent rules are localized and reviewed.

Risk: Student writing or conversation may include self-harm, bullying, family-safety, or severe-distress signals that are outside ordinary writing coaching.

Mitigation: Follow the crisis-exception path: stop the learning flow, avoid diagnosis, direct the student to a trusted adult and local emergency help, and record only limited referral facts when profile storage is already enabled.

Risk: Writing profiles and cross-skill sharing can create long-term records about minors.

Mitigation: Enable profile use only with appropriate consent, review sharing permissions, and keep view, correction, deletion, pause, sharing-control, and export controls available.

Risk: Feedback may become misleading if OCR, persistent memory, or cross-session statistics are unavailable but the agent implies those capabilities exist.

Mitigation: Apply the documented degradation paths: ask for typed text when OCR is unavailable, avoid ungrounded historical counts, and do not promise memory or reminders without platform support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-writing-coach)
- [低阶→精准词汇升级对照表](artifact/references/vocabulary-upgrade.md)
- [英语错因维度表](artifact/shared/english-error-dimension-table.md)
- [危机例外](artifact/shared/crisis-exception.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown/text coaching responses with structured feedback, revision prompts, progress summaries, and consent-gated profile handoff examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not produce executable code or shell commands; long-term writing records and cross-skill sharing are consent-gated.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
