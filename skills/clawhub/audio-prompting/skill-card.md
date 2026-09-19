## Description:

Use when crafting TTS, music, or bed prompts for any generative audio model - director style, song structure, and post-production layering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers and content teams use this skill to craft prompts for TTS narration, songs, instrumental beds, and audio/video layering across generative audio workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npx installer commands can install changing upstream content.

Mitigation: Install only from a trusted PrunaAI source and pin or review the intended release before use.

Risk: Audio, scripts, images, or videos may be uploaded to external providers during related workflows.

Mitigation: Do not upload confidential or unauthorized content, and check the provider data-handling terms before use.

Risk: Long narration can exceed audio-led video duration limits and lead to truncated output.

Mitigation: Probe audio duration, shorten copy, tighten pace, or split narration into separate scene rows before generation.

## Reference(s):

- [TTS style prompting](references/tts-style-prompting.md)
- [Music and bed prompting](references/music-and-bed-prompting.md)
- [Audio post-production](references/audio-post-production.md)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/audio-prompting)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with prompt templates, structured checklists, inline code blocks, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [References companion Pruna and Replicate skills for API calls, generation, and post-production assembly.]

## Skill Version(s):

1.0.13 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
