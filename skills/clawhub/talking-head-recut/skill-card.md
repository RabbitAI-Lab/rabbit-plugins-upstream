## Description:

Packages an existing talking-head, interview, or podcast video with timed graphic overlay cards such as kinetic titles, lower-thirds, data callouts, quotes, side panels, and picture-in-picture while the source clip plays underneath.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video editors, and agents use this skill to dress up existing talking-head footage with transcript-synced designed overlays while preserving the original video and audio. It is suited for social clips, interviews, podcasts, explainers, and data-heavy talking-head segments that need visual packaging rather than plain subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable pre-run skill updates and an unpinned npm CLI can change behavior between runs.

Mitigation: Review the release before use, pin the HyperFrames/npm version where practical, and avoid the pre-run skill update during normal use unless intentionally refreshing dependencies.

Risk: Video processing runs with the user's local permissions and reads or writes media artifacts in the workspace.

Mitigation: Run the workflow in a constrained workspace that contains only the source media needed, and review generated shell commands before execution.

Risk: Transcript errors or timing drift can produce misleading overlays or a black tail after the source clip ends.

Mitigation: Review and correct transcript text and timestamps, then clamp card and composition end times to the probed media duration before rendering.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [Design Index](references/DESIGN_INDEX.md)
- [Layout Reference - Stack](references/layouts/stack.html)
- [Layout Reference - Split](references/layouts/split.html)
- [Layout Reference - Overlay](references/layouts/overlay.html)
- [Layout Reference - Picture-in-Picture](references/layouts/pip.html)
- [Frame Reference - Clean](references/frames/clean.html)
- [Frame Reference - Hairline](references/frames/hairline.html)
- [Frame Reference - Polaroid](references/frames/polaroid.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON storyboard structures, HTML/CSS/JavaScript composition snippets, and bash commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow artifacts include metadata.json, transcript.json, storyboard.json, public/cards/*.html, public/index.html, and output.mp4; transcription uses local Whisper through HyperFrames and rendering uses ffmpeg/ffprobe plus the HyperFrames CLI.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
