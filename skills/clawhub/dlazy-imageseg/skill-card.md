## Description:

Image matting tool that separates foreground from background and returns a transparent-background URL for product image processing, character cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy image segmentation for product images, character cutouts, and compositing workflows. It helps agents produce transparent-background image results through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input images and task parameters are sent to the dLazy API, and local image files may be uploaded to dLazy media storage.

Mitigation: Use the skill only with images and prompts that are appropriate to send to dLazy's service.

Risk: A global installation of the external dLazy CLI creates a persistent local dependency.

Mitigation: Prefer `npx @dlazy/cli@1.2.3` when persistent installation is unnecessary, and review the referenced source or package before use in sensitive environments.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use API keys only in trusted environments and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text]

**Output Format:** [CLI command guidance and JSON result metadata with a hosted transparent PNG URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; input images may be uploaded to dLazy media storage; asynchronous invocations may return a task ID before final output is available.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
