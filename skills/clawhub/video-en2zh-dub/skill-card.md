## Description:

Turns English-language videos into Chinese-dubbed videos, with an option to retain the original English audio as a separate track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anshanzhaoqian](https://clawhub.ai/user/anshanzhaoqian)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and editors use this skill to transcribe and translate spoken English, synthesize Chinese narration, and produce a dubbed video with replaced or dual audio tracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chinese subtitle text is sent to Microsoft's online service for speech synthesis, despite an offline claim in the documentation.

Mitigation: Do not use confidential, regulated, or private video content unless that external text transfer is acceptable.

Risk: Video assembly commands can overwrite existing output files.

Mitigation: Check for existing output files and choose a safe destination before running the commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/anshanzhaoqian/skills/video-en2zh-dub)
- [Troubleshooting notes](references/pitfalls.md)
- [Audio synchronization guidance](references/sync-tuning.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [Markdown guidance, SRT subtitles, MP3 audio, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports replacement, dual-track, or mixed audio.]

## Skill Version(s):

1.0.1 (source: ClawHub release; SKILL.md frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
