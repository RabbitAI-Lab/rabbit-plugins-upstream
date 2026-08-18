## Description:

Generate images with the Kling O1 model, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Kling Image O1 service from an agent for text-to-image generation and reference-image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided reference images are sent to dLazy's hosted image-generation service.

Mitigation: Use the skill only when dLazy is an acceptable provider and avoid sending sensitive prompts or media unless approved.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer explicit invocation when provider choice matters, protect the local configuration file, and rotate or revoke API keys if exposure is suspected.

Risk: Generation depends on external dLazy API and media-storage endpoints.

Mitigation: Use dry-run or asynchronous polling when cost visibility, timeout behavior, or service availability is important.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result containing generated image URLs or asynchronous task identifiers, with concise user-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted file URLs; asynchronous mode returns a generation ID for later polling.]

## Skill Version(s):

1.3.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
