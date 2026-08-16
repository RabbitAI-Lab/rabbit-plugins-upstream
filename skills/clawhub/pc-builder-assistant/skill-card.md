## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, gaming and creator configurations, and local LLM GPU, VRAM, and RAM sizing using bundled China-market CNY references and user-provided overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent recommend desktop PC parts lists, complete or review configurations, check compatibility, compare budget tradeoffs, and estimate local LLM hardware fit. It is scoped to desktop PC planning and excludes laptops, server procurement, purchases, remote control, security isolation, and standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use online sources when market-price freshness matters, so pricing guidance can vary by time and source quality.

Mitigation: Review current prices before purchase decisions and treat the skill's prices as planning references rather than purchase commitments.

Risk: Hardware recommendations and compatibility conclusions can be incomplete when catalog fields or user-provided part details are missing.

Mitigation: Review listed compatibility verification points before ordering or deploying a final build.

## Reference(s):

- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [User Catalog](references/user-catalog.md)
- [Hardware Scope](references/hardware-scope.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [Price History](references/price-history.md)
- [English Usage](references/english-usage.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown recommendations with structured parts lists, compatibility notes, pricing references, and tradeoff explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include China-market CNY reference prices, user-provided overlay prices, compatibility review points, and local LLM fit estimates.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
