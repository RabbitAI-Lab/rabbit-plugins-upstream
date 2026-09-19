## Description:

Generate images with the Kling o1 model from text prompts or reference images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Kling o1 using text prompts and up to ten reference images. It is suited for cloud-based image generation workflows that can send prompts and selected media to dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local reference images are sent to dLazy's hosted service for image generation.

Mitigation: Avoid passing private prompts or local images unless the user is comfortable uploading them to the service.

Risk: The skill depends on a pinned third-party npm CLI package and an API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Review the pinned @dlazy/cli package under normal npm supply-chain controls and rotate or revoke the dLazy API key if exposure is suspected.

Risk: Generation can fail when the API key is missing, invalid, or the account has insufficient credits.

Mitigation: Confirm authentication before use and direct users to update credentials or recharge credits when those specific errors are returned.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [JSON responses with image output URLs, optional downloaded image files, and human-facing setup or error guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers when no-wait mode is used; saved outputs may be downloaded to a user-specified local path.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
