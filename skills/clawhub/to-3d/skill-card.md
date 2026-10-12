## Description:

Turns flat-lay clothing photos into dimensional ghost-mannequin product images while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to turn single-garment flat-lay photos into ghost-mannequin product imagery for listings and catalogs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos and prompts may be sent to dLazy or another selected image provider.

Mitigation: Use only images and prompts appropriate to share with the chosen provider; avoid untrusted image URLs.

Risk: Image generation can incur provider charges and require API credentials.

Mitigation: Use dry-run before paid calls and keep API keys scoped and revocable.

Risk: Generated product images may misrepresent garment details or show unintended artifacts.

Mitigation: Review image outputs against the original garment before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/to-3d)
- [Provider CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with prompts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image generation and review; the selected image provider produces the final product image files.]

## Skill Version(s):

1.0.20 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
