## Description:

Provides Midjourney-style image generation through the dLazy CLI, with aspect ratio, bot type, and grid or upscaled output controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to request strongly stylized image generations from dLazy's hosted service through an agent-driven CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted API and media storage.

Mitigation: Avoid passing private prompts or files unless they are intended for cloud processing by dLazy.

Risk: The workflow depends on the third-party @dlazy/cli npm package.

Mitigation: Prefer the pinned npx invocation for on-demand use, and review the package/source before installing a persistent global CLI.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Keep the key scoped and revocable, rotate it if exposed, or pass it per invocation with DLAZY_API_KEY when persistent storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses containing image output URLs, optional saved image files, and concise agent guidance for authentication or balance errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when no-wait mode is used; generated image assets are hosted by files.dlazy.com.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
