## Description:

Video Retalk uses the dLazy CLI and hosted API to generate a lip-synced talking-person video from an input video, voice audio, and optional reference face image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy VideoRetalk for lip-syncing a person video to a new speech audio track. It supports an optional reference face image to select the target person when the input video contains multiple faces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input videos, audio, and optional face reference images are uploaded to dLazy's hosted service for processing.

Mitigation: Avoid submitting private or sensitive media unless the user accepts the service handling it.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke saved keys from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
