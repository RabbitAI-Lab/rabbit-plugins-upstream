## Description:

Use for budget desktop PC build planning and recommendations, PC hardware DIY, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact, or ITX desktop builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and PC-building agents use this skill to plan desktop PC builds, upgrades, component substitutions, compatibility reviews, China-market CNY price-aware recommendations, local LLM hardware sizing, and gaming or creator workstation configurations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled Python tools are executed during catalog queries, compatibility checks, model-fit estimates, and price-history checks.

Mitigation: Install and run the skill only in an agent environment where executing its bundled Python scripts is expected, and review tool outputs as planning evidence rather than purchase authorization.

Risk: Offline China-market CNY prices can become stale or differ from checkout prices, local markets, warranty terms, and stock.

Mitigation: Use the skill's stated price-date and live-price fallback behavior, and verify exact SKU, channel, stock, warranty, and checkout price before buying.

Risk: User-provided overlay files may contain inaccurate hardware facts or local quote data.

Mitigation: Limit overlays to hardware and quote facts intended for PC-build planning, validate them with the bundled schema, keep currencies separate, and preserve unresolved compatibility fields as review items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [routing.md](references/routing.md)
- [selection-policy.md](references/selection-policy.md)
- [compatibility.md](references/compatibility.md)
- [pricing.md](references/pricing.md)
- [local-model-fit.md](references/local-model-fit.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with component tables, compatibility findings, price notes, and occasional inline shell commands for the agent to run bundled tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CNY reference prices, user-supplied overlay prices kept in their original currency, compatibility review items, and price reference dates.]

## Skill Version(s):

0.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
