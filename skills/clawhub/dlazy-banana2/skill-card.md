## Description:

Generate and edit high-quality images with Nano Banana 2.0 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to create images from prompts or edit supplied reference images with Nano Banana 2.0.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial and could not fully verify the CLI login flow or connected service behavior.

Mitigation: Review the listed CLI project and confirm you trust the CLI and dLazy service before signing in or sending requests.

Risk: Prompts and supplied local images are sent to dLazy's hosted API and media storage; the CLI stores an API key in the user's configuration.

Mitigation: Avoid sending sensitive prompts or images unless approved, protect the local CLI configuration, and rotate or revoke the API key if it may be exposed.

## Reference(s):

- [dLazy service website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, Files, JSON]

**Output Format:** [Generated image assets returned as hosted URLs in a JSON response, with optional local file saving]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-image and image-to-image; optional asynchronous task identifiers]

## Skill Version(s):

1.3.42 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
