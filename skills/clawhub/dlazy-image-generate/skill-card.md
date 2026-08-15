## Description:

Image generation skill that automatically selects an appropriate dLazy CLI image model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, upscale, segment, vectorize, or transform images through dLazy CLI image models from natural-language prompts and optional media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files explicitly passed to the CLI may be sent to dLazy's hosted service.

Mitigation: Avoid passing sensitive prompts or local media files unless the user has approved sending them to the hosted service.

Risk: Authentication stores a dLazy API key locally for future CLI use.

Mitigation: Use per-invocation authentication or npx when persistence is not desired, and rotate or revoke the API key from the dLazy dashboard if needed.

Risk: A global CLI install persists tooling on the user's machine.

Mitigation: Use the pinned npx invocation when the user does not want a persistent global CLI installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command output from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may return generated media URLs hosted by dLazy and may chain CLI commands using JSON envelope output.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
