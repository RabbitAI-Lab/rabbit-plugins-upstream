## Description:

PC Build Assistant supports desktop PC build planning, upgrades, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact, or ITX build recommendations using bundled China-market CNY price references and explicit user overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill to plan desktop PC builds, compare parts and prices, complete or review configurations, size local LLM hardware, and produce component recommendations with compatibility caveats.

### Deployment Geography for Use:

Global; bundled price references are China-market CNY unless the user provides explicit local overlays.

## Known Risks and Mitigations:

Risk: User-provided overlay files may include private or unrelated data.

Mitigation: Provide only the hardware and quote data intended for the assistant to use.

Risk: Bundled prices can become stale or may not represent a user's local market.

Mitigation: Verify current market prices before purchase, especially when local prices are stale, insufficient, or outside the bundled China-market CNY references.

## Reference(s):

- [PC Build Assistant ClawHub Page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [User Catalog Overlay](references/user-catalog.md)
- [English Usage](references/english-usage.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown prose with component tables, price summaries, compatibility findings, trade-offs, and verification items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may be in English or Chinese and may include CNY price dates, budget deltas, local overlay notes, local LLM fit estimates, and gaming FPS references when supported by bundled evidence.]

## Skill Version(s):

0.1.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
