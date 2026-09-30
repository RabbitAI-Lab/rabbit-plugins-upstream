## Description:

Combines up to eight clothing and accessory photos into a coordinated catalog look on one model, with optional pose and model references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce merchandisers and creative teams use this skill to create coordinated outfit photos from separate product images while keeping a consistent model and studio style across looks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and product or model images are sent to the configured image provider.

Mitigation: Use an approved provider, avoid private images, review API key setup and destinations, and check costs with --dry-run.

Risk: Generated looks may change or omit product details, or use a person's likeness without permission.

Mitigation: Review every image against its product references before publishing, and use model photos only with authorization.

## Reference(s):

- [ClawHub image-fusion release](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Text prompts and CLI commands; generated image files and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batch generation and saving images locally; prompts and selected images are sent to the configured provider.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
