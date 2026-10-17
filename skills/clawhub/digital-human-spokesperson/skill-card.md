## Description:

Creates an English-then-Arabic talking-head video from supplied copy, with a generated presenter, voiceovers, subtitles, and title cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams producing cross-border commerce, education, or promotional content use this skill to turn English copy, optionally with supplied Arabic copy, into a bilingual presenter video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scripts, presenter images, and voice or audio may be sent to external services without sufficiently explicit consent.

Mitigation: Confirm with the user before using edge-tts, D-ID, or HeyGen; use local SadTalker or the ffmpeg fallback when privacy matters.

Risk: Public media URLs used for cloud video generation may expose presenter images or audio.

Mitigation: Avoid public unauthenticated URLs for sensitive media and review hosting access before cloud processing.

Risk: Setting up the local lip-sync engine can introduce unreviewed third-party dependencies.

Mitigation: Review pip packages and GitHub dependencies before installing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/arronjack/skills/digital-human-spokesperson)
- [Bilingual digital-human pipeline](references/pipeline.md)
- [SadTalker](https://github.com/vinthony/SadTalker.git)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [MP4 video with burned-in bilingual subtitles and title cards; intermediate text, MP3 audio, and SRT subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [English segment precedes Arabic; report the voice choices, translation source, and whether the chosen engine provides precise lip-sync.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
