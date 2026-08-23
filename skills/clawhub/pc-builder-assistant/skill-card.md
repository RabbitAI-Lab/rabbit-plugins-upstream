## Description:

Helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM hardware sizing, and gaming, streaming, creator, aesthetic, compact, or ITX build recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to obtain desktop PC parts guidance, budget-aware build lists, upgrade advice, compatibility findings, pricing context, game-performance references, and local LLM GPU/VRAM/RAM sizing. Its bundled catalog is centered on China-market CNY references, while explicit user overlays keep local currencies separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PC build recommendations may reflect stale prices or incomplete compatibility evidence.

Mitigation: Review generated recommendations before purchasing, verify current prices, and check listed compatibility review items against the exact parts.

Risk: The skill can run bundled Python scripts and may look up public pricing or model information online when needed.

Mitigation: Review the skill before installation and provide only the local hardware overlays or files intended for the recommendation task.

## Reference(s):

- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Hardware Scope](references/hardware-scope.md)
- [Workflows](references/workflows.md)
- [Scenarios](references/scenarios.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [Price History](references/price-history.md)
- [User Catalog](references/user-catalog.md)
- [English Usage](references/english-usage.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with structured parts lists, compatibility summaries, verification notes, and occasional JSON overlay drafts or shell commands when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled data and helper scripts for catalog queries, compatibility checks, price history, game FPS samples, and local model-fit estimates.]

## Skill Version(s):

0.1.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
