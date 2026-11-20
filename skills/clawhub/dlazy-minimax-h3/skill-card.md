## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K. Supports text-to-video, first/last frame transitions and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short Hailuo video clips from text prompts, first and last frames, or reference images, videos, and audio. The CLI returns generated media links and task information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The description and CLI help differ on 4K support, and the login workflow is not clearly connected.

Mitigation: Check the installed CLI help and confirm the authentication flow before relying on those options.

Risk: The CLI implementation was not verified by the scan, and local references were unresolved.

Mitigation: Review the available CLI documentation and source before installing or sending prompts and media.

Risk: The skill documentation says local image, video, and audio inputs are uploaded to dLazy media storage.

Mitigation: Only provide media you are comfortable sending to the hosted service, and check its terms before use.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Audio, JSON]

**Output Format:** [Generated media assets with a JSON response containing hosted URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated clips are 5–15 seconds; asynchronous requests may return a generation ID and status.]

## Skill Version(s):

1.2.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
