## Description:

Use for budget desktop PC build planning and recommendations, PC hardware DIY, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact or ITX builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, gaming and creator systems, and local LLM GPU/VRAM/RAM sizing. It is scoped to desktop PC hardware guidance and uses bundled China-market CNY references with optional user-supplied local catalog overlays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled prices are China-market CNY references and may be stale for a user's purchase context.

Mitigation: Verify current local prices and availability before relying on totals or purchase decisions.

Risk: The skill may browse or contact fixed public sources when prices are stale, real-time pricing is requested, or model configuration must be verified.

Mitigation: Use it in an environment where those lookups are expected, and avoid including sensitive information in lookup prompts.

Risk: User-supplied overlay files can affect hardware and pricing calculations.

Mitigation: Provide private overlay files only when you intend the agent to use their contents for recommendations.

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
- [Scenarios](references/scenarios.md)
- [Selection Policy](references/selection-policy.md)
- [User Catalog Overlay](references/user-catalog.md)
- [Workflows](references/workflows.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B Model Card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B Model Card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B Model Card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct Model Card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral-Small-3.1-24B-Instruct-2503 Model Card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek-R1-Distill-Qwen-32B Model Card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured PC parts lists, compatibility findings, pricing notes, and concise hardware guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled local catalogs and helper scripts, and may browse fixed public sources when price or model evidence is stale or explicitly requested.]

## Skill Version(s):

0.1.26 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
