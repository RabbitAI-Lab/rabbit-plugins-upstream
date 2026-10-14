## Description:

Creates visual garment previews that retain a reference garment's silhouette while applying the texture and appearance of a supplied fabric swatch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and product teams use this skill to preview a garment design in different fabrics before physical sampling. It provides prompt guidance and commands for generating and reviewing visual mockups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, fabric references, and prompts are sent to the selected cloud image provider.

Mitigation: Use local files or trusted image URLs; avoid confidential designs unless the provider's terms permit their use.

Risk: Running image-generation commands may incur charges or send images to an unintended provider.

Mitigation: Review the selected provider and run a dry-run before paid generation when destination or cost matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Image model flags](artifact/references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and CLI commands; generated garment preview images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; not a substitute for physical fabric or fit samples.]

## Skill Version(s):

1.0.21 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
