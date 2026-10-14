## Description:

Turns garment flat-lay images and pose references into on-model e-commerce photos while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to create model-worn product photos from garment images and pose references, optionally keeping a consistent model across products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment, model, and reference images and prompts are sent to a cloud image provider.

Mitigation: Use only images and prompts you are authorized to share; check the provider and request with doctor or dry-run before generation.

Risk: Unauthorized portraits could be used to imply a person's endorsement.

Mitigation: Avoid sensitive or unauthorized portraits and do not use generated images to fabricate commercial endorsements.

Risk: Generated files may be written to unintended locations in shared workspaces.

Mitigation: Choose and review the output path before saving.

## Reference(s):

- [Flat Lay skill release](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider and authentication reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and commands; generated JPEG product photos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved to a chosen local path; review garment fidelity and image quality before use.]

## Skill Version(s):

1.0.21 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
