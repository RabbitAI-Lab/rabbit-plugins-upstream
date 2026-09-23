## Description:

Image matting tool that separates foregrounds from backgrounds and returns transparent-background image URLs for product imagery, character cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy image segmentation from an agent, submitting an image URL or local image file and receiving a transparent-background image URL or saved asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs, including local files, may be uploaded to dLazy services for processing.

Mitigation: Only pass images you are comfortable uploading to dLazy, and review the service terms before use.

Risk: Using `dlazy login` or `dlazy auth set` can persist an API key in the local dLazy CLI configuration.

Mitigation: Use the `DLAZY_API_KEY` environment variable for per-run authentication when persistent local configuration is not desired.

Risk: The skill depends on a third-party npm CLI and hosted API.

Mitigation: Review the dLazy CLI source and package before installing, or use `npx @dlazy/cli@1.2.3` to avoid a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples; runtime CLI output is JSON containing image result URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; local image inputs may be uploaded to dLazy-hosted endpoints, and --save can download a returned PNG asset.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
