## Description:

Turns a clothing photo into a clean, white-background flat-lay product image of a selected garment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use the skill to isolate a garment from model, street-style, or customer photos and prepare a flat-lay image for product listings or further image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos, prompts, and generated images are sent to the selected cloud provider.

Mitigation: Use only photos you have permission to share; check the provider's data handling and use --dry-run to inspect requests.

Risk: Hidden garment details may be guessed rather than faithfully reproduced.

Mitigation: Review generated details against source photos, especially where the garment was obscured.

Risk: Generated files may be saved to an unintended location.

Mitigation: Check --save paths before running generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [JPEG or PNG flat-lay image; Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One garment per generation; occluded garment details are inferred and need review.]

## Skill Version(s):

1.0.24 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
