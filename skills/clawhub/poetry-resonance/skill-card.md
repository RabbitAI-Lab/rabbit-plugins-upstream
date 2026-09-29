## Description:

Connects Tang and Song poetry with everyday life through daily poem cards, contextual recommendations, plain-language study notes, spaced-repetition review, and reading summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language poetry readers use this skill to connect Tang and Song poems to personal moments, study poems in everyday language, review what they have learned, and export their learning records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saving study notes to ima or Tencent Docs sends content outside the local workspace, despite the skill's broad no-upload privacy claim.

Mitigation: Review the destination and share notes with those services only when you intend to; keep notes local otherwise.

Risk: Optional poetry and weather lookups contact external services.

Mitigation: Set online: false to disable those lookups when network access is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/poetry-resonance)
- [Poetry library](references/poems.md)
- [Poet profiles](references/poets_profile.md)
- [Theme index](references/themes.md)
- [Author's background article](https://mp.weixin.qq.com/s/6cjNWyjWlha-ZuqsNeXY7A)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Chinese-language text and Markdown; optional Anki-compatible CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily poem cards, study notes, review summaries, and optional local study-record exports.]

## Skill Version(s):

1.5.1 (source: release metadata, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
