## Description:

Use when crafting TTS, music, or bed prompts for any generative audio model - director style, song structure, and post-production layering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to draft TTS, song, instrumental bed, and audio-layering prompts for generative audio and video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned install commands can fetch a moving package reference.

Mitigation: Review install commands before use and prefer trusted or pinned package references where available.

Risk: Audio workflows can send voice or audio content to Pruna or Replicate and may incur paid API usage.

Mitigation: Confirm before sending audio, avoid sensitive voice or audio content unless intended, and verify credential and cost expectations.

Risk: Post-muxing narration over silent video can truncate voiceover that is longer than the video slot.

Mitigation: Prefer audio-led video generation when narration exists, then probe, shorten, or split TTS lines to fit per-clip duration limits.

## Reference(s):

- [TTS Style Prompting](references/tts-style-prompting.md)
- [Music and Bed Prompting](references/music-and-bed-prompting.md)
- [Audio Post-Production](references/audio-post-production.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with prompt examples, inline shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompts for TTS, music, instrumental beds, narration timing, and audio layering decisions.]

## Skill Version(s):

1.0.11 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
