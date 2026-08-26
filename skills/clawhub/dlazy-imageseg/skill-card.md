## Description:

Image matting tool that separates foreground from background and returns a transparent-background image URL for product image processing, character cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to invoke dLazy image segmentation from an agent workflow, uploading a selected image and receiving a hosted transparent-background PNG result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images selected by the user are uploaded to dLazy cloud endpoints for processing.

Mitigation: Use the skill only for images that are appropriate to process with dLazy as a cloud service.

Risk: The dLazy CLI requires an API key and may store it in the local user configuration.

Mitigation: Review local file permissions and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted image URLs and can save generated image assets locally when requested.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
