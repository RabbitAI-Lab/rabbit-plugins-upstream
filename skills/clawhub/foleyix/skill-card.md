## Description:

Helps create Foleyix prompts for music, songs, speech, ambience, and sound effects, and can generate and download WAV audio on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvyinchao](https://clawhub.ai/user/lvyinchao)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to draft or improve audio prompts and, when requested, generate and retrieve Foleyix audio for music, podcasts, narration, dialogue, ambience, and effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio generation consumes account quota and requires connecting a Foleyix account.

Mitigation: Use prompt-only mode when generation is not requested; check quota before generating and have the user approve account login.

Risk: CLI login stores tokens locally, and downloads or forced replacement can write to a chosen output path.

Mitigation: Keep the local config directory private, review output paths, and allow --force replacement only when intended.

## Reference(s):

- [Foleyix skill homepage](https://foleyix.com/skill)
- [ClawHub skill release](https://clawhub.ai/lvyinchao/skills/foleyix)
- [Audio capabilities](references/audio-capabilities.json)
- [Prompt-writing guide](references/prompt-writing.md)
- [CLI reference](references/cli.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, WAV audio files]

**Output Format:** [Markdown prompts and guidance, JSON task results, or downloaded WAV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only use requires no login; generation requires an account and available quota.]

## Skill Version(s):

1.3.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
