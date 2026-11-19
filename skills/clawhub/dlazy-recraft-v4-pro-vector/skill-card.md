## Description:

Generates high-fidelity vector artwork from text prompts with Recraft V4 Pro Vector, for detailed illustrations and production-grade SVG assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to create detailed vector-style illustrations from text prompts through dLazy. It returns generated image assets for use in creative and production workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the advertised vector-generation purpose and documented authentication steps, with partial review coverage.

Mitigation: Review the CLI package and authentication flow, and confirm its credential handling before installing or signing in.

Risk: Prompts and local media provided to the skill are sent to dLazy-hosted services for processing and storage.

Mitigation: Avoid sending sensitive prompts or media unless their transfer to the service is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON response with generated image URLs and metadata; optionally a downloaded image file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented response example uses PNG; a local save path is optional.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
