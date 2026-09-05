## Description:

PC Build Assistant helps agents plan desktop PC builds and upgrades, check hardware compatibility, estimate China-market prices, and size systems for gaming, creator, streaming, compact/ITX, aesthetic, and local LLM use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users, developers, and PC builders use this skill to produce desktop build recommendations, upgrade plans, compatibility reviews, and hardware guidance. It is especially suited to China-market CNY price references, optional user-provided catalog overlays, and local LLM GPU/VRAM/RAM sizing.

### Deployment Geography for Use:

Global, with bundled pricing focused on China-market CNY references.

## Known Risks and Mitigations:

Risk: Bundled prices, market quotes, and component availability can be stale or vary by exact SKU.

Mitigation: Treat prices as references, check current market information when needed, and verify exact SKUs before buying.

Risk: Compatibility conclusions may depend on incomplete case, motherboard, power, cooling, or display-output evidence.

Mitigation: Use the skill's strict compatibility workflow and preserve any unresolved down-order verification items in the final recommendation.

Risk: User-provided overlay or catalog files may expose local hardware or pricing data to the agent.

Mitigation: Provide only overlay and catalog files that are intended for the skill to read.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Scenarios](references/scenarios.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [Price History](references/price-history.md)
- [User Catalog](references/user-catalog.md)
- [English Usage](references/english-usage.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B Model Card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B Model Card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B Model Card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct Model Card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral Small 3.1 24B Model Card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek R1 Distill Qwen 32B Model Card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance, Configuration]

**Output Format:** [Markdown text with priced part lists, compatibility notes, trade-off explanations, and verification items.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled hardware data and optional user-provided overlays; prices are references and exact SKUs should be verified before purchase.]

## Skill Version(s):

0.1.25 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
