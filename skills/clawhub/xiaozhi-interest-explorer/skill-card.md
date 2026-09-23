## Description:

用每周一次的中文 K12 兴趣探索，帮助学生通过困难反应、时间感和外部反馈区分浅层喜好与可能的真正兴趣。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students, families, and education operators use this skill to run consent-based weekly interest exploration in Chinese K12 settings. The skill helps record interest signals, compare difficulty responses over time, and produce cautious reflection rather than career, admissions, or academic-placement advice.

### Deployment Geography for Use:

Chinese-language K12 contexts; localize emergency resources, school-stage assumptions, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for Chinese-language K12 use and includes region-specific emergency, school-stage, and minor-consent assumptions.

Mitigation: Localize emergency resources, grade-band assumptions, and guardian-consent rules before deployment in another language, country, or school system.

Risk: The profile schemaVersion migration text is ambiguous and could confuse validation or migration behavior.

Mitigation: Clarify the migration text before relying on profile validation for upgraded long-term records.

Risk: The skill tracks minors' interest records across sessions when long-term memory is enabled.

Mitigation: Require explicit interest-tracking consent, include guardian involvement where required, and honor view, correction, deletion, pause, export, and sharing controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [兴趣探索记录模板](references/interest-exploration-template.md)
- [Learning DNA profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions](shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational guidance and Markdown-style structured interest records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update limited interestDNA fields only after explicit consent; includes downgrade behavior when long-term memory is unavailable.]

## Skill Version(s):

2.2.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
