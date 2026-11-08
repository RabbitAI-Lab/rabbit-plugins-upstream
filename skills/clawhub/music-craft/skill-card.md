## Description:

Guides an agent through generating songs, instrumentals, and lyrics-driven tracks with structured prompts and quality checks across available music backends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luischarro](https://clawhub.ai/user/luischarro)

### License/Terms of Use:

MIT-0

## Use Case:

Music creators and developers use the skill to turn a brief, lyrics, or reference audio into structured generation prompts and songs or instrumentals, then review the results for completeness, duration, and lyric alignment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports an unsafe installer pattern in setup guidance.

Mitigation: Review the setup and preflight commands and confirm their effects before executing them.

Risk: Some memory-limit advice could cause system-wide memory pressure.

Mitigation: Check available memory, use a model tier that fits the machine, and avoid changing system-wide memory limits without understanding the impact.

Risk: The bundle includes audio-extraction behavior beyond music generation.

Mitigation: Use extraction helpers only when extraction is intended, and limit them to audio the user has provided and is authorized to process.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/luischarro/skills/music-craft)
- [Project homepage](https://github.com/LuisCharro/skills/tree/main/publish/music-craft)
- [ACE-Step generation guide](references/acestep-generation.md)
- [Setup and preflight guide](references/setup-and-preflight.md)
- [Other music backends](references/other-backends.md)
- [Quality and revision guide](references/quality-and-revision.md)
- [Audio format selection](references/audio-format-selection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Audio files]

**Output Format:** [Structured music prompts and lyrics, backend requests or shell commands, and generated audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio format and duration depend on the selected backend and user request; results may be local or cloud-generated.]

## Skill Version(s):

1.7.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
