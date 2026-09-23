## Description:

Video generation skill that selects an appropriate dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, digital-human, and lip-sync workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route video-generation requests through dLazy CLI models, including text-to-video, image-to-video, reference-driven video, digital-human video, segmentation, and lip-sync generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media files may be sent to dLazy cloud endpoints for generation.

Mitigation: Use the skill only with content appropriate for dLazy's hosted service, and avoid submitting sensitive media unless the user accepts that transfer.

Risk: The dLazy CLI uses an API key and may store it in the local user configuration.

Mitigation: Prefer per-invocation credentials or the documented login flow as appropriate, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: Using the hosted generation service may consume account credits.

Mitigation: Confirm the user has sufficient dLazy credits before long or repeated generation runs.

Risk: A persistent global CLI install increases local dependency footprint.

Mitigation: Use the pinned npx invocation when a temporary CLI execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands; dLazy commands return JSON envelopes containing generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; prompts, parameters, and selected image, video, or audio inputs may be sent to dLazy endpoints.]

## Skill Version(s):

1.4.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
