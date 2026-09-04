## Description:

A Chinese-language English writing coach that gives grammar, vocabulary, and logic feedback on paragraphs or essays, then uses prompts to help students revise their own writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students in upper primary and middle school use this skill to improve English writing through targeted feedback, revision prompts, sentence-pattern upgrades, and scenario-based practice. Education agents may use it to guide consent-gated writing-profile updates and progress reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide writing-profile updates, cross-skill sharing, reminders, parent-visible summaries, and OCR-assisted essay intake.

Mitigation: Enable those behaviors only when the student's and guardian's consent settings allow them; otherwise keep feedback within the current conversation and ask the student to paste text when OCR is unavailable or inappropriate.

Risk: The bundled crisis-contact guidance is tailored to mainland China.

Mitigation: For deployments outside mainland China, replace crisis and emergency contact numbers with current local resources before use.

Risk: Students could become dependent on complete rewrites instead of learning to revise.

Mitigation: Keep the skill's prompt-first posture: identify a small number of concrete issues, use hints before examples, and avoid writing arguments, paragraphs, or essays for the student.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-writing-coach)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [Vocabulary Upgrade Reference](artifact/references/vocabulary-upgrade.md)
- [English Error Dimension Table](artifact/shared/english-error-dimension-table.md)
- [Platform Capability Conventions](artifact/shared/platform-conventions.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown or plain-text coaching responses with optional structured profile handoff examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language student-facing output; consent-gated profile updates; no executable output.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
