## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use this skill to generate images from text prompts with Jimeng, optionally guided by reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy services for generation and storage.

Mitigation: Avoid sending sensitive prompts or images unless you trust dLazy with that content.

Risk: The CLI saves an API key in the local user configuration when login completes.

Mitigation: Prefer device login over sharing keys in chat, protect access to the device, and revoke saved keys when they are no longer needed.

Risk: Image generation can incur charges.

Mitigation: Review the CLI dry-run cost estimate before submitting a generation request.

## Reference(s):

- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image assets returned as URLs, with JSON result metadata; images can optionally be saved as files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts an optional prompt and up to 10 reference images; asynchronous mode can return task metadata before image outputs are ready.]

## Skill Version(s):

1.3.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
