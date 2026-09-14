## Description:

Uses Amazon product details and review evidence to diagnose buyer decision barriers and suggest conversion-focused listing copy improvements; it is not for conversion-rate prediction, ad bidding, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace operators, and supporting agents use this skill to inspect product-detail and customer-review signals, quote the paid ARI operation, and produce evidence-grounded recommendations for improving listing copy after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that the CLI can run paid ARI operation workflows beyond the fixed Amazon conversion workflow it advertises.

Mitigation: Review before installing, only approve paid runs when the quote is clearly for listing/conversion, and avoid supplying workflow or focus overrides.

Risk: The skill requires an ARI API key and submits product and review data to ARI/Funewa.

Mitigation: Install only if ARI/Funewa is trusted with the API key and submitted product and review data; keep credentials out of prompts and logs.

Risk: Recommendations can be misleading if review evidence is insufficient or if unavailable business data is treated as fact.

Mitigation: Base conclusions only on product-detail and review evidence, state data gaps, and do not infer real conversion rate, sales, inventory, advertising, orders, profit, or automatic publishing actions.

## Reference(s):

- [Amazon conversion-copy API reference](artifact/references/reference.md)
- [Amazon conversion-copy operation workflow](artifact/references/operation-workflow.md)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/conversion-copy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise findings, review evidence, conclusions, and inline bash commands when setup, quote, run, or status checks are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid analysis must be quoted first and run only after explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: evidence release, CHANGELOG.md, _meta.json, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
