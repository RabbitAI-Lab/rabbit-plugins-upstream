## Description:

Helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact, or ITX desktop builds using packaged China-market CNY reference data and explicit user overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent users use this skill to produce desktop PC part recommendations, upgrade plans, compatibility summaries, price-aware build reports, local LLM hardware fit guidance, and game performance guidance. It is intended for desktop PC planning and hardware advice, not laptops, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global, with packaged pricing primarily focused on China-market CNY references.

## Known Risks and Mitigations:

Risk: Packaged prices and market data may be stale, unavailable, or specific to China-market CNY references.

Mitigation: Verify current local availability, exact SKU, warranty, and final checkout price before buying.

Risk: Compatibility conclusions depend on catalog completeness and may leave specific fields for purchase-time review.

Mitigation: Review any listed compatibility gaps, especially case clearance, motherboard outputs, power connectors, cooling fit, and vendor SKU details, before purchasing.

Risk: Public web lookups may be used when prices are stale, missing, or explicitly requested.

Mitigation: Treat web-derived prices and model facts as supporting evidence and confirm them against retailer or vendor pages before making a purchase decision.

## Reference(s):

- [Compatibility Checks](references/compatibility.md)
- [English Usage](references/english-usage.md)
- [Game Performance Reference](references/game-performance.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Price History](references/price-history.md)
- [Pricing Rules](references/pricing.md)
- [Routing](references/routing.md)
- [Scenarios](references/scenarios.md)
- [Selection Policy](references/selection-policy.md)
- [User Catalog Overlay](references/user-catalog.md)
- [Workflows](references/workflows.md)
- [Transformers Quantization Documentation](https://huggingface.co/docs/transformers/main/en/quantization)
- [Transformers KV Cache Documentation](https://huggingface.co/docs/transformers/kv_cache)
- [Accelerate Big Model Inference Documentation](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B Model Card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B Model Card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B Model Card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct Model Card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral Small 3.1 24B Instruct Model Card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek R1 Distill Qwen 32B Model Card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with desktop PC part lists, reference prices, totals, compatibility summaries, tradeoff notes, and purchase-review points.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses packaged hardware catalogs, compatibility scripts, game FPS samples, local model fit data, price references, and user-provided overlays where available.]

## Skill Version(s):

0.1.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
