## Description:

PC Build Assistant helps agents plan China-market desktop PC builds, upgrades, compatibility checks, hardware guidance, gaming and creator recommendations, and local LLM GPU/VRAM/RAM sizing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and external users use this skill to help agents produce budget-aware desktop PC build recommendations, upgrade plans, configuration completion, compatibility reviews, hardware explanations, game-performance references, and local LLM hardware-sizing guidance. The bundled catalog focuses on China-market CNY prices and keeps explicit user price overlays separate by currency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External price, hardware, model, Hugging Face, and GitHub lookups may be needed when bundled data is stale or incomplete.

Mitigation: Use bundled dated catalog data first, perform external lookups only for stale or missing evidence, and state price dates or verification gaps before purchase decisions.

Risk: Compatibility conclusions can be incomplete when catalog fields are missing or a user supplies partial hardware information.

Mitigation: Run strict compatibility checks for complete builds and surface unresolved review items instead of presenting an incomplete result as fully verified.

Risk: Local LLM sizing estimates can be mistaken for speed, throughput, or long-context guarantees.

Mitigation: State quantization, context, VRAM/RAM, and offload assumptions, and avoid promising performance beyond the estimator and official model evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [User Catalog Overlay](references/user-catalog.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text with structured component rows, compatibility summaries, price notes, and concise trade-off guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses China-market CNY catalog data by default; user-supplied price overlays keep currencies separate.]

## Skill Version(s):

0.1.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
