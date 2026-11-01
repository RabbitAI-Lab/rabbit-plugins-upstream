## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts and images, or extend an existing video, through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy, and generated assets are hosted by its service.

Mitigation: Only submit media you are comfortable uploading to dLazy.

Risk: The dLazy organization API key is stored in local CLI configuration when using the documented login flow.

Mitigation: Protect the local configuration, use the documented environment-variable option when appropriate, and rotate or revoke the key if needed.

Risk: Video generation may incur account charges.

Mitigation: Review expected charges and account credits before generating.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project listed in skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands, Configuration guidance]

**Output Format:** [Generated video asset URL and JSON result/status; optionally a downloaded video file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Frames mode supports 4, 6, or 8 second videos; extend mode adds 7 seconds. Frames mode supports 16:9 or 9:16 and listed resolutions of 720p, 1080p, or 4K.]

## Skill Version(s):

1.3.35 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
