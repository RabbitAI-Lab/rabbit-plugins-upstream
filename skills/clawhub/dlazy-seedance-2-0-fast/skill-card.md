## Description:

Generates videos with Seedance 2.0 Fast from text prompts, with optional multimodal references or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short Seedance 2.0 Fast videos from prompts, optionally guided by images, videos, audio, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had medium confidence and partial coverage, and the documented authentication commands are not clearly connected to the advertised video-generation purpose.

Mitigation: Before signing in or authorizing the CLI, inspect its command behavior and confirm it matches the requested video-generation task.

Risk: Local image, video, or audio inputs are uploaded to dLazy's hosted media service for generation.

Mitigation: Avoid submitting sensitive media unless it is appropriate to share with the hosted service.

## Reference(s):

- [dLazy CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON result with generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted separately; asynchronous runs may initially return a task ID and status.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
