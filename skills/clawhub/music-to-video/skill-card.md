## Description:

Turn a music track, supplied audio, video audio, or a mood brief into a beat-synced lyric video, slideshow, or kinetic promo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan, build, assemble, check, and render music-driven HyperFrames videos from audio plus optional user media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can silently update installed skills or run npx-based HyperFrames commands before the user has reviewed the action.

Mitigation: Require explicit approval before installing updates or running commands that modify the local skill set.

Risk: The workflow can install Python audio-analysis dependencies into the active environment.

Mitigation: Use an isolated project environment and review dependency installation before allowing environment mutation.

Risk: The workflow creates and modifies project files under videos/<project> and may use provider authentication for music generation.

Mitigation: Run it in a trusted workspace, keep credentials out of project files, and review provider authentication status before external generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Frame skeleton reference](references/frame-skeleton.md)
- [Planning reference](references/planning.md)
- [Storyboard format reference](references/storyboard-format.md)
- [Template catalog](references/template-catalog.md)
- [Motion primitive catalog](references/motion-primitive-catalog.md)
- [Montage reference](references/montage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown plans, HTML frame compositions, JSON timing data, shell commands, and rendered video project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project files under videos/<project>, including audiomap.json, STORYBOARD.md, frame.md, composition HTML, index.html, and renders/video.mp4.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
