## Description:

GPT Image 2.5 Sunburst is a dLazy-hosted image generation skill for text-to-image and image editing workflows that need fine detail, in-image text, reference images, wide aspect ratios, and high quality outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative practitioners, and external users can use this skill to ask an agent to generate or edit images through the pinned dLazy CLI, including reference-image workflows and optional local result downloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided media may be sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only when the user accepts that hosted-service data flow, and avoid sending sensitive prompts or media unless approved for that service.

Risk: Authentication may save a revocable dLazy API key in the user's local CLI configuration.

Mitigation: Use a scoped key where possible, keep local config access restricted to the OS user, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists a dLazy binary on the system.

Mitigation: Use the pinned npx command for one-time execution when a persistent global CLI install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result with hosted image URLs, async task metadata when requested, and optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry runs, asynchronous generation, timeout control, reference images, aspect ratio selection, quality selection, and local result saving.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
