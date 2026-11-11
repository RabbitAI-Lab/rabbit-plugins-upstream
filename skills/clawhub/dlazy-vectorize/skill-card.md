## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can use the skill to convert raster images such as logos, icons, and flat illustrations into color vector artwork and receive a hosted result URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan was partial, and it reports credential setup behavior that is not demonstrated in the stated image-conversion workflow.

Mitigation: Review the CLI and its data handling before installing or supplying an API key or images.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image, URL, JSON]

**Output Format:** [JSON result containing a hosted output URL and image metadata; asynchronous calls may return task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented CLI also supports saving the returned asset to a local path.]

## Skill Version(s):

1.2.38 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
