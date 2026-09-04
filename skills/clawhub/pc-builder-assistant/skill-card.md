## Description:

PC Build Assistant helps agents plan desktop PC builds and upgrades, check component compatibility, estimate China-market pricing, and size hardware for gaming, creator work, streaming, compact builds, and local LLM use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill through an agent to choose desktop components, complete or review configurations, compare upgrade paths, and understand hardware fit for gaming, creator, streaming, compact-build, and local LLM workloads. It is scoped away from laptops, server procurement, ordering or payment, remote control, security isolation, and standalone software tutorials.

### Deployment Geography for Use:

Global; bundled price references focus on China-market CNY data.

## Known Risks and Mitigations:

Risk: PC build recommendations can influence spending decisions.

Mitigation: Verify exact local SKU, warranty, stock, and checkout price before purchasing.

Risk: The skill may run bundled Python helpers, read explicit user-supplied hardware quote files, create normalized overlay files when directed, and browse for current hardware prices or specifications when offline data is insufficient.

Mitigation: Review the disclosed files before installation, run helpers only with intended inputs, and treat current market lookups as purchase-time references that still require user verification.

## Reference(s):

- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Scenarios](references/scenarios.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [User Catalog](references/user-catalog.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with parts lists, compatibility notes, price summaries, and occasional JSON overlay or shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled CNY price references by default; explicit user overlays keep currencies separate and do not perform cross-currency conversion.]

## Skill Version(s):

0.1.24 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
