## Description:

Midjourney-style image generation with aspect-ratio, bot-type, and output-position controls for artistic, strongly stylized creative output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate Midjourney-style images through dLazy's hosted CLI/API, choosing prompt, aspect ratio, bot type, and grid or upscaled output position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files passed to the skill are sent to dLazy's hosted service.

Mitigation: Use the skill only with data approved for dLazy processing and avoid passing sensitive local files unless that transfer is intended.

Risk: The dLazy API key is a paid credential stored locally or supplied through the environment.

Mitigation: Protect the key, check local config permissions on shared machines, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Image URLs, Guidance]

**Output Format:** [JSON result with generated image URLs, or an async task identifier when no-wait mode is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload prompt data or media inputs to dLazy-hosted endpoints.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
