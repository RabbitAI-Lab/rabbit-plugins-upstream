## Description:

Analyzes a reference image's visual style, composition, colors, and lighting, then creates a replication prompt and uses Seedream 4.5 to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can provide reference images and prompts to generate new images that follow a similar visual style. The skill uses dLazy's hosted service and returns generated image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to dLazy's hosted service, and local image paths may be uploaded for processing.

Mitigation: Use only images and prompts you are comfortable sending to dLazy.

Risk: The CLI stores an organization API key in the user's local configuration.

Mitigation: Protect the local configuration and key; use the documented key rotation or revocation controls if needed.

Risk: Image generation may incur service charges.

Mitigation: Check the cost estimate and available credits before running generation requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in skill metadata (not server-resolved provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Text, JSON]

**Output Format:** [Generated image assets and a JSON result envelope containing image URLs and task status when asynchronous mode is used.]

**Output Parameters:** [Reference images, a prompt, optional wait settings, and an optional local save path.]

**Other Properties Related to Output:** [Reference files may be uploaded to dLazy-hosted storage; returned image assets are hosted by dLazy.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
