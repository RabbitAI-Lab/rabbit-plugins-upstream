## Description:

This skill helps agents analyze an input image's composition, color, lighting, and style, then use dLazy's image-replicate CLI workflow to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative agents use this skill to create an image in the visual style of a supplied reference image through the dLazy hosted generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input image or media paths may be uploaded to dLazy's hosted service for processing.

Mitigation: Use only images and media approved for upload to dLazy, and review the service's data handling terms before use.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-invocation credentials when appropriate, restrict local config access, and rotate or revoke the key from dLazy if exposure is suspected.

Risk: A globally installed CLI can persist beyond the immediate task.

Mitigation: Use `npx @dlazy/cli@1.2.3` for on-demand execution when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted image URLs, saved local files, or asynchronous task identifiers from the dLazy CLI.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
