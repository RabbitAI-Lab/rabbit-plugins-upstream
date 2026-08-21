## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator recommendations using bundled China-market CNY price references and optional user overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to produce desktop PC parts recommendations, upgrade plans, compatibility reviews, and local AI or gaming sizing guidance. It is most directly grounded in China-market CNY pricing, with explicit user overlays for other local prices.

### Deployment Geography for Use:

Global, with bundled pricing focused on China-market CNY references.

## Known Risks and Mitigations:

Risk: Bundled prices and optional lookup results may differ from live stock, warranty terms, or checkout prices.

Mitigation: Verify the exact SKU, seller, warranty, stock, and final checkout price before buying.

Risk: Hardware compatibility conclusions can remain incomplete when catalog fields or vendor specifications are missing.

Mitigation: Use the skill's compatibility checks and keep unresolved fit, connector, firmware, display-output, PCIe, USB4, Thunderbolt, and clearance items as pre-purchase verification points.

Risk: The skill runs local Python helper scripts and reads bundled or user-supplied catalog data.

Mitigation: Install from a trusted package, keep user overlays explicit, and review generated recommendations before acting on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [routing.md](references/routing.md)
- [selection-policy.md](references/selection-policy.md)
- [workflows.md](references/workflows.md)
- [compatibility.md](references/compatibility.md)
- [pricing.md](references/pricing.md)
- [hardware-scope.md](references/hardware-scope.md)
- [hardware-faq.md](references/hardware-faq.md)
- [local-model-fit.md](references/local-model-fit.md)
- [game-performance.md](references/game-performance.md)
- [price-history.md](references/price-history.md)
- [user-catalog.md](references/user-catalog.md)
- [English usage](references/english-usage.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral Small 3.1 24B Instruct](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text recommendations with parts lists, prices, compatibility notes, trade-offs, and pre-purchase checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CNY reference prices, price dates, budget deltas, compatibility conclusions, and verification items.]

## Skill Version(s):

0.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
