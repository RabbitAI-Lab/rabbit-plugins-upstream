## Description:

Helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator-oriented builds using bundled China-market CNY reference data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to get desktop PC parts recommendations, upgrade guidance, compatibility review, pricing context, gaming FPS estimates, and local LLM hardware-fit guidance. It is not intended for laptops, server procurement, ordering or payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled prices are China-market references and may not reflect the buyer's current local market.

Mitigation: Verify current prices before purchase, preserve the original CNY reference basis, and keep user-supplied local-currency overlays separate instead of converting or mixing currencies.

Risk: Compatibility, FPS, and local model-fit outputs rely on bundled data and estimates that may be incomplete for a specific SKU, game, model, or build.

Mitigation: Run the provided checks, surface unresolved review items, and avoid presenting estimates or skipped checks as fully verified facts.

Risk: Server or NAS chassis may appear in data even though the skill is not intended for server procurement.

Mitigation: Keep recommendations scoped to desktop PC builds and exclude server procurement use cases.

Risk: Optional user overlay files can change catalog and pricing behavior.

Mitigation: Treat overlays as user-supplied inputs, validate them against the bundled schema, and review any local file changes before relying on the resulting recommendations.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [Hardware scope](artifact/references/hardware-scope.md)
- [Selection policy](artifact/references/selection-policy.md)
- [Compatibility checks](artifact/references/compatibility.md)
- [Pricing rules](artifact/references/pricing.md)
- [Workflow modes](artifact/references/workflows.md)
- [Local model fit](artifact/references/local-model-fit.md)
- [Game performance](artifact/references/game-performance.md)
- [Price history](artifact/references/price-history.md)
- [User catalog overlay schema](artifact/references/user-overlay.schema.json)
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text recommendations with structured parts lists, prices, compatibility findings, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CNY reference prices, budget deltas, compatibility caveats, FPS estimates, local model-fit estimates, and pre-purchase checks.]

## Skill Version(s):

0.1.34 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
