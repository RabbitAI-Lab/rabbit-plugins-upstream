## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, China-market CNY price references, local LLM hardware sizing, and gaming or creator configurations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to assemble and review desktop PC parts lists, upgrades, and compatibility or price tradeoffs, primarily with China-market CNY catalog data. It also supports gaming performance lookup and local LLM GPU, VRAM, and RAM sizing within the documented desktop-hardware scope.

### Deployment Geography for Use:

Global, with bundled pricing focused on China-market CNY references

## Known Risks and Mitigations:

Risk: Bundled China-market CNY prices may differ from current checkout prices or prices in other regions.

Mitigation: Verify exact local SKUs, seller availability, and final checkout prices before purchasing.

Risk: Compatibility conclusions depend on exact part variants and complete fields such as case clearance, motherboard display outputs, power connectors, BIOS support, and memory QVL details.

Mitigation: Use the documented compatibility checks and confirm unresolved SKU-specific details against vendor specifications before buying parts.

Risk: User-provided overlay files can change recommendations and pricing behavior.

Mitigation: Only provide overlay files intentionally created for this skill and keep currencies separate when using local quote data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Needs routing](references/routing.md)
- [General component selection policy](references/selection-policy.md)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Work modes](references/workflows.md)
- [User hardware and quote overlay](references/user-catalog.md)
- [Hardware scope](references/hardware-scope.md)
- [Game FPS reference](references/game-performance.md)
- [Local model and hardware fit](references/local-model-fit.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with parts lists, compatibility findings, price notes, and concise guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local catalog evidence for compatibility, CNY pricing, game FPS samples, and local LLM fit estimates; does not order parts or process payments.]

## Skill Version(s):

0.1.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
