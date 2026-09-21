## Description:

ByteDance's latest video generation model. Supports multi-modal reference (images, video, audio) to generate videos, as well as first/last frame and text-to-video modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through the dLazy Seedance 2.0 CLI from text prompts, reference images, video, audio, or first and last frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media files are sent to the third-party dLazy service for generation.

Mitigation: Use the skill only with content appropriate for dLazy processing, and avoid passing sensitive media or prompts unless approved for that service.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where persistent storage is not desired, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Generated files are hosted by dLazy and returned as service URLs.

Mitigation: Review generated output links and hosting expectations before sharing or using the generated media downstream.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted media URLs, async task identifiers, or save generated media to a local path.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
