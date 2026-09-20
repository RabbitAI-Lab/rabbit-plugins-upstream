## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator configurations using bundled China-market CNY catalog data and local helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to prepare desktop PC part lists, compare upgrade paths, check compatibility, estimate local LLM hardware fit, and summarize gaming or creator trade-offs before purchase decisions. It is not intended for laptops, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled prices and availability may not match the current retail market.

Mitigation: Verify current retailer pricing, stock, and final part availability before purchase.

Risk: FPS estimates and compatibility caveats may be incomplete planning aids rather than purchase-grade guarantees.

Mitigation: Confirm game performance expectations, manufacturer specifications, and fit constraints before ordering hardware.

Risk: China-market CNY references may not apply directly to other markets or currencies.

Mitigation: Keep user-provided local prices separate from bundled CNY references and avoid unsupported currency mixing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [User Catalog](references/user-catalog.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text recommendations with component rows, prices, compatibility conclusions, trade-offs, and verification caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled catalog data and local script results; user-facing outputs should keep price dates, market scope, and manual verification caveats visible.]

## Skill Version(s):

0.1.38 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
