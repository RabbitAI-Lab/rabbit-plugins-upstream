## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to ask an agent to generate Jimeng text-to-image results through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local image, video, or audio paths provided to the CLI may be uploaded to the third-party dLazy cloud service.

Mitigation: Install and use this skill only when the user accepts dLazy as a third-party cloud image-generation service, and avoid sending sensitive prompts or files unless approved.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not appropriate, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI returns generated image output metadata as JSON, including hosted file URLs; asynchronous calls can return a task identifier for polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
