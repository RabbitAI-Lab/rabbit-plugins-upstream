## Description:

Decode laundry care symbols from text descriptions (tub, triangle, iron, circle, square shapes with dots/bars), build a safe wash plan for a mixed load (color bleeding risk, temperature ceilings, fabric conflicts), and give evidence-based stain removal protocols by stain type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to interpret laundry care labels, divide garments into safe wash loads, and choose fabric-aware stain-removal steps before washing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Laundry and stain-removal advice may be unsuitable for expensive, delicate, unusual, or professionally structured garments.

Mitigation: Verify the garment label first and consult a professional cleaner when the garment is high-value, unusual, or outside the skill's stated scope.

Risk: Applying stain, bleach, heat, or solvent guidance to the wrong fabric can damage fibers or set stains.

Mitigation: Use the fabric-specific protocol, test chemicals on a hidden seam, avoid heat on protein stains, and do not use this skill for leather, suede, or dry-cleaning chemical handling.

## Reference(s):

- [Laundry Science & Practice Reference](references/care-and-stains.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/laundry-decoder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text or Markdown with optional JSON from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline, stdlib-only Python helper; no network or credential requirements were reported in security evidence.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
