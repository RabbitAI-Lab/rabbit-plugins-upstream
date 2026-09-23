## Description:

A Chinese K12 physics learning-profile skill that analyzes middle-school through first-year high-school physics mistakes, classifies root causes across five physics-specific dimensions, and produces weakness reports and follow-up guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, teachers, and learning-support agents use this skill to turn repeated physics mistakes into a structured profile of root causes, weak areas, and next-step practice guidance. It is designed for Chinese Mainland K12 physics contexts, mainly junior high and first-year high-school compulsory physics content.

### Deployment Geography for Use:

Chinese Mainland unless language, curriculum, crisis resources, and minor-consent rules are localized.

## Known Risks and Mitigations:

Risk: The skill is designed around Chinese Mainland curriculum, simplified Chinese interaction, crisis resources, and minor-consent assumptions.

Mitigation: Deploy directly only in that context; localize curriculum, language, crisis referral channels, and minor-consent rules before using it elsewhere.

Risk: The skill can work with a minor student's long-term learning profile, parent-sharing choices, cross-skill sharing, deletion/export requests, and reminder preferences.

Mitigation: Require the host platform to enforce explicit consent gates, identity checks in shared conversations, deletion/export controls, and reminder enqueueing permissions.

Risk: Physics anxiety conversations can reveal self-harm, severe distress, bullying, abuse, or family-safety concerns.

Mitigation: Stop learning workflows when crisis signals appear, avoid recording sensitive details, and route to trusted adults and localized emergency or support channels.

Risk: Generated practice items or diagnostics may be wrong, too advanced, or inconsistent with the student's grade band.

Mitigation: Apply the bundled item self-check before presenting generated questions and mark teacher-facing AI-generated items for human verification before reuse.

Risk: Historical counts, trends, or reminders may be misleading if platform memory, statistics, OCR, or scheduling capabilities are unavailable.

Mitigation: Use the documented degradation path: avoid exact historical claims without platform support, label sample limits, ask for text when OCR is unavailable, and do not promise proactive reminders.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-error-dna)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Physics error dimension table](artifact/references/physics-error-dimension-table.md)
- [Physics concept confusion map](artifact/references/physics-concept-confusion-map.md)
- [Physics math tools checklist](artifact/references/physics-math-tools-checklist.md)
- [Physics diagram guide](artifact/shared/physics-diagram-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese Markdown guidance with structured profile fields and consent-aware handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate weakness reports, error-type maps, monthly summaries, practice recommendations, consent-gated parent summaries, reminder handoffs, and profile export text.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
