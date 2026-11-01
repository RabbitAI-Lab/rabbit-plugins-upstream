## Description:

Guides agents through creating, editing, animating, and rendering HyperFrames videos, including films, explainers, music videos, charts, maps, captions, and overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and revise HyperFrames video projects, from storyboards and visual treatments to captions, overlays, audio, and rendered video. It supports formats such as launch films, explainers, music videos, charts, maps, and vertical clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standalone setup may change installed skills or project versions.

Mitigation: Set HYPERFRAMES_SKIP_SKILLS=1, keep an approved CLI version, and require approval before changing installed skills or project versions.

Risk: Map baking runs with browser isolation disabled.

Mitigation: Run map baking in an isolated environment.

Risk: The image-location workflow may send images to Google.

Mitigation: Use the local image-location workflow unless sending the image to Google is acceptable.

## Reference(s):

- [HyperFrames on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes)
- [Plugin installation guidance](artifact/references/plugin-installation.md)
- [Skill lifecycle guidance](artifact/references/skill-lifecycle.md)
- [Video format reference](artifact/references/format.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, HTML/CSS/JavaScript code, Shell commands, Configuration, Rendered video]

**Output Format:** [Markdown guidance, video project files, shell commands, and rendered video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific; may include storyboards, captions, overlays, visual assets, and audio.]

## Skill Version(s):

1.0.50 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
