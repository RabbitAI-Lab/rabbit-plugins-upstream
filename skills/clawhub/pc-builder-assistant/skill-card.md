## Description:

Helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, and hardware guidance for gaming, creator, streaming, local LLM, aesthetic, compact, and ITX use cases, using China-market CNY references and explicit user-provided price overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill to get desktop PC part recommendations, upgrade advice, compatibility reviews, local LLM GPU/VRAM/RAM sizing, and gaming-performance guidance for China-market builds or explicit user-provided price overlays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled catalog prices, stock status, warranty terms, and exact SKUs may differ from current local market conditions.

Mitigation: Verify current local prices, stock, warranty, and exact SKU details before buying or presenting a final purchase recommendation.

Risk: Some game FPS rows are prediction-based rather than measured benchmarks.

Mitigation: Treat FPS output as guidance, label uncertainty when applicable, and avoid presenting unmeasured values as guaranteed performance.

Risk: Server, NAS, workstation, compact, and ITX case recommendations can depend on physical clearance and layout details that may be incomplete.

Mitigation: Require explicit pre-purchase checks for clearance, power, cooling, cable, fan, and expansion constraints when the available evidence is incomplete.

## Reference(s):

- [PC Build Assistant skill definition](SKILL.md)
- [Demand routing](references/routing.md)
- [Component selection policy](references/selection-policy.md)
- [Pricing rules](references/pricing.md)
- [Compatibility checks](references/compatibility.md)
- [Workflows](references/workflows.md)
- [Hardware scope](references/hardware-scope.md)
- [Scenario guidance](references/scenarios.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Local model fit guidance](references/local-model-fit.md)
- [Game performance guidance](references/game-performance.md)
- [Price history guidance](references/price-history.md)
- [User catalog overlay guidance](references/user-catalog.md)
- [English usage guidance](references/english-usage.md)
- [User overlay schema](references/user-overlay.schema.json)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B model card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B model card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct model card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral-Small-3.1-24B-Instruct-2503 model card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek-R1-Distill-Qwen-32B model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown prose and tables with structured part lists, prices, compatibility findings, trade-offs, and verification notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CNY by default, keeps explicit user overlay currencies separate, and avoids unsourced models, prices, frame rates, or compatibility claims.]

## Skill Version(s):

0.1.32 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
