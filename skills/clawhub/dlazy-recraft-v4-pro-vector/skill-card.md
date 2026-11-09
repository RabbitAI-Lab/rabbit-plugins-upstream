## Description:

A high-fidelity text-to-vector model with 4MP-tier quality, suitable for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use the skill to send text prompts to Recraft V4 Pro Vector and receive generated vector imagery for illustrations and design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy's hosted service, and local media may be uploaded for processing.

Mitigation: Review prompts and files before submission; avoid sending confidential or personal information unless approved for that service.

Risk: Using the skill requires a dLazy API key, and the setup flow stores credentials in the CLI configuration.

Mitigation: Keep the key private, use the documented login flow, and rotate or revoke it if exposed.

## Reference(s):

- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON with generated image URLs and metadata; optionally a saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID before the image is ready.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
