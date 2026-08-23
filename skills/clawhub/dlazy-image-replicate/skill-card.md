## Description:

Image Replicate analyzes a source image's visuals, composition, colors, lighting, and style, then uses dLazy's hosted image generation service to produce a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to replicate the style of reference images through the dLazy CLI. The skill helps an agent authenticate, submit image-replication requests, and interpret JSON responses that contain generated image URLs or async task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image files are sent to dLazy's hosted service.

Mitigation: Do not submit sensitive or restricted content unless the user accepts dLazy's data handling for the task.

Risk: Logging in can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication when persistence is not desired, and rotate or revoke keys that are no longer needed.

Risk: The skill depends on an external CLI and hosted API availability.

Mitigation: Use the pinned npx invocation when possible and handle unauthorized, insufficient-balance, and async task failures before reporting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, JSON, Image URLs]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as hosted URLs; async runs can return a task identifier for later polling.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
