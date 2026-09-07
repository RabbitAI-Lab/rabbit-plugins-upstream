## Description:

Interest Growth Exploration Plan guides Chinese K12 students through weekly, consent-gated interest exploration that distinguishes casual likes from interests that remain compelling when challenges appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners and education platforms use this skill to run weekly interest-exploration conversations, record consented interest-DNA signals, and produce student-facing reflections or optional parent summaries.

### Deployment Geography for Use:

China Mainland by default; other regions require localized crisis contacts, school-system alignment, and minor-data consent review before student use.

## Known Risks and Mitigations:

Risk: Persistent student-profile writes may exceed the intended interest-DNA scope if the receiving platform accepts loosely constrained handoff payloads.

Mitigation: Before persisting anything, enforce current profileEnabled, interestTrackingConsent, crossSkillSharing, exact recipient/type matching, and a strict allowlist for currentExploringFields, challengeReactionSignals, confirmedShallowLikes, and possibleTrueInterests.

Risk: Student interest records or parent-facing summaries may expose minor data without current consent.

Mitigation: Require explicit student consent and the relevant sharing flags before reading records, writing records, cross-skill sharing, or creating parent-visible summaries; keep parent summaries factual and avoid evaluative conclusions.

Risk: Crisis or safety signals in student conversation may require action outside ordinary interest exploration.

Mitigation: Apply the crisis-exception protocol before other flows, avoid recording sensitive details, prompt contact with a trusted adult, and localize emergency contacts before use outside China Mainland.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Interest exploration template](references/interest-exploration-template.md)
- [Platform capability and localization conventions](shared/platform-conventions.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Shared vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Conversational text or Markdown with structured interest-record fields and JSON-compatible handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses persistent records only after consent; otherwise degrades to single-session exploration guidance.]

## Skill Version(s):

2.1.12 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
