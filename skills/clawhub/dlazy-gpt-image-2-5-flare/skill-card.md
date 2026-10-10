## Description:

Helps agents generate and edit images with GPT Image 2.5 Flare through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit images using references, with selectable aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images may be uploaded to the dLazy service, which hosts generated outputs.

Mitigation: Avoid sensitive prompts and files unless their upload and external hosting are acceptable.

Risk: Authentication may store a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it in the provider dashboard if needed.

Risk: Installing the third-party CLI globally leaves a persistent executable on the device.

Mitigation: Review the CLI before installing; use the documented npx option if a persistent global installation is not desired.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image files]

**Output Format:** [JSON with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs can return a task ID for later retrieval.]

## Skill Version(s):

1.2.16 (source: ClawHub release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
