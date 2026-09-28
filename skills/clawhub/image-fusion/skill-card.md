## Description:

Guides an agent in combining up to eight product photos into a coordinated fashion look on one model using cloud image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Retailers, creative teams, and agents create consistent ecommerce outfit images from product photos, with optional model or pose references and prompts for missing garments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model photos and prompts are sent to a selected cloud generation provider.

Mitigation: Use only images and prompts approved for that provider; obtain consent and a data-processing basis before using private or personally sensitive photos, and inspect the request with --dry-run.

Risk: Generation requests may use the wrong provider or expose reusable API credentials.

Mitigation: Choose or restrict the provider intentionally and use scoped, revocable API keys.

Risk: Generated garments or likenesses may differ from references or imply unauthorized endorsement.

Mitigation: Review outputs against the supplied products and do not use another person's likeness to imply endorsement.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Model flags](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands saves generated outfit images to a chosen path; results depend on the selected cloud provider.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
