## Description:

Generate vertical short videos (9:16) from a Markdown script by parsing sections, generating TTS audio, rendering subtitle cards, and compositing the result into MP4 with FFmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuhedev](https://clawhub.ai/user/liuhedev)

### License/Terms of Use:


## Use Case:

Developers and content automation teams use this skill to turn structured Markdown scripts into vertical short-form videos with synchronized narration, subtitle cards, and FFmpeg composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes promotional branding and a fixed closing pattern in its templates and example script.

Mitigation: Review and edit templates and script text before publishing generated videos.

Risk: The optional custom TTS command can execute arbitrary shell commands.

Mitigation: Avoid --tts-command unless the exact command string and script content are trusted.

Risk: Markdown inputs and temporary output paths may contain sensitive script text or generated media.

Mitigation: Treat Markdown inputs as trusted content and use a dedicated output or temporary directory when scripts may contain sensitive text.

## Reference(s):

- [Project homepage](https://github.com/liuhedev/lh-openclaw-kit)

## Skill Output:

**Output Type(s):** [files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and generated MP4 video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media depends on local FFmpeg, Chrome or supplied slide images, and a trusted TTS tool or command.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
