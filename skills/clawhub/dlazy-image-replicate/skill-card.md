## Description:

Analyzes a reference image's composition, colors, lighting, and style, then creates a prompt for generating a new image in a similar style with Seedream 4.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to analyze a reference image and request a new image with a similar visual style through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and submitted images are sent to dLazy, and local image paths are uploaded for processing.

Mitigation: Submit only images and prompts you are comfortable sharing with dLazy.

Risk: Image generation can incur usage charges.

Mitigation: Review the CLI cost estimate with --dry-run before generating.

Risk: The API key is stored in the local CLI configuration after login.

Mitigation: Protect the local account and configuration, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image file or URL, with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can run asynchronously; results can be saved to a local path.]

## Skill Version(s):

1.3.38 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
