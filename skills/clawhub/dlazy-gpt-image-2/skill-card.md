## Description:

Helps agents generate images from text and edit images using reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request new images from text prompts or edit and combine images with reference inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images are sent to dLazy's hosted service.

Mitigation: Use the service only for content you are comfortable sharing with dLazy.

Risk: Signing in can save an API key in local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY if you do not want the key saved locally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns image URLs; images can optionally be saved locally.]

## Skill Version(s):

1.3.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
