## Description:

PC Build Assistant supports desktop PC build planning, upgrades, compatibility checks, hardware guidance, gaming and creator scenarios, and local LLM GPU/VRAM/RAM sizing with China-market component references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to plan budget desktop PC builds, complete or upgrade configurations, compare hardware options, and check compatibility before purchasing. It is not intended for laptop selection, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global; bundled component pricing defaults to China-market CNY references.

## Known Risks and Mitigations:

Risk: Market prices, stock, and exact SKUs may differ from bundled China-market references or limited network lookups.

Mitigation: Verify current prices, variant names, stock region, warranty terms, and exact SKUs with the seller before purchase.

Risk: A parts list can still have incomplete compatibility evidence for dimensions, power connectors, cooling clearance, display outputs, or case fan placement.

Mitigation: Use the bundled compatibility checks and review any remaining manual verification items before ordering components.

Risk: Local LLM hardware-fit guidance estimates capacity, not speed, latency, long-context reliability, or training suitability.

Mitigation: Treat model-fit output as planning guidance and validate specific model configuration, quantization, context length, and offload behavior for the target workload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Workflows](references/workflows.md)
- [Local model hardware fit](references/local-model-fit.md)
- [Game performance reference](references/game-performance.md)
- [User catalog overlay](references/user-catalog.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured component lists, prices, compatibility notes, verification items, and occasional inline shell commands for agent-side checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled local catalog and compatibility scripts; may use limited network lookups for current market prices, published version history, or official model configuration when needed.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
