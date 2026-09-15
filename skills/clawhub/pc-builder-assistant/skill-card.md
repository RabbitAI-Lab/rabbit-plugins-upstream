## Description:

PC Build Assistant helps agents produce China-market desktop PC build recommendations, upgrades, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator build advice while avoiding unsupported laptop, server, procurement, payment, remote-control, and security-isolation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill to plan budget desktop PCs, compare upgrades, complete partial configurations, check compatibility, and size GPU, VRAM, and RAM needs for gaming, streaming, creator, compact, ITX, and local AI workflows, primarily with China-market CNY catalog data.

### Deployment Geography for Use:

Global, with China-market CNY catalog assumptions.

## Known Risks and Mitigations:

Risk: Bundled prices and FPS figures are decision support rather than guaranteed retail quotes or measured benchmarks.

Mitigation: Verify exact local SKUs, warranty terms, stock, compatibility, benchmark relevance, and checkout prices before buying.

Risk: The skill is scoped to desktop PC planning and can give unsuitable guidance if used for laptops, server procurement, ordering, payment, remote control, or security isolation.

Mitigation: Keep usage within desktop PC build planning, upgrades, compatibility checks, and hardware guidance; redirect unsupported tasks to appropriate tools or experts.

Risk: Catalog entries or user-provided hardware details may lack enough fields for a complete compatibility conclusion.

Mitigation: Use the skill's compatibility workflow and preserve concrete down-before-buy review items when evidence is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Selection policy](references/selection-policy.md)
- [Workflow modes](references/workflows.md)
- [Hardware scope](references/hardware-scope.md)
- [Scenario rules](references/scenarios.md)
- [English usage](references/english-usage.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [Price history](references/price-history.md)
- [User hardware and quote overlay](references/user-catalog.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)
- [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B)
- [Qwen3-30B-A3B model card](https://huggingface.co/Qwen/Qwen3-30B-A3B)
- [Qwen3-32B model card](https://huggingface.co/Qwen/Qwen3-32B)
- [Qwen2.5-72B-Instruct model card](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)
- [Mistral Small 3.1 24B Instruct model card](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503)
- [DeepSeek R1 Distill Qwen 32B model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, analysis]

**Output Format:** [Markdown or plain text hardware recommendations with priced component rows, compatibility findings, trade-offs, and verification notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include China-market CNY reference prices, local user quote overlays when supplied, price reference dates, compatibility status, FPS sample caveats, and local model fit estimates.]

## Skill Version(s):

0.1.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
