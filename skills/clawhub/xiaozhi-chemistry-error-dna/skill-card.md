## Description:

Analyzes chemistry mistakes across six dimensions, identifies recurring root causes, and produces targeted learning profiles and weakness reports for secondary-school students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to diagnose chemistry errors, track recurring weak areas, and request tailored practice or progress summaries. Persistent profiles and sharing require student consent.

### Deployment Geography for Use:

Mainland China (Simplified Chinese K–12 context); localize safety contacts, curriculum, and consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The memory-pause control may not prevent student-profile reads, writebacks, reminders, or persistent cross-skill handovers.

Mitigation: Enforce the pause outside the skill or update it so memoryPaused=true blocks all persistent profile access and handovers before deployment.

Risk: Mainland China-specific crisis contacts, curriculum assumptions, and consent rules may mislead users elsewhere.

Mitigation: Use in the intended Simplified Chinese Mainland China K–12 setting, or localize contacts, curriculum, and consent requirements first.

## Reference(s):

- [Chemistry error dimension table](references/chemistry-error-dimension-table.md)
- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-error-dna)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language diagnostic guidance and progress summaries; structured profile and handover data when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses confirmed student answers for persistent updates; historical reports depend on available, authorized profile data.]

## Skill Version(s):

2.4.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
