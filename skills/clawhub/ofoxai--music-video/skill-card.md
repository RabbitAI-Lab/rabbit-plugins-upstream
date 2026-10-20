## Description:

Generates visual video segments structured around a user's music track, prices Ofox video jobs before paid execution, and muxes the user's local audio onto the finished video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they have a specific music file and want generated visuals planned around its duration, mood, and sections. The workflow is not for beat-frame-accurate editing, lyric rendering, or generic video ads with background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can submit paid Ofox video jobs using an API key.

Mitigation: Require a dry-run cost table and explicit user approval before any command uses the paid `--approved` path.

Risk: Users may expect the model to listen to or synchronize with their audio file.

Mitigation: State before quoting that the audio stays local, the model does not hear the track, and beat-frame-accurate edits should be done in an editor.

Risk: Missing or outdated dependencies can cause the workflow to fail after planning.

Mitigation: Check `curl`, `jq`, `ffmpeg`, `OFOX_API_KEY`, and `ofox-video-core` 2.0.0 or newer before paid generation.

Risk: Generated files can be hard to locate or can land inside the skill directory.

Mitigation: Use an absolute output directory and report the muxed file's absolute path as the deliverable.

Risk: Installer recovery commands such as `npx` can write outside the working directory.

Mitigation: Relay installer commands for user review instead of running broad third-party installation commands silently.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/music-video)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Source homepage](https://github.com/ofoxai/skills/tree/main/skills/music-video)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command blocks, cost tables, and local file path reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a single-stream agent workflow that includes preflight checks, dry-run pricing, explicit approval posture, generation commands, muxing commands, and final absolute output path guidance.]

## Skill Version(s):

2.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
