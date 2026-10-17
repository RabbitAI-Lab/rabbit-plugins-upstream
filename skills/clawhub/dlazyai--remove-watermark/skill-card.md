## Description:

Guides image cleanup to remove watermarks, text, badges, and promotional overlays while reconstructing covered backgrounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and e-commerce teams use this skill to prepare cleaner product images by removing authorized text and overlays before further image work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images sent to cloud editing providers leave the local machine and may contain sensitive content.

Mitigation: Use only approved providers and avoid uploading sensitive or regulated images unless provider settings and policies permit it.

Risk: Removing ownership, legal, safety, or brand-identifying marks can mislead viewers or violate others' rights.

Mitigation: Edit only images you own or are authorized to modify; do not remove marks to misrepresent ownership, products, or compliance.

Risk: Reconstructed content may alter perspective, textures, or obscured product details.

Mitigation: Review the output against the original and use pixel-preserving editing tools when exact fidelity matters.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Provider CLI guide](references/provider-cli.md)
- [Image model flags](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Following the commands may produce edited image files; reconstructed areas are inferred, not pixel-exact restorations.]

## Skill Version(s):

1.0.22 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
