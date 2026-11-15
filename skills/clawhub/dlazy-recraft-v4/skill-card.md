## Description:

Generates 1MP raster images with refined design judgment for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, including designers and other creators, use prompt-based Recraft V4 image generation to make raster artwork and iterate on aspect ratios. The skill runs through the dLazy CLI and returns generated image URLs or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial with medium confidence; it noted an apparent mismatch between the image-generation purpose and a CLI login operation, and several references could not be resolved.

Mitigation: Review unresolved references and confirm the command behavior and scope before installing if additional assurance is needed.

Risk: Prompts and local media supplied to the CLI are sent to dLazy-hosted services.

Mitigation: Avoid sending confidential prompts or files unless their use with the service is approved.

## Reference(s):

- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [Raster image files (PNG) and JSON result metadata containing output URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports aspect-ratio selection, asynchronous task IDs, and saving results to a local path.]

## Skill Version(s):

1.3.40 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
