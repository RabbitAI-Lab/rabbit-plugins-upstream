## Description:

Rebuild any video file as an editable HyperFrames project—motion graphics, talking heads, live action, or AI-generated footage—and check the render against the original frame by frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use the skill to rebuild video they are authorized to use as an editable HyperFrames project, then compare its render with the source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow directs paid processing of people's images and voices without asking and suppresses cost information.

Mitigation: Require approval for footage, face, and voice uploads and set a total credit limit for retries; keep estimates and usage reporting visible.

Risk: Footage, faces, and voice audio may be processed externally.

Mitigation: Use footage the user is authorized to share, choose the HeyGen opt-out and local rendering when external processing is unsuitable, and review provider retention practices.

Risk: The HyperFrames CLI implementation and telemetry behavior are outside the supplied artifacts.

Mitigation: Review and pin the CLI version before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/reverse-any-video)
- [Opening a Reverse](references/start.md)
- [Re-shooting a person](references/people.md)
- [Animated and painted films](references/animated.md)
- [Matching what is drawn](references/match.md)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Guidance]

**Output Format:** [Editable HyperFrames project files, HTML components and media assets, plus a Markdown REVERSE.md report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The project includes a rendered video when rendering succeeds, with a frame-by-frame comparison against the source.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
