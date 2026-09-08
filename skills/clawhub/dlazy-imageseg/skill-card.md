## Description:

Image matting tool that separates foreground subjects from backgrounds and returns a transparent-background image URL for product images, character cutouts, and composition workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to remove image backgrounds through the dLazy CLI and hosted image segmentation API. It is suited for preparing product imagery, foreground cutouts, and compositing assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs are uploaded to dLazy's hosted service for processing.

Mitigation: Only pass images approved for upload to dLazy, and prefer local or on-demand execution patterns for sensitive environments.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use user-scoped credentials, avoid running npm or the CLI as administrator/root, and rotate or revoke keys when access changes.

Risk: The skill depends on the third-party dLazy CLI and remote API endpoints.

Mitigation: Review the referenced package and source before installation in sensitive environments, and pin the documented CLI version when deploying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted transparent-background image URLs and can save result assets locally through the dLazy CLI.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
