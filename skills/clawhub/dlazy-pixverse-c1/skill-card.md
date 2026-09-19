## Description:

PixVerse C1 generates videos from text prompts, images, first and last frames, or reference media, with emphasis on action, VFX, and high-motion scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to call dLazy's hosted PixVerse C1 video-generation CLI for text-to-video, image-to-video, first/last-frame-to-video, and reference-to-video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends prompts, parameters, and referenced media files to dLazy's hosted service.

Mitigation: Review prompts and media before invocation, and avoid sending sensitive data unless the user accepts the hosted-service handling.

Risk: The login flow stores an API key in the local CLI configuration.

Mitigation: Use a revocable API key, rotate or revoke it when needed, and prefer per-invocation DLAZY_API_KEY for temporary access.

Risk: Installing the global CLI persists the pinned @dlazy/cli package on the system.

Mitigation: Prefer npx @dlazy/cli@1.2.3 for on-demand use when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, saved local assets, or asynchronous task identifiers.]

## Skill Version(s):

1.2.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
