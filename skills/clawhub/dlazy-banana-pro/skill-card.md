## Description:

Generate/edit images with Nano Banana Pro, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate or edit images through dLazy's hosted Nano Banana Pro API from prompts and optional input images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files can be uploaded to dLazy's hosted service.

Mitigation: Use the skill only for content that may be processed by dLazy, and avoid sending sensitive prompts or private media unless that hosted processing is acceptable.

Risk: The dLazy CLI may save an API key in the local user configuration.

Mitigation: Use per-invocation credentials through DLAZY_API_KEY when persistent local storage is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: API use may consume dLazy credits.

Mitigation: Use dry-run or review cost estimates before generation when credit usage matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated image URLs, asynchronous task IDs, or save generated assets to a local path.]

## Skill Version(s):

1.2.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
