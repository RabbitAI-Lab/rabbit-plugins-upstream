## Description:

Turns arbitrary text into a faceless explainer video by planning a HyperFrames project, generating storyboard and script assets, building HTML frames, assembling audio, captions, and transitions, and rendering an MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and developers use this skill to turn articles, notes, topics, or briefs into topic explainers, concept breakdowns, how-tos, and listicle-style videos without relying on captured website footage or presenter video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can run floating HyperFrames CLI commands and update installed skills globally, which may execute changed package code at use time.

Mitigation: Review before installing, prefer a pinned or locally audited HyperFrames CLI, and run the workflow in a limited project workspace.

Risk: The workflow can use audio and media provider credentials and start a local preview service.

Mitigation: Use scoped credentials, verify sign-in status before generation, and avoid exposing preview services outside the intended local environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/faceless-explainer)
- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker delta](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown workflow guidance with shell commands, JSON metadata, HTML frame compositions, and rendered video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project files such as BRIEF.md, STORYBOARD.md, SCRIPT.md, frame.md, audio_meta.json, index.html, caption data, contact sheets, and renders/video.mp4.]

## Skill Version(s):

1.0.38 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
