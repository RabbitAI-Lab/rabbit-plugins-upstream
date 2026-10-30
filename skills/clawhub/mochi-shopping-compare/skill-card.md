## Description:

Compare product specifications, prices and usage costs, separating confirmed facts from missing information. Use for 购物比较助手.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External shoppers use this skill to compare products against intended use, budget, region, required specifications, and known purchase or usage costs while keeping confirmed facts distinct from missing information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Comparison records, source excerpts, and product URLs are saved locally in plaintext.

Mitigation: Use an appropriately access-controlled workspace and review saved information before sharing it.

Risk: A product comparison could be mistaken for authorization to purchase.

Mitigation: Treat comparisons as decision support; purchasing requires a separate user instruction.

## Reference(s):

- [ClawHub release](https://clawhub.ai/hznetnewpower/skills/mochi-shopping-compare)
- [MochiLab homepage](https://mochilab.bz)
- [Input contract](references/input.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown product comparisons and structured JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates confirmed facts from missing information; includes sources and observation dates, like-for-like quantities, currency-specific price and unit-cost comparisons, and stated usage assumptions.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
