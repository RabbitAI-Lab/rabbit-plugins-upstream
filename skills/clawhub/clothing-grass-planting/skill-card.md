## Description:

Turns an outfit photo into social-style fashion images with a different model, pose, and setting while aiming to preserve the clothing details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use the skill to turn an outfit photo into lifestyle fashion images for social content, changing the model and setting while keeping the outfit consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outfit photos, reference images, and prompts are sent to the selected cloud image provider.

Mitigation: Use explicit image paths, avoid private or regulated photos, and review the provider and credentials before submission.

Risk: Generated images may misstate clothing details or imply a real person's endorsement.

Mitigation: Review clothing fidelity and obtain permission for likeness references; do not use outputs to impersonate people or fabricate endorsements.

Risk: Batch generation may incur cloud provider charges.

Mitigation: Run a dry run to inspect the request and estimated cost before generating images.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider and data-flow reference](artifact/references/provider-cli.md)
- [Image generation options](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [Locally saved JPEG, PNG, or WebP images; text guidance and generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional batches of scene variations; a dry run previews the request and estimated cost.]

## Skill Version(s):

1.0.15 (source: server-resolved release, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
