## Description:

Generates images, videos, and audio by selecting a suitable dLazy CLI model based on the user's intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users use this skill to route image, video, and audio creation requests to a suitable dLazy CLI model and receive generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad generation triggers may start media generation for an unrelated request.

Mitigation: Confirm that the user intends to generate media and identify the requested media type before invoking a generation command.

Risk: Prompts and supplied local media are sent to dLazy-hosted services, and generation may incur charges.

Mitigation: Before generation, confirm the user intends to use the external service, avoid sending sensitive content without authorization, and check that the expected cost is acceptable.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, URLs]

**Output Format:** [Generated media files or hosted media URLs, with JSON command output]

**Output Parameters:** [Prompts and optional reference media]

**Other Properties Related to Output:** [Available formats and model options depend on the selected generation command.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
