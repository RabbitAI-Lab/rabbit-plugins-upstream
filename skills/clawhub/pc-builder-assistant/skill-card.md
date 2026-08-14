## Description:

PC Build Assistant helps agents plan desktop PC builds, upgrades, compatibility checks, hardware guidance, local LLM hardware sizing, and gaming or creator configurations using bundled China-market CNY references and optional user-supplied price overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for desktop PC parts lists, upgrades, compatibility reviews, hardware explanations, local LLM GPU/VRAM/RAM sizing, and game performance guidance, with China-market CNY pricing as the default market reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled or current price and specification data may be stale, incomplete, or market-specific.

Mitigation: Use bundled data with price dates, look up current market prices or official specifications when required, and state concrete review points before purchase.

Risk: User overlay files can change the parts and prices considered by the skill.

Mitigation: Only provide overlay files the user intentionally wants the skill to read or write, and keep currencies separate rather than converting or mixing them.

Risk: Compatibility conclusions can be incomplete when catalog fields are missing.

Mitigation: Run strict compatibility checks for complete builds and surface unresolved hardware fields as purchase-time review items instead of claiming full compatibility.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Pricing](references/pricing.md)
- [Compatibility](references/compatibility.md)
- [Hardware scope](references/hardware-scope.md)
- [Workflows](references/workflows.md)
- [Scenarios](references/scenarios.md)
- [User catalog overlays](references/user-catalog.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text reports with priced parts lists, compatibility conclusions, trade-off rationale, and verification notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default prices are CNY China-market references; current prices or official specifications may require web lookup when bundled data is stale or insufficient.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
