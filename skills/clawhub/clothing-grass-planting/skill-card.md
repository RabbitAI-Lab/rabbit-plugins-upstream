## Description:

Turns outfit photos into social-media-style lifestyle images with new models, poses, and scenes while aiming to preserve the clothing and accessories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and apparel marketers use the skill to turn an existing outfit photo into lifestyle images for social posts, changing the model and setting while keeping the outfit recognizable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clothing photos, reference images, and prompts are sent to the selected cloud image provider, potentially exposing private personal images.

Mitigation: Check the selected provider and its privacy terms before uploading; avoid private personal images unless those terms are acceptable.

Risk: Image generation may incur charges through the configured provider.

Mitigation: Check which provider key is configured and use dry-run to review requests and estimated costs first.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider setup and usage](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image files]

**Output Format:** [Prompt guidance and shell commands; generated JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggested portrait output is 1024×1536; generated images are saved locally.]

## Skill Version(s):

1.0.23 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
