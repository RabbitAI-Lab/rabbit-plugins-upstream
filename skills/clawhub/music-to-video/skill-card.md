## Description:

Turn a music track (an audio file, a video to pull audio from, or a track generated from a mood brief) into a beat-synced video — lyric video, slideshow, or kinetic promo. The music drives all pacing; any user-supplied images/videos are cut onto the same beat grid, and a complete video needs zero assets. Narrated pieces → the input-matched workflow (see /hyperframes). Unclear → /hyperframes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a music track and optional media into a beat-synced HyperFrames video. It guides an agent through music analysis, storyboard planning, frame composition, assembly, checks, and MP4 rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run HyperFrames commands through npm at use time, which can execute external runtime tooling.

Mitigation: Run the workflow in a constrained project workspace and review commands before execution, especially before provider authentication or rendering steps.

Risk: The skill can prompt updates to installed skills, including global skill updates.

Mitigation: Review the skills-update prompt before approving it and confirm the installed skill set after updates.

Risk: Generated HTML and video output may use external runtime resources or intense flashing effects.

Mitigation: Check the assembled project and rendered video before sharing, with extra attention to runtime resources, snapshots, contrast, and flashing sequences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Frame skeleton reference](references/frame-skeleton.md)
- [Planning reference](references/planning.md)
- [Template catalog](references/template-catalog.md)
- [Motion primitive catalog](references/motion-primitive-catalog.md)
- [Montage reference](references/montage.md)
- [Frame worker sub-agent](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON analysis files, storyboard and configuration files, HTML composition code, and rendered video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent workflow artifacts under a HyperFrames project, including audiomap.json, STORYBOARD.md, frame.md, HTML frame compositions, index.html, snapshots, and renders/video.mp4.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
