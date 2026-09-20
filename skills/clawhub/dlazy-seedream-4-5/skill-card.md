## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts or reference images through the dLazy Seedream 4.5 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input image files are sent to dLazy hosted endpoints for generation.

Mitigation: Use only with content approved for the dLazy hosted service, and review prompts and files before invocation.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use OS-protected local configuration or the DLAZY_API_KEY environment variable, and rotate or revoke keys if exposure is suspected.

Risk: Generic image-generation requests could be routed to this provider unintentionally.

Mitigation: Invoke the dLazy Seedream skill explicitly when this provider is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result containing generated image URLs, with optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.17 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
