## Description:

PC Build Assistant helps agents plan China-market desktop PC builds, upgrades, compatibility checks, hardware guidance, gaming performance references, and local LLM GPU/VRAM/RAM sizing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and PC builders use this skill to get desktop part lists, upgrade paths, compatibility checks, price-aware recommendations, game FPS references, and local LLM hardware capacity guidance. It is scoped to desktop PC hardware advice, with bundled China-market CNY prices as references rather than purchase guarantees.

### Deployment Geography for Use:

Global use with China-market pricing scope

## Known Risks and Mitigations:

Risk: China-market prices, FPS figures, and hardware availability can change quickly or vary by exact SKU and retailer.

Mitigation: Treat catalog values as references and verify current retailer listings, exact model identifiers, and price dates before buying.

Risk: Compatibility conclusions can be incomplete when vendor dimensions, power connectors, display outputs, cooler mounts, or case clearance fields are missing.

Mitigation: Prefer candidates with complete evidence, run the packaged compatibility checks for final lists, and surface unresolved pre-purchase review items to the user.

Risk: Local LLM fit estimates describe capacity assumptions and do not guarantee throughput, latency, long-context behavior, or training performance.

Mitigation: State quantization, context, concurrency, VRAM, and RAM assumptions, and verify model configuration when a specific model is outside the bundled samples.

## Reference(s):

- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [Price history](references/price-history.md)
- [User catalog overlays](references/user-catalog.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or plain text with tables for concrete part lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include component prices, total cost, compatibility conclusions, tradeoffs, pre-purchase review points, price reference dates, FPS references, or local LLM capacity assumptions.]

## Skill Version(s):

0.1.40 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
