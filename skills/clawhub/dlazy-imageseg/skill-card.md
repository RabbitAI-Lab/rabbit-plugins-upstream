## Description:

Separates foregrounds from image backgrounds and returns transparent-background result URLs for product images, person cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy image segmentation for background removal from supplied image URLs or local image paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected image paths or media URLs may be uploaded to dLazy for processing.

Mitigation: Only process media the user is authorized to share with dLazy, and avoid sending sensitive images unless that use is approved.

Risk: Authentication can store a revocable API key in the local dLazy config.

Mitigation: Use the `DLAZY_API_KEY` environment variable for one-off runs when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated outputs are hosted by dLazy.

Mitigation: Review resulting URLs before sharing them and apply the same confidentiality rules used for the source media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked service returns image output URLs and can save generated assets locally when requested.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
