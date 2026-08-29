## Description:

Turn arbitrary text such as an article, notes, topic, or brief into a faceless explainer video with invented per-scene visuals such as typography, abstract graphics, diagrams, and data visualization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and video-production agents use this skill to convert source text into a structured HyperFrames project with a brief, storyboard, narration script, invented visuals, captions, preview, and final MP4 render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to update installed skill content from remote sources during setup or normal use, including a broad global update path.

Mitigation: Run it in a dedicated project directory, confirm update steps before execution, and review or disable update behavior where possible.

Risk: Generated previews or renders may load GSAP from jsDelivr and may use HeyGen credentials when the user is signed in.

Mitigation: Use it only in a trusted network environment, check authentication status before running, and use offline mode or sign out when credentials should not be used.

Risk: Explainer planning and generated visuals can introduce incorrect or misleading guidance into the final video.

Mitigation: Review the storyboard, script, contact sheet, and final preview before rendering or publishing.

## Reference(s):

- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)
- [Frame worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown instructions with shell commands plus generated project files, HTML compositions, JSON metadata, captions, previews, and MP4 render output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a HyperFrames project under videos/<project> with BRIEF.md, STORYBOARD.md, SCRIPT.md when narration is used, audio_meta.json when audio is generated, index.html, frame HTML files, caption_groups.json when captions are built, snapshots, and renders/video.mp4.]

## Skill Version(s):

1.0.27 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
