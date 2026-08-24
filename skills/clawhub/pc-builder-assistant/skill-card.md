## Description:

PC Build Assistant helps agents plan budget desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator configurations using bundled China-market CNY references and user-supplied local overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to assemble or review desktop PC parts lists, upgrades, compatibility findings, China-market price references, game FPS samples, and local LLM hardware sizing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recommendations rely on bundled China-market reference data unless the user supplies local prices.

Mitigation: Use local price overlays or current public market checks before purchasing, and keep currencies separate.

Risk: Live price or model checks may involve normal web lookups to verify current public information.

Mitigation: Limit lookup inputs to hardware or model facts needed for the recommendation and avoid sharing sensitive purchasing or account details.

Risk: PC part specifications, prices, and compatibility details can change after bundled data is released.

Mitigation: Verify final part prices, SKU details, case clearances, power connectors, and motherboard support before ordering.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Scenarios](references/scenarios.md)
- [Hardware Scope](references/hardware-scope.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Game Performance](references/game-performance.md)
- [Price History](references/price-history.md)
- [Local Model Fit](references/local-model-fit.md)
- [User Catalog](references/user-catalog.md)
- [English Usage](references/english-usage.md)
- [User Overlay Schema](references/user-overlay.schema.json)
- [Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with parts lists, compatibility notes, price references, and verification caveats.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CNY price references, compatibility findings, game FPS samples, local LLM sizing estimates, and user-supplied local price overlays without currency mixing.]

## Skill Version(s):

0.1.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
