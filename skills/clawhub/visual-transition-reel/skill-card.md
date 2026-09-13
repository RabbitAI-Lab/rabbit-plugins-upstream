## Description:

Use when someone wants a montage with transitions between shots -- action-sequence reel or multi-scene piece where narration is optional.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and agent users use this skill to plan and generate multi-scene visual transition reels with approved scene plans, start and end stills, video clips, and final assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install guidance uses unpinned remote package execution.

Mitigation: Review install commands before use, prefer pinned and reviewed versions of the skills CLI and Pruna skill references, and avoid the full-suite install unless all referenced skills are needed.

Risk: The workflow can upload source images and overwrite generated media files.

Mitigation: Run media generation only in a workspace where those uploads and overwrites are acceptable, and review source images and destinations before generating.

Risk: The security summary notes one overbroad response-control instruction.

Mitigation: Review the workflow habit requirements before deployment and narrow or remove response-control language that is not needed for the deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/visual-transition-reel)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plan templates and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged planning, still-generation, clip-generation, assembly, and manifest guidance; generated media files are produced by referenced image, video, audio, and ffmpeg tools.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
