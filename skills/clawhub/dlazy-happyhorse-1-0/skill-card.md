## Description:

Generates and edits videos with Happy Horse 1.0 from text prompts, first frames, or reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to generate videos from text, animate a first frame, create videos from reference images, or edit existing video using Happy Horse 1.0.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy for cloud generation.

Mitigation: Use the service only with content you are comfortable sharing with dLazy.

Risk: Video generation spends service credits.

Mitigation: Review cost estimates before submitting jobs.

Risk: Login saves the service API key in the local dLazy configuration.

Mitigation: Protect the local configuration and revoke the key through the dLazy dashboard if needed.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [JSON containing generated video asset URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return task status without generated assets.]

## Skill Version(s):

1.3.33 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
