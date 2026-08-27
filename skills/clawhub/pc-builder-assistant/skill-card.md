## Description:

PC Build Assistant helps agents plan budget desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM hardware sizing, and gaming or creator configurations using bundled China-market CNY references and explicit user overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to assemble or review desktop PC part lists, compare budget trade-offs, verify compatibility, and explain hardware choices for China-market builds and user-supplied local overlays.

### Deployment Geography for Use:

Global, with bundled price references focused on the China market.

## Known Risks and Mitigations:

Risk: Hardware prices, stock, warranty terms, and local availability can differ from bundled China-market CNY references or change after the recorded price date.

Mitigation: Verify exact SKUs, current checkout prices, stock, warranty, and retailer terms before purchasing; keep non-CNY user overlay prices separate from CNY references.

Risk: Compatibility conclusions can be incomplete when catalog fields are missing or when a user supplies partial part information.

Mitigation: Use the bundled compatibility workflow for complete builds and surface concrete pre-purchase checks such as clearance, power connectors, motherboard outputs, QVL, and storage slot sharing.

Risk: Refreshing prices or model configuration details may require web searches or fixed online sources when local data is insufficient.

Mitigation: Avoid private retailer accounts and credentials; provide explicit local overlay files only for prices or parts the user wants considered.

## Reference(s):

- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Scenarios](references/scenarios.md)
- [Hardware Scope](references/hardware-scope.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Game Performance](references/game-performance.md)
- [Local Model Fit](references/local-model-fit.md)
- [Price History](references/price-history.md)
- [User Catalog Overlay](references/user-catalog.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [English Usage](references/english-usage.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown recommendations and concise text guidance, with structured part-list details when specific models are selected]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prices, price dates, budget deltas, compatibility findings, trade-offs, and pre-purchase verification items.]

## Skill Version(s):

0.1.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
