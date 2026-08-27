## Description:

Creates low-cost vertical motion-comic videos from scripts using consistent AI-generated keyframes, Mandarin Edge TTS, captions, audio mixing, and FFmpeg assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT

## Use Case:

External creators, developers, and production teams use this skill to turn story scripts into reviewable vertical motion-comic episodes with reusable assets. It is also useful for diagnosing character drift, subtitle timing issues, robotic TTS, audio balance problems, and FFmpeg motion jitter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text may be sent to the online Edge TTS service by the default voice route.

Mitigation: Avoid sensitive scripts with the default online TTS route, or choose an approved authenticated or local TTS alternative before generating voices.

Risk: The skill runs FFmpeg/ffprobe and helper scripts and creates project files from user-provided manifests and media paths.

Mitigation: Work in a dedicated project directory, run the preflight check, and review manifests or paths from untrusted sources before executing helper scripts.

Risk: Generated or downloaded audio such as background music may have unclear reuse rights.

Mitigation: Use synthesized audio or media with explicit reusable licensing, and record provenance for external audio assets.

Risk: Image generation can produce character drift, hand anatomy errors, accidental text, watermark-like artifacts, or subtitle-safe-area conflicts.

Mitigation: Inspect the visual bible, contact sheets, full-size keyframes, subtitles, and final snapshots before handoff, and regenerate failed shots with targeted corrections.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/ToBeWin/make-motion-comic)
- [ClawHub skill page](https://clawhub.ai/tobewin/skills/make-motion-comic)
- [Audio and Edge TTS](references/audio-and-tts.md)
- [Image Consistency](references/image-consistency.md)
- [Motion and Quality Control](references/motion-and-qc.md)
- [Story and Shots](references/story-and-shots.md)
- [Edge TTS](https://github.com/rany2/edge-tts)
- [FFmpeg](https://ffmpeg.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON manifests, SRT subtitles, audio files, MP4 video files, image assets, and QC notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical outputs include a script and shot table, character visual bible, prompts, keyframes, TTS manifest, voice mix, timeline, subtitles, cover, contact sheet, final video, and verification results.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
