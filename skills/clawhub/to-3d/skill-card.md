## Description:

Turns flat-lay clothing photos into dimensional ghost-mannequin product images while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce content creators and product teams use this skill to turn single-garment flat-lay photos into volumetric, mannequin-free product shots for listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud image provider.

Mitigation: Share only approved images and trusted public URLs; use a dry run before sending data and keep API keys scoped and rotatable.

Risk: Generated files may overwrite important local outputs, and synthesized garment details may be inaccurate.

Mitigation: Choose a safe output path and review the result against the source garment before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown instructions and commands; generated JPEG product images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square or portrait output and optional local image files.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
