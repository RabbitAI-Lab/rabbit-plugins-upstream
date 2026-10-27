## Description:

Convert a Simplified-Chinese article in ai-thoughts/docs/ into its Traditional-Chinese twin, and keep the two in sync. The Simplified article is the source of truth and lives as <YYMMDD-slug>-zh-hans.md; the Traditional twin is generated to <YYMMDD-slug>-zh-hant.md with OpenCC (s2twp) plus a permanent cross-link. Use when the user asks to make, sync, or update the Traditional (繁體) version of a Chinese article — "convert to traditional", "做繁體版", "同步繁简", "zh-hant", "繁體". Never runs automatically; acts only on an explicitly named article. Future articles only — do NOT backfill existing files unless the user explicitly orders it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use this skill to create and maintain a Traditional Chinese Markdown counterpart for a specifically selected Simplified Chinese article, while preserving links and reviewing conversion choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OpenCC may choose contextually incorrect Traditional forms, especially in verbatim quotations.

Mitigation: Review converted text against the cited edition and use the documented overrides process for confirmed corrections.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text]

**Output Format:** [Traditional Chinese Markdown file (`-zh-hant.md`) and an updated Simplified Chinese source cross-link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OpenCC s2twp; runs only after explicit user approval for a named article.]

## Skill Version(s):

1.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
