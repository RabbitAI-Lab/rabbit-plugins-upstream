## Description:

Checks ecommerce product images against marketplace listing requirements and can save geometry- and color-level repairs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers and ecommerce operators use the skill to check product images against platform-specific listing criteria, review pass-or-rejection risks, and optionally save repaired copies. It is intended for image compliance checks, not as a guarantee of marketplace approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pixel-based checks cannot reliably judge text, watermarks, collages, or whether a product image is visually malformed, and passing checks does not guarantee marketplace approval.

Mitigation: Treat the report as a screening aid, review images visually or with a suitable visual check, and confirm the target marketplace's current requirements before listing.

Risk: Automatic repairs can change framing or color and may not preserve the intended appearance.

Mitigation: Save repaired copies to a separate output directory and compare each result with its original before use.

Risk: Optional cloud image-generation helpers may upload supplied images to a provider and incur charges.

Mitigation: Use the local checker when generation is unnecessary; before using a generation helper, explicitly select a provider and confirm image-sharing and cost expectations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/platform-compliance)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Image files, Shell commands]

**Output Format:** [Text or JSON compliance reports, plus optionally repaired image files saved separately from the originals.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can process multiple images; automated pixel checks do not assess every visual or marketplace-policy requirement.]

## Skill Version(s):

1.0.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
