## Description:

Generates 1MP raster images through the dLazy Recraft V4 CLI for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operators use this skill to call dLazy's Recraft V4 image-generation CLI, set prompts and aspect ratios, and receive generated image URLs or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files passed to image, video, or audio fields are sent to dLazy's hosted API and media storage.

Mitigation: Confirm trust in the dLazy CLI and hosted service before use, and avoid sending sensitive content unless that use is approved.

Risk: The dLazy API key can be saved in the local CLI configuration file.

Mitigation: Use DLAZY_API_KEY per invocation when persistent credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy binary in the user environment.

Mitigation: Use the documented npx invocation for on-demand execution when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON output examples; generated results are image URLs or saved PNG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; can use npx without a persistent global install and supports async polling.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
