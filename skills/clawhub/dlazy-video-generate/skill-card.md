## Description:

Video generation skill that selects an appropriate dLazy CLI video model for text-to-video, image-to-video, first/last-frame video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform short videos through the dLazy CLI, including text-to-video, image-to-video, first/last-frame generation, digital human, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a hosted dLazy API and may upload prompts, images, video, or audio supplied by the user.

Mitigation: Use only media and prompts that are appropriate to send to dLazy, and review the service before using sensitive content.

Risk: Authentication stores a revocable dLazy API key in the local user configuration when using the CLI login flow.

Mitigation: Protect the local user account and rotate or revoke the API key from the dLazy dashboard when access should change.

Risk: The skill depends on the external @dlazy/cli package.

Mitigation: Review the pinned CLI package before installation in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands; dLazy CLI responses are JSON envelopes with hosted media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; media inputs may be uploaded to dLazy-hosted endpoints for generation.]

## Skill Version(s):

1.4.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
