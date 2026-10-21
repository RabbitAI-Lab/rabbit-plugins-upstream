## Description:

Helps agents generate lip-synced media quickly from video and audio using the dLazy-hosted HeyGen Lipsync Speed service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request fast lip-sync generation from video and audio and retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication requires an API key that the CLI may store locally.

Mitigation: Protect the local key, use a per-invocation environment variable when appropriate, and rotate or revoke compromised keys.

Risk: Media supplied as local files is uploaded to dLazy's cloud service for generation.

Mitigation: Only submit media approved for third-party processing and review the service terms before use.

Risk: The documented example and output type do not match the video-and-audio lip-sync options.

Mitigation: Check the command's current help and inspect the returned result before relying on examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI documentation and source link](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include generated-media URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.34 (source: ClawHub release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
