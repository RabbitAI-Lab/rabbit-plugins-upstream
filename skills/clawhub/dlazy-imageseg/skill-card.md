## Description:

Image matting tool that separates foreground from background and returns a transparent-background image URL for product image processing, character cutout, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative production teams use this skill to remove image backgrounds through the dLazy hosted image segmentation CLI/API and receive transparent PNG output URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected image inputs and local file uploads are sent to dLazy's hosted API and media storage.

Mitigation: Submit only images that are acceptable for dLazy processing, and avoid sensitive images unless dLazy's terms and data handling are acceptable for the use case.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Use the npx invocation or DLAZY_API_KEY for per-run authentication when avoiding persistent global installs or saved API keys is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [JSON result with image output URL, plus optional shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted PNG output URLs from files.dlazy.com; async mode can return a task identifier for polling.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
