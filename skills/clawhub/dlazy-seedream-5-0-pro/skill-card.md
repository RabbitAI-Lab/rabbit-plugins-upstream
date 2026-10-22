## Description:

Helps agents generate detailed images, including typography and complex compositions, for brand assets and commercial key visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and brand teams use this skill to ask an agent for generated images and commercial visual assets from text prompts, optionally using reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media can be sent to dLazy's cloud service.

Mitigation: Avoid submitting sensitive prompts or files unless cloud processing is acceptable.

Risk: The CLI may save a dLazy API key locally, and global installation persists the CLI.

Mitigation: Use npx for one-off runs when preferred, and rotate or revoke the key in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text and shell commands; the CLI returns JSON with generated image URLs or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can optionally be saved locally. The skill specifies dLazy CLI version 1.2.3.]

## Skill Version(s):

1.2.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
