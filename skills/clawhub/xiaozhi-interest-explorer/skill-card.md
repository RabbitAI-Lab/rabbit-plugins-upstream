## Description:

Helps Chinese K-12 students run weekly, consent-gated interest explorations that distinguish shallow likes from sustained interests by tracking how they respond to difficulty.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and education agents use this skill to structure weekly interest exploration for mainland-China Chinese K-12 contexts. The skill records only consented interest signals, compares difficulty responses across weeks, and avoids tutoring, career planning, major recommendations, and admissions advice.

### Deployment Geography for Use:

China mainland by default; localize language, crisis channels, minor-consent requirements, curriculum assumptions, and privacy controls before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill may retain interest records for minors across weeks.

Mitigation: Require the stated student and, where applicable, guardian consent before tracking; without consent, keep the interaction single-session and do not create records.

Risk: Crisis support and minor-consent assumptions are localized for mainland China.

Mitigation: Before using the skill elsewhere, localize emergency channels, consent requirements, privacy controls, and curriculum assumptions; ask the user's region before giving emergency numbers.

Risk: Interest labels could be overread as fixed career, major, or admissions guidance.

Mitigation: Keep outputs as evidence-backed interest signals with confidence labels, avoid professional or admissions recommendations, and avoid conclusions from insufficient samples.

Risk: Parent-facing summaries could disclose sensitive student information.

Mitigation: Generate parent summaries only with the required consent, include factual exploration activity only, and omit emotional judgments or evaluative conclusions unless separately authorized.

Risk: Platform memory or calendar capabilities may be unavailable.

Mitigation: Use the documented degraded mode: provide single-session records and user-saveable templates, and do not promise future recall or proactive reminders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Interest exploration record template](references/interest-exploration-template.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Platform conventions and localization notes](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational guidance with structured interest-record templates and consent-controlled profile fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce student-facing weekly prompts, interest summaries, parent-shareable factual summaries when consented, and handover payloads for profile writeback or reminders.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
