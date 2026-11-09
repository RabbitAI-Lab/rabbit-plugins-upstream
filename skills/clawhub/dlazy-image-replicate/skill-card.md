## Description:

Analyzes an input image's composition, colors, lighting, and style, then creates a prompt for Seedream 4.5 to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can provide a reference image to generate a new image with a similar visual style using dLazy's image-replicate service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that the CLI login step is not clearly connected to the image-generation purpose.

Mitigation: Before installing, consider whether the login step and use of the CLI fit your needs.

Risk: Prompts and local media are handled by the hosted service.

Mitigation: Review the setup details and the service's handling of prompts and media before use.

## Reference(s):

- [CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON response containing generated image URLs and image metadata; optionally saves an image file locally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier before an image is available.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
