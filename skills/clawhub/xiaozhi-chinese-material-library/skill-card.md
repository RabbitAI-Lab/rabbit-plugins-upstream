## Description:

Stores, tags, retrieves, and summarizes Chinese-language writing materials so students can find relevant quotes, stories, and self-written lines when preparing essays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language students, especially upper-primary and middle-school learners, use this skill to save useful writing materials, retrieve 3-5 relevant entries by theme, and review monthly material usage. Tutoring agents can call it during writing workflows to fetch materials, then return control to the writing coach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may retain a student's writing materials and usage history across sessions.

Mitigation: Use the documented view, correct, delete, pause memory, sharing-control, and export controls; for minors, confirm guardian consent before enabling long-term memory.

Risk: Crisis referral resources bundled with the skill are oriented to mainland China.

Mitigation: Replace hotline and emergency guidance with local resources before deployment outside mainland China, while preserving the immediate escalation behavior for safety risks.

Risk: Suggested sources, tags, or writing-use recommendations can be incorrect.

Mitigation: Keep uncertain sources marked as pending confirmation and ask the student to confirm or correct tags before relying on stored entries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Learning DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [artifact/shared/dna-profile.schema.json](artifact/shared/dna-profile.schema.json)
- [artifact/shared/handover-protocol.schema.json](artifact/shared/handover-protocol.schema.json)
- [artifact/shared/platform-conventions.md](artifact/shared/platform-conventions.md)
- [artifact/shared/crisis-referral-protocol.md](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, configuration, guidance]

**Output Format:** [Chinese-language conversational responses with structured material entries, retrieval lists, usage summaries, and JSON handover/profile writeback payloads when coordinating with other skills.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires memory/profile capability for cross-session storage, statistics capability for historical monthly summaries, and file capability for export; otherwise it falls back to current-session text output.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
