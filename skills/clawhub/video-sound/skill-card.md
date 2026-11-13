## Description:

Plan, generate, and measure dialogue, music, and sound effects for videos, using scripts and human listening checks to guide voice selection and final mixing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use the skill to plan and produce voice, music, and sound design for videos, then measure the mix and get human approval for voice and final playback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded files and audio inputs may not be sufficiently validated.

Mitigation: Check download destinations and validate audio inputs before running the skill's processing steps.

Risk: Temporary-file cleanup could affect files beyond those created by the skill.

Mitigation: Restrict cleanup to temporary files created by the current skill run.

Risk: External services may receive scripts or recordings, and their handling is unclear.

Mitigation: Review each service's data handling before sending scripts or recordings, and avoid sending sensitive material until it is clear.

## Reference(s):

- [Cue sheet format](artifact/references/cue-sheet.md)
- [Dialogue writing](artifact/references/dialogue.md)
- [Voice direction and auditioning](artifact/references/voice.md)
- [Music planning](artifact/references/music.md)
- [Sound effects](artifact/references/sfx.md)
- [Mixing and loudness checks](artifact/references/mix.md)
- [Video sound design guide](https://varg.ai/how-to/design-sound-and-voice-for-ai-video)
- [Video sound in ten steps](https://varg.ai/how-to/make-a-video-in-ten-steps)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Code, Shell commands, HTML, Audio files]

**Output Format:** [Markdown plans and scripts, JSON cue sheets and reports, HTML audition pages, and audio mix files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts provide measurements and checks; a person selects voice takes and listens to approve the final mix.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
