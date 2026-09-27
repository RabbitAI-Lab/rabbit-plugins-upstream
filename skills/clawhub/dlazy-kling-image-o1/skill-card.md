## Description:

Generate images with the Kling O1 model from text prompts and optional reference images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to request text-to-image or image-to-image generation with Kling O1, receive hosted image results, and optionally save generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to dLazy's hosted API and media storage.

Mitigation: Review prompts and media for sensitive content before invocation, and avoid uploading confidential assets unless dLazy use is approved.

Risk: The dLazy CLI can store an API key in a local user configuration file.

Mitigation: Use user-scoped file permissions, rotate or revoke keys from the dLazy dashboard when needed, or supply DLAZY_API_KEY per invocation when persistent storage is not desired.

Risk: API usage may consume credits and generated files are hosted by dLazy.

Mitigation: Use dry-run or cost checks where appropriate, monitor account credits, and handle hosted output URLs according to the user's data-retention expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI homepage from ClawHub metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands; the CLI returns JSON containing generated image output URLs and can save image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation by returning a generateId for later polling.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
