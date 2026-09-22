## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator scenarios using China-market CNY reference data and explicit user overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to produce desktop parts recommendations, upgrade plans, compatibility reviews, pricing notes, FPS and local-model-fit estimates, and hardware Q&A for desktop PC builds. It is scoped away from laptops, server procurement, ordering or payment, remote control, security isolation, and standalone software tutorials.

### Deployment Geography for Use:

Global, with built-in pricing focused on China-market CNY references.

## Known Risks and Mitigations:

Risk: Bundled component prices are China-market CNY references and may become stale or differ from current buying conditions.

Mitigation: Verify current prices before purchase, preserve visible price dates, and use explicit user overlays for local prices without mixing currencies.

Risk: Compatibility and build-fit conclusions depend on the completeness of catalog fields and user-provided model details.

Mitigation: Run the bundled strict compatibility checks for complete builds and surface missing fields, physical clearances, cable requirements, and other pre-purchase review items.

Risk: FPS prediction-labeled samples and local-model-fit estimates are planning aids, not measured benchmark proof or speed guarantees.

Mitigation: Present these outputs as estimates, cite only collected samples or model configuration evidence, and avoid promising exact frame rates, long-context behavior, or inference throughput.

Risk: User overlay files can change recommendations and pricing results.

Mitigation: Keep overlay files under the installer's control and treat user-supplied catalog data as scoped input for the current recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility rules](artifact/references/compatibility.md)
- [Pricing rules](artifact/references/pricing.md)
- [Selection policy](artifact/references/selection-policy.md)
- [Workflows](artifact/references/workflows.md)
- [Local model fit](artifact/references/local-model-fit.md)
- [User overlay schema](artifact/references/user-overlay.schema.json)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B model card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B model card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct model card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral-Small-3.1-24B-Instruct-2503 model card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek-R1-Distill-Qwen-32B model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with structured parts lists, pricing notes, compatibility findings, and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled Python scripts and offline data to support recommendations; no persistent credentials, hidden persistence, or destructive behavior were reported by the authoritative security evidence.]

## Skill Version(s):

0.1.39 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
