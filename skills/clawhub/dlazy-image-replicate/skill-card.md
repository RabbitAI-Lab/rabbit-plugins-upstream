## Description:

Analyzes a reference image’s composition, colors, lighting, and style, then builds a prompt and sends it to Seedream 4.5 to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can provide a reference image to create a new image that follows its visual style, composition, colors, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags login and authentication steps that are not clearly connected to the image workflow; the referenced CLI and service details were not fully reviewed.

Mitigation: Review the current CLI and service documentation and authentication flow before installing or using the skill.

Risk: Prompts and local reference image files are sent to dLazy hosted services for processing.

Mitigation: Submit only images and prompts you are authorized to share, and review dLazy’s service terms before use.

Risk: The dLazy API key is saved in the local CLI configuration unless supplied per invocation.

Mitigation: Protect the account-scoped key and configuration file, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets with a JSON result containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are hosted on files.dlazy.com; asynchronous requests may initially return a task ID without image outputs.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
