## Description:

Recomputes true gross profit and margin per SKU, flags miscomputed or abnormally low-margin rows, and checks totals, duplicate rows, blanks, and negative values with source line citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, cross-border operators, and finance teams use this skill during monthly close to recalculate SKU-level profit from exported tables and identify rows whose margin math or required fields need review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation contains unused anonymous-statistics and --no-stats wording that may confuse users about whether table contents leave the machine.

Mitigation: Confirm the current behavior during review and remove or correct the stale wording before publication.

Risk: The skill calculates profit only from the fields supplied in the input table and does not cover taxes, warehousing, payment fees, labor, or accounting policy decisions.

Mitigation: Treat the output as a SKU table check, then reconcile it with the user's full accounting model before making financial decisions.

Risk: Release license evidence conflicts with the artifact frontmatter.

Mitigation: Verify whether MIT-0 or Proprietary is the authoritative license for this release before rendering the public card.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/sku-profit-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, analysis, shell commands, guidance]

**Output Format:** [Console text or JSON results with per-row findings and source line citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local SKU profit table input; insufficient input returns missing-field guidance instead of a conclusion.]

## Skill Version(s):

1.0.37 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
