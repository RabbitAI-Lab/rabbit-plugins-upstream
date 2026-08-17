## Description:

PC Build Assistant helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact, or ITX desktop configurations using China-market CNY reference data and optional user-supplied catalog overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agent operators use this skill to produce desktop PC parts recommendations, upgrade plans, compatibility reviews, hardware explanations, local LLM sizing guidance, and price-aware build reports. It is scoped to desktop PC hardware planning and does not cover laptops, server procurement, ordering, payment, remote control, security isolation, or standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled component prices are China-market CNY references and can become stale or differ from local stock, warranty, tax, shipping, and checkout prices.

Mitigation: Show price reference dates, keep CNY and user-supplied local currencies separate, and tell users to verify exact retailer price and SKU before purchase.

Risk: Hardware recommendations can be misleading if compatibility-critical fields are missing or if a user's existing parts are incomplete or ambiguous.

Mitigation: Use the bundled compatibility workflow for complete builds and explicitly list concrete review items such as physical clearance, connectors, QVL, or unknown catalog fields.

Risk: User-provided catalog overlays can contain incorrect SKUs, conflicting specifications, or mixed currencies.

Mitigation: Require explicit SKU and currency evidence, validate overlays against the documented schema, and avoid combining prices across currencies.

Risk: The skill can run local Python helper scripts and may search current market prices when offline data is stale or insufficient.

Mitigation: Review planned script execution and network lookup behavior before deployment; security evidence reports no purchasing, credential access, broad local scanning, or hidden background activity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing rules](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Compatibility checks](references/compatibility.md)
- [Pricing rules](references/pricing.md)
- [Scenario guidance](references/scenarios.md)
- [Upgrade and workflow guidance](references/workflows.md)
- [Hardware scope](references/hardware-scope.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [Price history](references/price-history.md)
- [User catalog overlay](references/user-catalog.md)
- [User overlay schema](references/user-overlay.schema.json)
- [English usage](references/english-usage.md)
- [Hugging Face Transformers quantization documentation](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache documentation](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference documentation](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown recommendations and tables with concise prose; JSON snippets for explicit user-provided catalog overlays when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should keep prices dated, keep currencies separate, summarize compatibility status in user-facing language, and avoid exposing internal command status or scanner details.]

## Skill Version(s):

0.1.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
