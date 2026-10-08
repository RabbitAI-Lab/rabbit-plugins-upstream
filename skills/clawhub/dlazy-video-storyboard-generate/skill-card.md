## Description:

Turns storyboard scenes and settings into a video-generation pipeline for a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn storyboard dialogue, video prompts, aspect ratio, and resolution into a canvas pipeline with shared source assets and per-scene audio and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to install and run a dLazy CLI and store or use a dLazy API key.

Mitigation: Review the CLI before installing, protect the API key, and confirm each generation command before execution.

Risk: Prompts are sent to dLazy and local media may be uploaded to its service.

Mitigation: Use only prompts and media approved for remote processing; review inputs before each call.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands]

**Output Format:** [JSON canvas pipeline and Markdown guidance; optional CLI-generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses shared source audio and scene image, with cloned audio and video per storyboard scene.]

## Skill Version(s):

1.2.24 (source: server-resolved ClawHub release; skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
