## Description:

Use when crafting TTS, music, or bed prompts for any generative audio model - director style, song structure, and post-production layering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to draft and review prompt guidance for TTS narration, sung music, instrumental beds, and audio layering decisions across generative audio and video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Related-skill install suggestions and provider workflows can lead an agent toward additional tools or paid generation services.

Mitigation: Review related-skill installation suggestions before accepting them, and only provide API keys or upload audio when those services are intended for the task.

Risk: Audio-led video workflows can truncate narration when generated speech exceeds the target model's clip duration.

Mitigation: Probe TTS length before rendering, keep per-scene narration within the documented duration gate, or split long narration into multiple scene rows.

## Reference(s):

- [TTS Style Prompting](references/tts-style-prompting.md)
- [Music and Bed Prompting](references/music-and-bed-prompting.md)
- [Audio Post-Production](references/audio-post-production.md)
- [ClawHub Skill Page](https://clawhub.ai/pruna-ai/skills/audio-prompting)
- [Pruna AI Publisher Profile](https://clawhub.ai/user/pruna-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with prompt text, checklists, tables, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include TTS style prompts, lyrics, music prompts, narration text, mix settings, and related-skill installation guidance.]

## Skill Version(s):

1.0.10 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
