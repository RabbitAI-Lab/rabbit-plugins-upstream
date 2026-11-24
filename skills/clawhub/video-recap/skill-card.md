## Description:

General-purpose AI video editing and narration recap skill for planning, assembling, and checking narrated video edits from a shared timeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and creators use this skill to plan and produce narrated recaps, including source review, editing, voiceover, subtitles, packaging, and quality checks. It supports exporting a JianYing or CapCut draft for further editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags credential handling and notes that selected speech services can receive narration text or audio.

Mitigation: Review service settings before use, keep API keys in environment variables, and choose local ASR or TTS when you want to avoid sending media or narration to a remote service.

Risk: The security review flags automatic dependency installation, and the Remotion workflow may download packages on its first run.

Mitigation: Review the dependency setup before running Remotion, or use the offline packaging workflow when it meets your needs.

Risk: The security scan was incomplete, with three components only partially analyzed.

Mitigation: Review the skill files and scan results before installation, especially before enabling remote services or dependency installation.

## Reference(s):

- [Video Recap on ClawHub](https://clawhub.ai/worldwonderer/skills/video-recap)
- [Remote services and offline controls](artifact/references/remote-services.md)
- [Timeline schema](artifact/references/timeline-schema.md)
- [JianYing protocol template source (duo-video)](https://github.com/duoec/duo-video)

## Skill Output:

**Output Type(s):** [Video files, Audio files, JSON configuration and reports, Subtitles, Markdown guidance, HTML review pages, Editing project drafts, Shell commands]

**Output Format:** [MP4 video, WAV audio, JSON timeline and quality report, subtitle files, HTML review page, and JianYing/CapCut project draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first workflow; optional remote speech services and first-time Remotion dependency downloads when selected.]

## Skill Version(s):

2.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
