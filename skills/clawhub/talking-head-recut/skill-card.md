## Description:

Package an existing talking-head / interview / podcast video with timed, designed GRAPHIC OVERLAY cards — kinetic titles, lower-thirds, data callouts, quotes, side panels, picture-in-picture — synced to the transcript, on a 16:9 / 9:16 / 4:5 canvas of your choice; the clip plays untouched underneath.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and video-production teams use this skill to turn an existing talking-head, interview, or podcast clip into a rendered video with timed graphic overlays while preserving the underlying clip. Agents use it to plan transcript-synced cards, author HTML overlay fragments, assemble a HyperFrames composition, and render the final MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to silently run an unpinned `npx hyperframes skills update talking-head-recut` command before use, which can update the skill and related HyperFrames skills without an explicit review point.

Mitigation: Skip the silent update path for controlled deployments; run updates manually only when intended, review the command and package changes first, and rescan the skill before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [HeyGen publisher profile](https://clawhub.ai/user/heygen-com)
- [NOTICE.md](NOTICE.md)
- [Design index](references/DESIGN_INDEX.md)
- [vtake-skills attribution source](https://github.com/notedit/vtake-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON planning artifacts, HTML/CSS/JavaScript composition files, and MP4 render outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local source video plus system ffmpeg/ffprobe, HyperFrames CLI, and a headless browser render environment.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
