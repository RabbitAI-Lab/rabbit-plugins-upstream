## Description:

Generates original music from a natural-language prompt using ElevenLabs Music through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate music for background tracks, advertisements, and short videos from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external CLI executes third-party software.

Mitigation: Review the pinned dLazy CLI package before installing or running it.

Risk: Prompts and explicitly provided media files are sent to dLazy's hosted service.

Mitigation: Send only content you are authorized to share with that service.

Risk: A dLazy API key may be stored locally or passed to the CLI.

Mitigation: Protect the key from disclosure and revoke or rotate it if compromised.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Text with shell commands and a generated asset link or saved file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later polling.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
