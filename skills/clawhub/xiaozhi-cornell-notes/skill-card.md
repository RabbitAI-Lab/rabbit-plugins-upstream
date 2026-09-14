## Description:

把课堂笔记整理成可复习的康奈尔笔记：左栏线索问题、右栏课堂内容、底部一句话总结，并按学科、课题和日期归档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in supported K12 grade bands use this skill to turn photographed or typed class notes into Cornell-style study notes, retrieve related notes during review, and receive consent-based note cues through companion learning workflows. When profile storage is enabled, it can summarize note usage without sharing full note text across skills.

### Deployment Geography for Use:

Mainland China Chinese K12 context; curriculum, minor-consent requirements, and crisis referral resources should be localized before deployment elsewhere.

## Known Risks and Mitigations:

Risk: A long-term student note archive may contain sensitive learning data.

Mitigation: Keep profile storage disabled unless intentionally enabled, and preserve view, correction, export, pause, and deletion controls for the student or guardian.

Risk: Cross-skill sharing may exceed the skill's promise to share only aggregate note information.

Mitigation: Limit shared profile updates to extensions.notes.noteCount, extensions.notes.recurringGaps, and extensions.notes.lastUpdated, and require crossSkillSharing consent before handoff.

Risk: Reminder behavior and crisis referral guidance depend on consent and deployment region.

Mitigation: Use reminder workflows only after reminderConsent is enabled, and localize crisis referral contacts before use outside Mainland China.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-cornell-notes)
- [Cornell note format guide](artifact/references/cornell-format-guide.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Grade-band applicability](artifact/shared/grade-bands.md)
- [Learning DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Multi-agent handover schema](artifact/shared/handover-protocol.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text, with JSON-compatible handover fields when profile or reminder workflows are enabled]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports OCR-assisted note intake when available; falls back to typed note points when image recognition or cross-session memory is unavailable.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
