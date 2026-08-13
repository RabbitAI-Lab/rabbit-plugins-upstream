## Description:

Image Replicate analyzes a source image's visuals, composition, colors, lighting, and style, then uses the dLazy image-replicate CLI flow to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to ask an agent to run dLazy's image-replication workflow for style-consistent image generation from reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy, and generated outputs are hosted by dLazy.

Mitigation: Avoid submitting sensitive prompts or media unless the user accepts dLazy processing and hosting for that content.

Risk: Logging in can save a dLazy API key in the local CLI configuration.

Mitigation: Use the pinned npx invocation or the DLAZY_API_KEY environment variable when persistent local credentials are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns image output metadata and hosted result URLs; async mode may return a generation task identifier for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
