## Description:

Turns storyboard scenes and dialogue into a video-generation pipeline for a canvas, with optional dLazy media generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn storyboard scenes, dialogue, and prompts into a canvas-ready video pipeline and optionally generate media using dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests installation and execution of a third-party CLI beyond its narrow storyboard description.

Mitigation: Review the full skill and CLI package before installation, and approve each generation command before running it.

Risk: dLazy API credentials are stored locally, and prompts or selected media may be sent to dLazy-hosted services.

Mitigation: Protect and rotate API keys as needed; provide local media paths only when you intend to upload the files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [JSON canvas pipeline and text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas entries share source audio and scene image, with cloned audio and video per storyboard; optional generation returns media URLs.]

## Skill Version(s):

1.2.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
