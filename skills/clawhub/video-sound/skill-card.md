## Description:

Plans and creates dialogue, music, sound effects, and measured mixes for video using cue sheets, voice auditions, and audio checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and developers use this skill to plan and produce voiceover, music, sound effects, and a checked mix for videos, trailers, and launch films.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Judging cleanup may delete files beyond those created by the skill.

Mitigation: Use a fresh, dedicated output directory for judging until cleanup is fixed to remove only files it created.

Risk: Some inputs are not sufficiently validated, including download paths, URLs, and numeric fields.

Mitigation: Use trusted manifests and cue sheets, and validate paths, URLs, and numeric values before running the helpers.

Risk: Remote estimation, generation, or judging can involve sharing scripts or footage, and dependencies can change.

Mitigation: Approve script or footage sharing before remote processing and pin dependencies.

## Reference(s):

- [ClawHub video-sound skill](https://clawhub.ai/vargai/skills/video-sound)
- [Project homepage (metadata.clawdis)](https://github.com/vargHQ/skills/tree/main/video-sound)
- [Cue sheet format](artifact/references/cue-sheet.md)
- [Dialogue guidance](artifact/references/dialogue.md)
- [Music and sound effect guidance](artifact/references/music.md)
- [Mix guidance](artifact/references/mix.md)
- [Voice and audition guidance](artifact/references/voice.md)
- [Audio judging guidance](artifact/references/judge.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Audio files, HTML]

**Output Format:** [Markdown plans and scripts, JSON cue sheets and reports, generated audio files, and HTML audition pages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote voice, music, or sound effect generation may incur usage costs; human audition and final listening review are part of the workflow.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
