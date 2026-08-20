## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator configurations using bundled China-market CNY references and user-provided overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill to ask an agent for desktop PC build recommendations, upgrade planning, configuration completion, compatibility review, hardware explanations, game performance references, and local LLM hardware sizing. The skill is scoped to desktop PC hardware and China-market CNY reference pricing unless the user provides explicit local-price overlays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled and web-sourced hardware prices can be stale, incomplete, or different from retailer checkout terms.

Mitigation: Treat prices as references and verify retailer listings, stock, final price, warranty terms, and exchange rates before buying.

Risk: User-provided overlay files can materially change recommendations and totals.

Mitigation: Provide only hardware or quote data that the agent should use, keep currencies separate, and review generated build totals before acting on them.

Risk: Hardware compatibility and local model fit outputs are planning aids rather than purchase guarantees.

Mitigation: Review the skill's compatibility findings and unresolved verification items against official product specifications before ordering parts.

## Reference(s):

- [Compatibility Checks](references/compatibility.md)
- [English Usage](references/english-usage.md)
- [Game Performance Reference](references/game-performance.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Price History](references/price-history.md)
- [Pricing Rules](references/pricing.md)
- [Request Routing](references/routing.md)
- [Scenario Rules](references/scenarios.md)
- [Selection Policy](references/selection-policy.md)
- [User Catalog Overlay](references/user-catalog.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [Workflows](references/workflows.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B Model Card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B Model Card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B Model Card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct Model Card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral Small 3.1 24B Instruct Model Card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek R1 Distill Qwen 32B Model Card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured build lists, compatibility findings, pricing notes, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CNY reference prices, price dates, budget deltas, compatibility review items, game FPS references, and local model sizing caveats.]

## Skill Version(s):

0.1.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
