## Description:

Check marketplace product trust, compare listings, and find better-evidenced alternatives — triggers on Amazon, Walmart, Target, Best Buy products, review authenticity, "should I trust/buy" questions, or finding stronger alternatives; returns GoBuy Evidence Scores (0-100) across 30,000+ scored products, powered by the Agentic Commerce Console.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

External shopping agents and their users use this skill to check marketplace listing evidence, compare product evidence quality, and identify stronger-evidenced alternatives before purchase guidance is given.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GoBuy Evidence Scores may be mistaken for product quality, product safety, or purchase advice.

Mitigation: State that the score measures evidence quality only, quote the verdict label and computed date, and independently verify important or expensive purchases.

Risk: Evidence-ranked alternatives may be interpreted as product recommendations.

Mitigation: Describe alternatives as products with stronger evidence, not recommended products, and avoid claims that a product is good or bad.

Risk: A product may be unavailable in the index or have incomplete marketplace signals.

Mitigation: When the skill reports not_indexed or missing signals, say so directly and do not guess beyond the available evidence.

## Reference(s):

- [Product evidence report](https://audit.gobuy.ai)
- [Free storefront audit](https://agentic.gobuy.ai)
- [Agentic Commerce Console](https://gobuy.ai/ao-console/sign-up)
- [ClawHub skill page](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown]

**Output Format:** [Markdown text with evidence scores, verdict labels, signal summaries, freshness, comparisons, and stronger-evidenced alternatives]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should treat scores as evidence-quality signals, not product quality, product safety, or purchase recommendations.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
