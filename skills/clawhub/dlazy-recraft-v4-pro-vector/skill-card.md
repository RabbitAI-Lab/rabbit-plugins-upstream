## Description:

High-fidelity text-to-vector generation for production-grade SVG assets and detailed illustrations, with 4MP-tier quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can submit text prompts to dLazy's Recraft V4 Pro Vector service to create detailed vector-style artwork and save the returned image asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial; some CLI references remain unresolved, and the documented login flow is not clearly connected to vector generation.

Mitigation: Review the pinned CLI package and confirm its login and hosted API behavior before installation; provide an API key only if comfortable with that service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with a generated image URL and image metadata (the example output is PNG)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result can be downloaded to a local path with --save.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
