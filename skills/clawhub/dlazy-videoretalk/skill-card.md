## Description:

Helps agents generate a lip-synced talking-person video from a source video and replacement speech audio, with an optional reference face for multi-person scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a speaker's mouth movements in a video with new voice audio, optionally selecting a face when multiple people appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video, audio, or reference images supplied to the CLI can be uploaded to dLazy.

Mitigation: Share only media authorized for upload and review the dLazy CLI package before installation.

Risk: The API key is stored in local configuration or supplied through an environment variable.

Mitigation: Keep the key out of logs and repositories; rotate it if exposed.

Risk: Some skill examples use incorrect prompt or image flags for Video Retalk.

Mitigation: Use `dlazy videoretalk -h` to confirm supported flags before running a request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance and JSON results containing generated-media URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated media locally when requested.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
