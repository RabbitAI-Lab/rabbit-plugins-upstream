## Description:

Helps agents plan and produce video soundtracks, including dialogue, voice casting, music, sound effects, mixing, and measured quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Video editors and creators use this skill to plan and build soundtracks for launch videos, ads, trailers, explainers, and AI-generated films, including dialogue, music, effects, and a measured mix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An existing temporary `_tmp` folder may lose its contents.

Mitigation: Use a separate project with backups and a fresh judging output directory.

Risk: Cue and audition inputs may be processed without adequate checks.

Mitigation: Use trusted cue and audition files, restrict filesystem and network access, and pin dependencies.

Risk: External processing may begin before estimated charges are approved; provider retention and remote dependency behavior are unverified.

Mitigation: Approve external processing before requesting estimates. Note that `--yes` gates paid generation but not the initial dialogue upload, and check provider retention and remote dependency behavior before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/video-sound)
- [Project homepage listed in skill metadata](https://github.com/vargHQ/skills/tree/main/video-sound)
- [Voice direction guide](references/voice.md)
- [Dialogue and narration guide](references/dialogue.md)
- [Music guide](references/music.md)
- [Sound effects guide](references/sfx.md)
- [Mixing and mastering guide](references/mix.md)
- [Cue sheet format](references/cue-sheet.md)
- [Take judging guide](references/judge.md)
- [Sourced evidence guide](references/evidence.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Audio files, HTML, Shell commands]

**Output Format:** [Markdown plans, JSON cue sheets and reports, audio files, and an HTML voice audition page]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A person must listen to and approve audio; generated assets may incur provider charges.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
