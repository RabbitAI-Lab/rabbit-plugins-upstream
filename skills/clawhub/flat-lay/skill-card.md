## Description:

Turns garment flat-lay images and pose references into on-model product images for apparel listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Apparel sellers and creative teams use the skill to create on-model catalog photos from garment images and pose references, with optional consistent model appearance across products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, model, and reference images may be uploaded to the selected cloud provider.

Mitigation: Review provider settings and send only images and paths you are authorized to share.

Risk: Provider credentials may grant access to paid generation services.

Mitigation: Use limited, revocable API keys and review estimated charges before generating.

Risk: The bundled generator exposes tasks beyond this flat-lay workflow.

Mitigation: Check the selected task and proposed command before execution.

## Reference(s):

- [Flat Lay ClawHub listing](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider setup and data flow](references/provider-cli.md)
- [Image generation options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown guidance and shell commands; generated JPEG, PNG, or WebP images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be saved locally; cloud generation may incur usage charges.]

## Skill Version(s):

1.0.16 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
