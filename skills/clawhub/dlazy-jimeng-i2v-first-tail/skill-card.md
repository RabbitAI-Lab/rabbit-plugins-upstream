## Description:

Generate coherent transition videos using Jimeng's first and tail frame models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Jimeng first-and-tail-frame image-to-video service from an agent, supplying a prompt plus first and last frame images to create transition video results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs the third-party @dlazy/cli npm package.

Mitigation: Install only if you trust dLazy and the package source; prefer npx or an isolated environment and avoid elevated privileges.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for one-off runs when appropriate, and rotate or revoke the key if the CLI or host environment is later distrusted.

Risk: Prompts, parameters, and selected media files are sent to dLazy services for generation.

Mitigation: Pass only files and prompts intended for upload, and review dLazy service terms before using sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or asynchronous task IDs through the dLazy CLI.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
