## Description:

Helps agents use dLazy's HeyGen Lipsync Speed service to synchronize video lip movements with audio quickly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through fast video lip-sync generation from video and audio inputs using the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are sent to dLazy cloud endpoints.

Mitigation: Confirm the user is comfortable sharing the selected media with dLazy before submission.

Risk: Authentication uses an API key stored locally or provided via an environment variable.

Mitigation: Protect the key, avoid exposing it in shared commands or logs, and rotate it if compromised.

Risk: Some examples incorrectly mention --prompt and image/png output for this lip-sync command.

Mitigation: Check command help for the required video and audio flags and verify the actual output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI generation results may include hosted media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
