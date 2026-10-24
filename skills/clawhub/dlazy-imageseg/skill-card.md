## Description:

Image matting tool: separates foreground from background and returns a transparent-background URL, suitable for product image processing, character cutout, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers can remove backgrounds from product or portrait images and use the transparent results in compositions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to dLazy's hosted service for processing, and processing may incur costs.

Mitigation: Submit only images approved for third-party processing and use the documented dry-run cost preview before processing.

Risk: The CLI uses an organization API key stored in local configuration.

Mitigation: Protect the API key and review the pinned CLI source and version before installation.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, JSON]

**Output Format:** [JSON result containing a transparent-background image URL; optionally saves the image to a local file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs can return a task ID and status before an image is available.]

## Skill Version(s):

1.3.33 (source: target release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
