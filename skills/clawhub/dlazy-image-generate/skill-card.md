## Description:

Selects a dLazy image model to generate or edit images from prompts and optional reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate, edit, upscale, or vectorize images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media are sent to dLazy's hosted service.

Mitigation: Send only content approved for third-party processing and review referenced files before use.

Risk: The skill depends on a third-party CLI package and an API key.

Mitigation: Review the pinned package before installation; rotate or revoke the API key when no longer needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)

## Skill Output:

**Output Type(s):** [Images, Text]

**Output Format:** [JSON CLI response with hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation and editing results may include hosted URLs; reference media may be uploaded.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
