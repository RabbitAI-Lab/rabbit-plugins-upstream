## Description:

Generates fast lip-synced video from supplied video and audio using HeyGen Lipsync Speed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can use the skill to synchronize speech audio with a video for rapid lip-sync generation. It supports options such as captions, duration adjustment, speech enhancement, and handling the original music track.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio files supplied by local path are uploaded to dLazy's hosted media service for processing.

Mitigation: Only submit media you are authorized to share, and review the service terms before sending sensitive content.

Risk: The security review is partial and reports a mismatch between the lip-sync description and CLI authentication behavior.

Mitigation: Check the CLI help and confirm the requested action and inputs before running the skill; the scan verdict is not a guarantee of safety.

Risk: The API key is saved in the local CLI configuration when using the recommended login flow.

Mitigation: Restrict access to the account and local configuration, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)

## Skill Output:

**Output Type(s):** [Video asset, JSON, Shell commands]

**Output Format:** [CLI JSON response with generated media URLs; optionally a downloaded media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.3.45 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
