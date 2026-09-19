## Description:

Image replicate tool: analyzes the visuals, composition, colors, lighting, and style of the source image, builds a replicate prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to replicate the visual style, composition, color, and lighting of a source image through the dLazy hosted image-generation CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI stores a dLazy API key in the user's local configuration or accepts it through DLAZY_API_KEY.

Mitigation: Use OS user permissions for the config file, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing keys in shared shells or logs.

Risk: User-selected local images or other media are uploaded to dLazy's cloud service for processing.

Mitigation: Provide only files that are approved for upload to dLazy and use dry-run or local review workflows before sending sensitive assets.

Risk: Installing a global npm CLI can affect the user's local toolchain and supply-chain posture.

Mitigation: Review the dLazy CLI source or npm package first, and use the pinned `npx @dlazy/cli@1.2.3` invocation when a persistent global install is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [JSON result objects, image URLs, optional downloaded image files, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when --no-wait is used; generated assets are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
