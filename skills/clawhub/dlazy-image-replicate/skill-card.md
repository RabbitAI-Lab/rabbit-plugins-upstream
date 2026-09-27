## Description:

Image Replicate analyzes a source image's composition, colors, lighting, and style, builds a replication prompt, and invokes Seedream 4.5 through the dLazy CLI to generate a new image in a similar style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate new images that follow the visual style of user-supplied reference images. The agent invokes a pinned dLazy CLI command and can return generated image URLs or saved output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to the dLazy hosted service.

Mitigation: Use the skill only with media and prompts approved for upload to dLazy, and review dLazy service terms before use.

Risk: Authentication requires storing or providing a dLazy API key.

Mitigation: Use OS-restricted CLI configuration or the DLAZY_API_KEY environment variable, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy binary on the user's machine.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global install is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, files]

**Output Format:** [JSON responses from the dLazy CLI, with optional image URLs or saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and npm or npx; generated output URLs are hosted by dLazy.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
