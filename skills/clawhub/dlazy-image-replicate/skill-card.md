## Description:

Analyzes an input image's composition, colors, lighting, and style, then sends a replication prompt to Seedream 4.5 to generate a new image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a reference image to generate a new image with a similar visual style through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan found no confirmed harmful behavior, but had medium confidence and did not fully assess the package and referenced material.

Mitigation: Review the package and referenced materials before installation.

Risk: Prompts and local image files provided to the skill are sent to dLazy's hosted services, and use requires an API key.

Mitigation: Submit only content you are authorized to share and comfortable processing remotely; protect the API key and rotate it if exposed.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)

## Skill Output:

**Output Type(s):** [Image files, JSON result metadata]

**Output Format:** [Generated image URL in a JSON response; optionally saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task identifier when run without waiting.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
