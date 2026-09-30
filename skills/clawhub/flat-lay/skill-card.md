## Description:

Guides agents in turning garment flat-lay images and pose references into on-model e-commerce images using a configured image provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to prepare virtual try-on product imagery from clothing photos and pose or scene references. It provides prompts and commands for generating and reviewing catalog images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected clothing, reference, and optional face images and prompts are sent to a cloud image provider.

Mitigation: Use only images you are comfortable sharing with the configured provider and obtain permission for any person's likeness.

Risk: Image-generation requests may consume paid credits.

Mitigation: Use dry-run to review estimated cost before submitting a generation request.

Risk: Provider credentials grant access to external image-generation services.

Mitigation: Keep API keys scoped and revocable, and do not disclose them in prompts or shared outputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can save generated image files locally.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
