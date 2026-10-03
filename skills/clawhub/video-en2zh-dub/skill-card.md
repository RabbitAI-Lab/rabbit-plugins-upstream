## Description:

Turns English-language videos into Mandarin-dubbed videos with options to replace the original audio, retain both tracks, or mix them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anshanzhaoqian](https://clawhub.ai/user/anshanzhaoqian)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Video creators and developers use this skill to transcribe English speech, translate subtitles into Mandarin, synthesize a voice track, and deliver a dubbed video with their preferred audio arrangement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mandarin subtitle text is sent to an online text-to-speech service despite claims of offline operation.

Mitigation: Use only video transcripts you are comfortable sharing with that service.

Risk: Output files may be overwritten.

Mitigation: Check existing files and choose output names before running the pipeline.

Risk: Unpinned dependencies can make installations less repeatable.

Mitigation: Pin dependencies or use a locked environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/anshanzhaoqian/skills/video-en2zh-dub)
- [Troubleshooting and pitfalls](references/pitfalls.md)
- [Audio synchronization guidance](references/sync-tuning.md)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands]

**Output Format:** [MP4 video, SRT subtitles, MP3 audio, and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can replace English audio, retain switchable English and Mandarin tracks, or mix Mandarin with quieter English audio.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
