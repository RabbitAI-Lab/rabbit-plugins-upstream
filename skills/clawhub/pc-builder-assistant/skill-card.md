## Description:

Helps agents plan budget desktop PC builds, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM hardware sizing, and gaming, streaming, creator, aesthetic, compact, or ITX builds using bundled China-market CNY references and optional user-provided price overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for desktop PC parts lists, upgrade advice, compatibility review, hardware Q&A, gaming performance references, and local AI hardware fit guidance. It is scoped away from laptops, server procurement, ordering or payment, remote control, security isolation, and standalone software tutorials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled Python scripts and hardware catalogs are used to produce recommendations and may read an overlay file explicitly supplied by the user.

Mitigation: Review the skill before installation and provide only overlay data that is acceptable for the agent to process.

Risk: Fresh pricing or model-fact requests may cause the agent to search public sources, which could expose private quotes or hardware lists if included in the lookup.

Mitigation: Avoid sending private procurement details to online searches unless that disclosure is acceptable.

Risk: Hardware recommendations can be wrong or incomplete when price, compatibility, or specification evidence is stale or missing.

Mitigation: Confirm final prices, exact SKUs, compatibility notes, and purchase details before ordering parts.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Compatibility Checks](references/compatibility.md)
- [Pricing Rules](references/pricing.md)
- [Selection Policy](references/selection-policy.md)
- [Workflow Modes](references/workflows.md)
- [Hardware Scope](references/hardware-scope.md)
- [Local Model Fit](references/local-model-fit.md)
- [Game Performance](references/game-performance.md)
- [User Catalog Overlay](references/user-catalog.md)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with structured parts lists, compatibility findings, price notes, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite bundled catalog dates, user overlay prices, or public source checks when fresh pricing or model facts are requested.]

## Skill Version(s):

0.1.27 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
