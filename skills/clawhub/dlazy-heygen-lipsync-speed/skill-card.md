## Description:

HeyGen Lipsync Speed: Fast lip-sync model, ideal for scenarios requiring rapid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators can use the skill to generate fast lip-synced results from a video and audio input, with optional captions and audio adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local video or audio inputs may be sent to dLazy services, and generated media is hosted there; the security assessment has medium confidence and says the CLI package could not be resolved.

Mitigation: Before authenticating or sending media, review the dLazy CLI and confirm that the service's handling of your prompts and files is acceptable for your use.

Risk: The security assessment reports a possible mismatch between the stated lip-sync purpose and visible CLI login and authentication commands.

Mitigation: Review the CLI source and verify the skill's expected behavior before installation and use.

## Reference(s):

- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)

## Skill Output:

**Output Type(s):** [Media files, JSON]

**Output Format:** [JSON response with generated media URLs; optionally a downloaded media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when run without waiting.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
