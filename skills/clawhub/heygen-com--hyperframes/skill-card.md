## Description:

Read first to make, edit, animate or render any video with HyperFrames (HTML rendered to video), including launch films, explainers, music videos, charts, maps, vertical clips, title cards, captions and overlays. Holds the render contract, the work loop and what each kind of video needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to plan, build, edit, animate, and render videos as editable HyperFrames projects, including explainers, launch films, music videos, charts, maps, and social clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standalone setup may modify installed agent instructions or an existing CLI pin.

Mitigation: Prefer the versioned plugin installation; for standalone setup, set HYPERFRAMES_SKIP_SKILLS=1 and require approval before changing an existing CLI pin.

Risk: The optional image workflow's auto mode sends the entire image to Google.

Mitigation: Use the local grid workflow for private images.

Risk: Map baking can affect the working environment or replace an existing frame.md.

Mitigation: Run map baking in an isolated environment and preserve an existing frame.md before applying a preset.

## Reference(s):

- [HyperFrames on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and project files such as HTML, CSS, and JavaScript]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content and files depend on the requested video task; a rendered video is produced only when requested or approved.]

## Skill Version(s):

1.0.49 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
