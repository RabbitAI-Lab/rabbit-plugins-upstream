## Description:

Generates 1 MP raster images with refined design judgment for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative professionals use the skill to generate 1 MP raster images from prompts and iterate quickly on everyday design work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy cloud services for generation.

Mitigation: Send only prompts and media you are comfortable sharing with the service.

Risk: Image generation may incur charges.

Mitigation: Use the documented dry-run option to preview the request and estimated cost before generating.

Risk: The third-party CLI uses a locally stored organization API key.

Mitigation: Prefer device-code login over putting a key in a shell command, protect the local configuration, and rotate or revoke keys when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [PNG raster image with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs and can optionally be saved locally.]

## Skill Version(s):

1.3.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
