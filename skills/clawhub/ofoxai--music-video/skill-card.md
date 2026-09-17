## Description:

Creates structure-matched visual video segments for a user-provided music track, prices the required Ofox jobs, and locally muxes the user's audio onto the final video without sending the audio to the API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill when they have a specific local music file and need an agent to plan, price, generate, and assemble structure-matched video segments with the original audio muxed locally. It is not intended for beat-frame-accurate edits, lyric rendering, generic social drafts, or jobs with no particular audio file to carry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery guidance includes an overbroad global wildcard install path that could install more skills or agent integrations than intended.

Mitigation: Review any npx install command before running it; prefer a pinned, scoped install of only ofox-video-core for the intended agent.

Risk: The skill depends on a paid API workflow, so mistaken segment counts, prompt splitting, or missing cost approval can create unexpected spend.

Mitigation: Use dry-run pricing, show the full multi-segment cost table, verify SHOTS_REQUESTED, and require explicit user approval before submitting paid jobs.

Risk: The generated visuals are not beat-frame-accurate and the model does not listen to the user's track.

Mitigation: State this limitation before quoting or running jobs; route beat-accurate cuts, lyrics, and exact timing work to an editor workflow.

Risk: Missing ffmpeg, ffprobe, or an outdated ofox-video-core can prevent stitching or the final local audio mux after paid segments have completed.

Mitigation: Check local binaries and confirm ofox-video-core 1.25.0 or newer before generation; keep the user's OFOX_API_KEY scoped to the Ofox workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/music-video)
- [Source homepage](https://github.com/ofoxai/skills/tree/main/skills/music-video)
- [Ofox API key portal](https://app.ofox.ai)
- [Artifact skill definition](artifact/SKILL.md)
- [Artifact changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown with inline bash code blocks and a final local video file path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, ffmpeg/ffprobe, and ofox-video-core 1.25.0 or newer.]

## Skill Version(s):

1.1.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
