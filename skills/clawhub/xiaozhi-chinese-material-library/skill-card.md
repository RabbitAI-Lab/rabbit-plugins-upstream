## Description:

语文素材库 helps Chinese-language K12 learners store, tag, retrieve, and review writing materials for composition and reading workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 learners, parents, teachers, and tutoring agents use this skill to collect writing素材, retrieve relevant examples by theme, and export or summarize saved material. It supports composition preparation and reading or classical-Chinese study without taking over the full writing-coach workflow.

### Deployment Geography for Use:

Mainland China by default for Chinese-language K12 use; other regions require localized emergency contacts, curriculum assumptions, and minor-consent requirements before deployment.

## Known Risks and Mitigations:

Risk: The skill is intended for minors and can retain student-provided writing materials or usage counts when memory and sharing are enabled.

Mitigation: Use it only in an appropriate Chinese-language K12 learning context, obtain required parent or teacher involvement, and honor view, correct, delete, pause, sharing, and export controls.

Risk: Emergency contacts, curriculum assumptions, and minor-consent expectations are China-specific by default.

Mitigation: Before use outside mainland China, localize emergency contacts, curriculum assumptions, and consent requirements.

Risk: Stored素材 can include uncertain sources or student-created text that should not be treated as verified citation material.

Mitigation: Keep uncertain sources marked for student confirmation and avoid inventing provenance when the source is unknown.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Conversational Markdown and plain text, with optional structured JSON profile writeback records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce material lists, tag suggestions, retrieval recommendations, exports, monthly summaries, and consent-gated usage-count updates.]

## Skill Version(s):

2.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
