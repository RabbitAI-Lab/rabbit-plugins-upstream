## Description:

Happy Horse 1.0 supports text-to-video, first-frame-to-video, reference-to-video, and video editing through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate videos from prompts or reference media and to edit existing videos through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial and does not establish how the CLI login flow handles authentication.

Mitigation: Review the CLI authentication behavior before logging in, use an organization API key that can be revoked, and rotate it if it may have been exposed.

Risk: Local image or video inputs are uploaded to dLazy media storage for processing.

Mitigation: Only provide media that you are permitted to share with the hosted service.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video asset and JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-to-video, first-frame-to-video, reference-to-video, and video editing; generation options include resolution, aspect ratio, and duration.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
