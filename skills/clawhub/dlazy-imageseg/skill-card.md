## Description:

Image matting skill that separates image foregrounds from backgrounds and returns transparent-background image URLs for product images, character cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call dLazy image segmentation for image matting workflows, such as product-image cleanup, character cutouts, and transparent-background composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are sent to dLazy's hosted service for processing.

Mitigation: Use explicit file paths intentionally and avoid sending sensitive images unless the user accepts third-party processing.

Risk: The workflow requires storing or passing a dLazy API key.

Mitigation: Use dLazy's supported authentication flow or environment variable handling, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Image segmentation calls may consume account credits.

Mitigation: Use the CLI dry-run mode before billable calls when cost or payload behavior needs confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted image URLs; asynchronous mode can return a task identifier for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
