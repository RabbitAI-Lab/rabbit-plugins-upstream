## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, gaming performance estimates, and local LLM GPU/VRAM/RAM sizing using bundled China-market component references and optional current lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for budget desktop PC part lists, upgrade paths, configuration completion, compatibility review, hardware explanations, gaming FPS references, and local LLM hardware sizing. It is scoped to desktop PC hardware guidance and excludes laptops, server procurement, ordering, payment, remote control, security isolation, and standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hardware prices, stock, and regional availability can change after the bundled catalog date.

Mitigation: Verify current prices before buying and use current market lookups when offline prices are missing, stale, or explicitly challenged.

Risk: Compatibility conclusions can be incomplete when product dimensions, motherboard outputs, power connectors, cooling support, or case clearances are missing.

Mitigation: Run the bundled strict compatibility checks for concrete builds and surface unresolved review items as purchase-time checks instead of presenting them as fully verified.

Risk: The skill may read bundled catalog/reference files, run included Python scripts, and perform task-related market or official-source lookups.

Mitigation: Deploy only in environments where those local reads, script executions, and lookups are acceptable; the skill should not be granted ordering, payment, or remote-control authority.

## Reference(s):

- [Skill Page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Demand Routing](artifact/references/routing.md)
- [Selection Policy](artifact/references/selection-policy.md)
- [Compatibility Checks](artifact/references/compatibility.md)
- [Pricing Rules](artifact/references/pricing.md)
- [Workflows](artifact/references/workflows.md)
- [User Catalog Overlay](artifact/references/user-catalog.md)
- [Hardware Scope](artifact/references/hardware-scope.md)
- [Hardware FAQ](artifact/references/hardware-faq.md)
- [Game Performance](artifact/references/game-performance.md)
- [Price History](artifact/references/price-history.md)
- [Local Model Fit](artifact/references/local-model-fit.md)
- [English Usage](artifact/references/english-usage.md)
- [User Overlay Schema](artifact/references/user-overlay.schema.json)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured part lists, compatibility findings, price notes, and occasional command-backed analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite bundled catalog data, price reference dates, compatibility review items, and local model-fit assumptions.]

## Skill Version(s):

0.1.28 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
