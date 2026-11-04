## Description:

High-fidelity text-to-vector generation for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use this skill to generate detailed vector illustrations from text prompts through dLazy's hosted Recraft V4 Pro Vector service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service for generation.

Mitigation: Submit only prompts and media that are approved for sharing with the service.

Risk: Logging in stores an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key when needed.

Risk: The supplied security review does not cover a full audit of the external CLI or service.

Mitigation: Review the pinned CLI before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands]

**Output Format:** [Generated image assets with a JSON response containing output URLs and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally save the generated asset to a local path; asynchronous jobs may return a task identifier.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
