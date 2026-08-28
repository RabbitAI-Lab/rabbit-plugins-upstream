## Description:

PC Build Assistant helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact, or ITX builds using China-market CNY reference data and optional user overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill for desktop PC part selection, upgrade planning, compatibility review, price-aware build lists, gaming FPS lookup, and local model hardware sizing. It is not intended for laptops, server procurement, ordering or payment, remote control, security isolation, or standalone software, game, or agent tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled or searched prices may be stale, incomplete, or different from purchase-time market prices.

Mitigation: Treat quoted prices as references and verify current seller prices before purchase.

Risk: User overlay or catalog files may contain hardware inventory and pricing data the user does not intend to share with an agent.

Mitigation: Only provide overlay files containing hardware and pricing information that is acceptable to share with the agent.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility checks](references/compatibility.md)
- [English usage](references/english-usage.md)
- [Game FPS reference](references/game-performance.md)
- [Hardware scope](references/hardware-scope.md)
- [Local model hardware fit](references/local-model-fit.md)
- [Pricing rules](references/pricing.md)
- [Selection policy](references/selection-policy.md)
- [User catalog overlays](references/user-catalog.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with build lists, compatibility notes, price references, and verification points]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CNY price references, budget differences, component rows, compatibility conclusions, and purchase-time review notes.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
