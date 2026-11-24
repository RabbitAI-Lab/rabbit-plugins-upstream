## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can convert PNG or JPG logos, icons, and flat illustrations into vector assets for scalable use, then retrieve the result URL or save the file locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a dLazy API key, and the security review notes that some referenced material was unavailable.

Mitigation: Review the official CLI information before setup, keep the API key private, and rotate or revoke it through the dLazy organization dashboard if needed.

Risk: The skill uploads local image inputs to dLazy media storage for processing.

Mitigation: Only submit images that are appropriate to send to the hosted service; avoid confidential images unless their use is approved.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [Structured JSON response containing the generated asset URL; a vector image file when downloaded with --save.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The command can return a task ID for asynchronous jobs.]

## Skill Version(s):

1.2.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
