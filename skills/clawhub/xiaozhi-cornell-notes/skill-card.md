## Description:

把课堂笔记整理成能被再次用上的形式：左栏线索问题 + 右栏内容 + 底部一句话总结，并按学科课题归档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, middle school, and high school use this skill to turn class notes or uploaded note images into Cornell-style study notes, retrieve relevant prior notes, and connect note summaries to review workflows. It is not intended for teaching new material, error analysis, or independent understanding checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent student note memory can retain student learning records beyond the current session.

Mitigation: Deploy only with explicit memory consent and visible controls to view, correct, delete, pause, and export notes; keep long-term writeback to note summary fields rather than full note text.

Risk: OCR or image interpretation can misread handwritten or photographed class notes.

Mitigation: Ask the student to confirm subject and topic before saving, allow correction before final storage, and fall back to typed note bullets when images cannot be read reliably.

Risk: Cross-skill note lookup can surface study-note context outside the student's intended workflow.

Mitigation: Require cross-skill sharing consent, share only minimal relevant summaries, and limit retrieval prompts to the most relevant note entries.

Risk: Reminders, parent sharing, and teacher writeback can affect students or minors if enabled without the right consent.

Mitigation: Require reminder, parent-sharing, and teacher-writeback consent as applicable, and apply age or guardian consent checks before using the skill with younger students.

Risk: Student notes or conversations may contain crisis signals outside the skill's study-support scope.

Mitigation: Use the bundled crisis referral protocol, provide locale-appropriate help resources, and record only the disposition fact rather than sensitive crisis details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Cornell format guide](references/cornell-format-guide.md)
- [Grade bands](shared/grade-bands.md)
- [Platform conventions](shared/platform-conventions.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Learning DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown study-note guidance and structured note summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Cornell cue questions, bottom-line summaries, note tags, retrieval prompts, and consent-gated memory or writeback guidance.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
