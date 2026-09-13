## Description:

Multi-language video subtitle translation and automatic dubbing skill (supports English, Chinese, Japanese, Spanish, French, German, Korean, etc.).

This skill is ready for commercial/non-commercial use.

## Publisher:

[zbjincheng](https://clawhub.ai/user/zbjincheng)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and video localization workflows use this skill to translate subtitles and optionally synthesize target-language dubbing for source videos. It produces a translated subtitle file and a muxed MKV video with source and target audio or subtitle tracks according to the selected processing mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subtitles, TTS text, and provider API keys can be sent to configured external endpoints, including unencrypted HTTP URLs.

Mitigation: Use only trusted HTTPS translation and TTS endpoints, avoid processing sensitive or unauthorized media unless the provider is approved for that data, and scope API keys to minimum permissions and spend limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zbjincheng/skills/video-subtitle-translation-dubbing)
- [Skill homepage](https://github.com/zbjincheng/openclaw-skill-videotranslate)
- [OpenClaw project](https://github.com/OpenClaw)

## Skill Output:

**Output Type(s):** [Files, Text, Configuration]

**Output Format:** [Result object with file paths to translated UTF-8 SRT/VTT subtitle output and muxed MKV video output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local video input and ffmpeg/ffprobe; translation and dubbing modes may call configured translation and TTS services with subtitle or speech text.]

## Skill Version(s):

0.1.4 (source: frontmatter, manifest.yaml, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
