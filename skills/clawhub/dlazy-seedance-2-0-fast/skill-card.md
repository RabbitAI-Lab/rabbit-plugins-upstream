## Description:

Helps generate videos with Seedance 2.0 Fast using text prompts, media references, or first and last frames through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, media references, or first and last frames via dLazy's hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI may save an API key in local configuration.

Mitigation: Protect the local key, use per-invocation credentials when appropriate, and rotate or revoke exposed keys.

Risk: Prompts and selected local media are sent to dLazy's hosted service for generation.

Mitigation: Confirm that the prompts and media are appropriate to share with the service before submitting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [CLI commands and JSON generation results with hosted output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous generation ID; generated assets may be downloaded to a local path.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
