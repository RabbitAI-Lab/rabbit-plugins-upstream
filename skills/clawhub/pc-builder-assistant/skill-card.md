## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, local LLM hardware sizing, and gaming or creator configurations using China-market CNY reference prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to recommend or review desktop PC component lists, budget allocation, upgrades, and compatibility for gaming, creator, streaming, aesthetic, compact, ITX, and local AI builds. It is not intended for laptops, server procurement, purchasing or payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hardware purchase guidance can be affected by market-specific prices, availability, exact SKU differences, warranty terms, and changing official specifications.

Mitigation: Verify final prices, availability, exact SKUs, warranty terms, and compatibility before buying.

Risk: User overlay or catalog paths may cause the skill to read or write local files selected by the agent or user.

Mitigation: Only pass overlay or catalog file paths that are intended for the skill to access.

## Reference(s):

- [PC Build Assistant Skill Page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Scenarios](references/scenarios.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [Price History](references/price-history.md)
- [User Catalog Overlay](references/user-catalog.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [English Usage](references/english-usage.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with structured component lists, compatibility findings, price notes, and verification items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CNY price references, compatibility conclusions, trade-off notes, and pre-purchase verification points.]

## Skill Version(s):

0.1.23 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
