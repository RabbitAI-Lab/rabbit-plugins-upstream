## Description:

Generates detailed vector-style illustrations from text prompts through dLazy's Recraft V4 Pro Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to generate detailed artwork from text prompts through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media files explicitly supplied to the CLI are sent to dLazy's hosted service.

Mitigation: Review prompts and supplied media for sensitive information before submitting them.

Risk: Installation runs a third-party npm CLI, and the service requires an API key.

Mitigation: Review the CLI before installing, use npx to avoid a global install if preferred, and rotate or revoke the API key through the service dashboard when needed.

## Reference(s):

- [dLazy CLI source and documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image assets]

**Output Format:** [JSON response containing a generated image URL; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of an image URL.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
