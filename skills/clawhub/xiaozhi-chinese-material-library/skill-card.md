## Description:

A Chinese writing-materials library that helps students save tagged quotations, stories, and self-written lines, retrieve relevant materials by theme, and summarize confirmed usage with consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and Chinese-language learning agents use this skill to store writing materials with tags, retrieve 3-5 relevant items for a composition theme, and record only student-confirmed usage counts when sharing is enabled. It is scoped to storing and finding materials, while a separate writing coach leads the full composition workflow.

### Deployment Geography for Use:

China mainland by default; other regions require localized safety resources, curriculum assumptions, and minor-data consent handling before student use.

## Known Risks and Mitigations:

Risk: Student-provided writing notes and usage records may be retained or shared without appropriate controls.

Mitigation: Enable the platform's memory, export, deletion, pause, and cross-skill sharing controls before use; require crossSkillSharing and student consent before writing materialUsage to Learning DNA.

Risk: Younger students may need guardian consent before long-term profiles or cross-skill sharing are used.

Mitigation: Confirm age band and guardian-consent requirements before enabling persistent profiles for小学高段 or younger junior-high students.

Risk: Safety-resource and curriculum assumptions are written for mainland China and may be wrong elsewhere.

Mitigation: Localize crisis resources, curriculum expectations, and minor-data consent rules before deploying outside mainland China.

Risk: The skill may overstate historical counts if cross-session memory or statistics are unavailable.

Mitigation: Use the documented fallback paths: current-session storage only without memory, current-session counts only without statistics, and plain-text export when file export is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Learning DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Crisis exception guidance](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown responses with structured text records and optional JSON handover payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on platform memory, cross-session statistics, and file export capabilities; falls back to current-session text when those controls are unavailable.]

## Skill Version(s):

2.1.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
