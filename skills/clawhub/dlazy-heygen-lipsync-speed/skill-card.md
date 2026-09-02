## Description:

HeyGen Lipsync Speed is a dLazy CLI skill for generating fast lip-sync results from user-provided video and audio inputs through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run the dLazy HeyGen Lipsync Speed command, passing video and audio inputs for rapid lip-sync generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio inputs supplied to the skill are sent to dLazy's hosted service for processing.

Mitigation: Use the skill only for media that may be processed by dLazy, and avoid submitting sensitive or restricted content unless that use is approved.

Risk: The skill requires a dLazy API key stored locally or supplied through the environment.

Mitigation: Protect the API key, prefer per-invocation or pinned npx usage when appropriate, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs or asynchronous task identifiers from the dLazy service.]

## Skill Version(s):

1.3.12 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
