## Description:

Generate and edit images with Nano Banana 2.0 using text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users can generate or edit images from text prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input images are sent to dLazy hosted services, and image generation may incur charges.

Mitigation: Review dLazy's data handling and charges before use, and send only content appropriate for cloud processing.

Risk: The API key may be saved in the local CLI configuration when using the login flow.

Mitigation: Choose between local key storage and supplying the key per run; protect stored credentials and rotate or revoke a key if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [Declared CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON, Text]

**Output Format:** [JSON results with generated image URLs; optionally downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID when generation is requested without waiting.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
