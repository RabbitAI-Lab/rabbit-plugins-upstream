## Description:

Generates 2K, 3K, or 4K images from text prompts and reference images for posters, key visuals, and large-format print.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and designers use this skill to generate or redraw images from prompts and reference images for posters, key visuals, and large-format print.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI requires trusting its package and source.

Mitigation: Review the dLazy CLI source and package before installation.

Risk: Prompts and selected local reference images are sent to dLazy's hosted service.

Mitigation: Share only prompts and files appropriate for a third-party hosted service.

Risk: The CLI can store an API key locally for authenticated requests.

Mitigation: Provide or store a key only if you trust the provider; rotate or revoke it if necessary.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON response with generated image URLs; optional locally saved image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K, 3K, and 4K output and asynchronous tasks. The bundled installation command pins dLazy CLI 1.2.3.]

## Skill Version(s):

1.2.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
