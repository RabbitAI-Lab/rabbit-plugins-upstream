## Description:

Guides agents in generating short MiniMax Hailuo videos with audio from text prompts, frame transitions, or reference media through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from prompts, first and last frames, or reference images, video, and audio using the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Share only prompts and media approved for upload to the service.

Risk: Logging in saves a dLazy API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation if local key persistence is unwanted.

Risk: The documented output example shows an image despite the skill generating video.

Mitigation: Check actual response media types and URLs before relying on the example.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers generated video URLs, optional local downloads, and asynchronous task IDs.]

## Skill Version(s):

1.2.19 (source: server-resolved ClawHub release; bundled CLI instructions specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
