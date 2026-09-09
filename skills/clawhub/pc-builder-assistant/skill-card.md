## Description:

Helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM hardware sizing, and gaming or creator configurations using bundled China-market component data and scoped helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to produce desktop PC part recommendations, upgrade plans, budget tradeoffs, compatibility findings, and local model hardware-fit guidance. It is intended for normal ClawHub skill use, not for laptop advice, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hardware recommendations can become inaccurate when bundled China-market prices are stale or unavailable.

Mitigation: Use the skill's stated price freshness workflow, verify current market prices before purchase, and exclude items without sourced prices from totals.

Risk: Compatibility conclusions may be incomplete when component fields such as GPU length, power connectors, motherboard display outputs, or cooler clearance are missing.

Mitigation: Require explicit compatibility checks for final builds and surface unresolved review items as purchase-time verification points.

Risk: User-supplied overlay files can alter component and price data used for recommendations.

Mitigation: Treat overlays as explicit user input, keep currencies separate, and review overlay contents before relying on them.

Risk: Optional network search for pricing freshness can expose queries to external services.

Mitigation: Use bundled offline data first and perform network price checks only when freshness, missing data, or the user's request requires it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Selection policy](references/selection-policy.md)
- [Workflows](references/workflows.md)
- [User catalog overlay](references/user-catalog.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with structured part lists, prices, compatibility notes, and verification points when applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated shell commands for bundled helper scripts and may cite price reference dates for selected hardware.]

## Skill Version(s):

0.1.29 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
