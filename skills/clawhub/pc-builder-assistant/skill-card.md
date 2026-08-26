## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM sizing, and gaming or creator configurations using bundled China-market catalogs and verification rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to produce desktop PC part recommendations, upgrade plans, configuration completion, and compatibility guidance for budget, gaming, creator, compact/ITX, and local AI workloads. It is not intended for laptops, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global; bundled reference pricing is China-market CNY unless the user supplies a separate local overlay.

## Known Risks and Mitigations:

Risk: Bundled hardware catalogs and CNY price references may become stale or may not match a user's local market.

Mitigation: Use current online price checks when offline data is old or the user asks for real-time pricing, and keep user-supplied local currency overlays separate from CNY references.

Risk: Unrelated private files or overly broad user overlay inputs could expose data that is not needed for PC build advice.

Mitigation: Provide only relevant hardware, quote, or catalog overlay inputs and avoid sharing unrelated private files with the skill.

Risk: Incomplete catalog fields can leave purchase-critical compatibility details unresolved.

Mitigation: Run strict compatibility checks for complete build recommendations and present unresolved items as pre-purchase checks instead of claiming full compatibility.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Skill definition](SKILL.md)
- [Demand routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware scope](references/hardware-scope.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [User catalog overlay](references/user-catalog.md)
- [Price history](references/price-history.md)
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

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or structured text with part lists, prices, totals, compatibility findings, trade-off notes, and pre-purchase checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CNY by default, keeps user-supplied overlay currencies separate, and includes price reference dates and compatibility status for concrete build recommendations.]

## Skill Version(s):

0.1.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
