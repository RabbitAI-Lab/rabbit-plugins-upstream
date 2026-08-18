## Description:

PC Build Assistant helps agents plan desktop PC builds and upgrades, check compatibility, size local AI hardware, and provide gaming or creator hardware guidance with China-market CNY price references and user-supplied overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide desktop PC build planning, upgrade decisions, configuration completion, compatibility review, and local AI or gaming hardware sizing. It is not intended for laptop selection, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global, with bundled market data focused on China-market CNY pricing.

## Known Risks and Mitigations:

Risk: Bundled prices or online price checks may not match final checkout price, stock, warranty terms, or exact SKU variants.

Mitigation: Verify exact SKUs, seller terms, stock, warranty, and final prices with the purchase channel before buying.

Risk: Compatibility conclusions can depend on physical dimensions, connectors, BIOS support, QVL details, regional variants, and user-supplied overlay accuracy.

Mitigation: Review the skill's compatibility findings and confirm purchase-time details for dimensions, power cabling, firmware support, display outputs, and variant-specific specifications.

Risk: The skill may use host-agent web access when bundled price or model evidence is stale or incomplete.

Mitigation: Keep web checks scoped to the requested hardware evidence and treat the result as buying guidance, not as ordering, payment, or remote-control authority.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility Checks](references/compatibility.md)
- [Pricing Rules](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text responses with parts lists, prices, compatibility findings, trade-offs, and verification notes; bundled helper scripts may return JSON diagnostics for agent use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled catalog data and explicit user overlays; current prices or unrecorded model details may require scoped web checks by the host agent.]

## Skill Version(s):

0.1.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
