## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users can use this skill to convert raster image inputs into scalable vector-style outputs through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image paths supplied to the CLI may be uploaded to dLazy media storage for processing.

Mitigation: Use the skill only for images intended for upload to dLazy, and avoid private or sensitive local images unless upload is acceptable.

Risk: The dLazy API key is saved in the local CLI configuration or supplied through an environment variable.

Mitigation: Prefer per-invocation credentials when persistence is not desired, restrict local config access, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: A persistent global CLI install increases local dependency exposure.

Mitigation: Use the pinned npx invocation, npx @dlazy/cli@1.2.3, when a persistent global binary is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON response with hosted output URLs, optional saved local asset, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and image input as a URL or local path.]

## Skill Version(s):

1.2.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
