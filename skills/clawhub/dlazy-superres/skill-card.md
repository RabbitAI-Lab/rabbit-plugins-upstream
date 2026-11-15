## Description:

Enhances image clarity and detail with a super-resolution workflow, returning an enhanced image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to upscale low-resolution images and retrieve the enhanced image URL through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available inspection did not establish the advertised upscaling workflow or what information the CLI package sends to its hosted service.

Mitigation: Review the package source and confirm its data handling before authenticating or uploading images.

## Reference(s):

- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Image, URL, JSON]

**Output Format:** [JSON response containing the enhanced image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image is hosted remotely; asynchronous requests can return a task identifier before completion.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
