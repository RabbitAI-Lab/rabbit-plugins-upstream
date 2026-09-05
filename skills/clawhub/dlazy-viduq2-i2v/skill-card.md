## Description:

Convert static images into dynamic videos using Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn static images into short generated videos through the dLazy hosted Vidu Q2 image-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-provided image, audio, or video paths may be sent to dLazy infrastructure for generation.

Mitigation: Avoid sending sensitive media unless dLazy processing is acceptable for the user's account and data policy.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Use per-invocation environment variables when persistent local credentials are not appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated assets are returned as URLs hosted by dLazy.

Mitigation: Review generated output and sharing requirements before distributing returned URLs or downloaded files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown instructions with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video result URLs are hosted by dLazy; asynchronous runs can return a generation ID for polling.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
