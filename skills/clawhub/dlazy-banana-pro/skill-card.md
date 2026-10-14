## Description:

Generate and edit images with Nano Banana Pro from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images using references through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy, and generated images are hosted remotely.

Mitigation: Confirm with the user before uploading local media; avoid sending sensitive content without approval.

Risk: Image generation may consume account credits.

Mitigation: Check estimated cost when available and confirm with the user before billable calls.

Risk: The CLI may save an API key on the user's device.

Mitigation: Keep credentials private and use the account's key rotation or revocation controls if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown and shell commands; the CLI returns JSON with image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are hosted remotely and can optionally be saved locally.]

## Skill Version(s):

1.2.32 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
