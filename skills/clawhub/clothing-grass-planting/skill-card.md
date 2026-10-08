## Description:

Turns outfit photos into social-style images with new models, poses, and settings while aiming to preserve the clothing and accessories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use an outfit photo, optionally with a model or setting reference, to make lifestyle images for social posts while keeping the pictured outfit consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and clothing, model, or reference photos are sent to a cloud image provider.

Mitigation: Use a dry run to inspect the request, select the provider explicitly when privacy or billing matters, and share only images authorized for upload.

Risk: Generated likenesses could imply a real person's endorsement or experience.

Mitigation: Do not use real people's images for impersonation, fabricated endorsements, or face-swap-like outputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Image model options](artifact/references/model-flags.md)
- [Provider setup and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Image files, Prompt text, Shell commands]

**Output Format:** [Generated images (JPEG by default) with text guidance and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batches and a dry run that previews the request before generation.]

## Skill Version(s):

1.0.17 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
