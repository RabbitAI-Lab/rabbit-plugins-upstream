## Description:

Generates a video with a speaker's lip movements synchronized to supplied audio for dubbing, localization, and virtual presenters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams can dub, localize, or resynchronize a speaker by supplying a video and audio track and receiving a lip-synced video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio are uploaded to dLazy for processing, and requests use account credits.

Mitigation: Send only media you are authorized to share, and check the service terms and credit cost before use.

Risk: The generic prompt and image-output examples do not match the documented lip-sync inputs and output.

Mitigation: Check `dlazy sync-lipsync-3 -h` and use the documented video and audio options before running.

Risk: The workflow requires a dLazy API key.

Mitigation: Keep the key private and rotate or revoke it if it is exposed.

## Reference(s):

- [CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files]

**Output Format:** [Lip-synced video returned by URL or saved as a local file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A generated video asset; it can be saved locally with the CLI.]

## Skill Version(s):

1.3.35 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
