## Description:

Guides shoppers through evidence-led product comparisons, source and manufacturer checks, price and risk calculations, and clear recommendations for high-value or safety-critical purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT-0

## Use Case:

External shoppers use the skill to evaluate major or safety-critical purchases, compare candidates using public evidence and prices, and understand the tradeoffs behind a recommendation.

### Deployment Geography for Use:

China (mainland focus)

## Known Risks and Mitigations:

Risk: The optional update check uses an unpinned installer, and its scope is unclear.

Mitigation: Review the source and version before allowing the check to run; skip it if you cannot verify it.

Risk: Potential calculation or evidence-classification inconsistencies could affect purchase advice.

Mitigation: Verify cited prices, standards, and calculations against current primary sources before relying on a recommendation.

Risk: The security review was partial and had medium confidence, with some referenced paths missing.

Mitigation: Treat the review as incomplete and confirm the relevant source material and behavior before deployment.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zhashushu/skills/bilei-team)
- [Source review guide](artifact/references/agent1_blacklist.md)
- [Quantitative comparison guide](artifact/references/agent2_quant.md)
- [Verdict guide](artifact/references/agent3_verdict.md)
- [Price research guide](artifact/references/agent4_price_intel.md)
- [Manufacturer audit guide](artifact/references/manufacturer-audit.md)
- [Report and shareable output template](artifact/references/output_template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Chinese Markdown report with comparisons, evidence notes, and a shareable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides a primary recommendation report and a simplified shareable Markdown version; conclusions depend on available evidence and may identify unverified facts.]

## Skill Version(s):

1.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
