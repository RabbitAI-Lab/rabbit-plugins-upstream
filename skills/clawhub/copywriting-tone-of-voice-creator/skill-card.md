## Description:

Builds or adapts a machine-readable TONE.md brand voice guide using discovery questions, voice attributes, tone modulation, lexicon, mechanics, and channel rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Brand, marketing, content, and developer teams use this skill to create or adapt a TONE.md guide that downstream writing agents can consume for consistent brand voice across channels. It is suited for creating a new tone-of-voice system, refreshing an existing one, or adapting a guide to a specific channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local SOUL.md or TONE.md files can contain sensitive brand strategy or stakeholder information.

Mitigation: Keep unrelated sensitive material out of those files and review generated voice guidance before sharing or using it downstream.

Risk: Research for unusual or regulated categories can introduce stale, incomplete, or context-specific guidance.

Mitigation: Verify research-derived claims and category constraints against current primary sources before committing them to TONE.md.

Risk: A generated tone guide can encode misleading brand, regulatory, or audience assumptions if discovery inputs are incomplete.

Mitigation: Have the responsible brand or content owner review the final TONE.md before using it as input to writing agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/copywriting-tone-of-voice-creator)
- [OpenClaw homepage](https://github.com/samber/cc-skills)
- [TONE.md template](artifact/assets/TONE-template.md)
- [Discovery Questionnaire](artifact/references/discovery-questionnaire.md)
- [Category Adaptations](artifact/references/category-adaptations.md)
- [Channel Adaptations](artifact/references/channel-adaptations.md)
- [Voice Attributes](artifact/references/voice-attributes.md)
- [Lexicon and Mechanics](artifact/references/lexicon-mechanics.md)
- [Reference Brands](artifact/references/reference-brands.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown file, typically TONE.md or a channel-specific TONE file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May incorporate user discovery answers, an existing TONE.md, an optional SOUL.md, and bounded web research for uncovered or regulated categories.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
