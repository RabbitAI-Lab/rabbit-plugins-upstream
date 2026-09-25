## Description:

Checks marketplace listing evidence, compares products, and identifies stronger-evidenced alternatives across Amazon, Walmart, and Target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping agents and their users check evidence behind Amazon, Walmart, and Target listings, compare evidence quality, and find stronger-evidenced alternatives when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad shopping prompts may trigger a product evidence check when a buyer expects a recommendation.

Mitigation: Present the result as marketplace evidence, not a purchase recommendation, and confirm the buyer's intended question.

Risk: Evidence Scores can be mistaken for product quality or safety ratings.

Mitigation: Include the verdict and computed date, identify missing signals, and verify current product details before buying.

## Reference(s):

- [GoBuy product evidence reports](https://audit.gobuy.ai)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence Score (0–100), verdict, computed date, observed and missing signals; comparisons and evidence-ranked alternatives only when eligible.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
