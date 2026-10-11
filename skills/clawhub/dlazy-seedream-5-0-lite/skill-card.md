## Description:

Generates images from text prompts or reference images with Doubao Seedream 5.0 Lite through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create images from text prompts or reference images using the dLazy-hosted Seedream 5.0 Lite service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy, and generated images are hosted there.

Mitigation: Avoid sharing sensitive prompts or images unless the user accepts dLazy as the provider.

Risk: The CLI may store a dLazy API key locally.

Mitigation: Protect the local key and rotate it if exposed; use an on-demand CLI invocation if a persistent global install is unwanted.

Risk: Generic image-generation requests may use a third-party provider unexpectedly.

Mitigation: Confirm the provider choice with the user before sending a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source linked in release metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image links, Shell commands, Configuration guidance]

**Output Format:** [Markdown with image links and optional command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
