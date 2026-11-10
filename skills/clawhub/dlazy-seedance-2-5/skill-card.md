## Description:

ByteDance's next-generation video model supports clips up to 30 seconds, native 4K, stronger instruction following and long-form narratives, multimodal image, video, and audio references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can ask an agent to generate Seedance 2.5 video from a prompt and optional image, video, or audio references. They can set duration, aspect ratio, resolution, audio generation, and first or last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image, video, or audio may be sent to dLazy's API or uploaded to its media storage.

Mitigation: Submit only prompts and media you are permitted and comfortable sharing with dLazy.

Risk: The security assessment has medium confidence and is partial; the documented behavior did not clearly match the advertised video-generation purpose, and some references were unavailable for review.

Mitigation: Review the CLI's documented behavior against the intended video-generation task before installing or running it.

## Reference(s):

- [dLazy service website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Generated video or other media, JSON]

**Output Format:** [JSON response with generated media URLs and task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs can return a task identifier before the media is ready. Result URLs are hosted by dLazy.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
