## Description:

Assists agents with desktop PC build planning, upgrades, configuration completion, compatibility checks, hardware guidance, gaming and creator recommendations, and local LLM sizing using China-market CNY catalog data and optional user price overlays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan desktop PC builds, upgrades, part substitutions, compatibility reviews, local LLM hardware sizing, and gaming or creator configurations. It is scoped to desktop hardware advice and reference pricing, not ordering, payment, server procurement, laptops, remote control, or security-isolation work.

### Deployment Geography for Use:

Global, with bundled price references focused on the China market in CNY.

## Known Risks and Mitigations:

Risk: Hardware prices, stock, warranties, and regional availability can change or differ from the bundled China-market CNY references.

Mitigation: Treat price advice as a reference, preserve price dates, use explicit user overlays for local quotes, and recheck current retail listings before buying.

Risk: Incomplete or stale component specifications can lead to uncertain compatibility conclusions.

Mitigation: Run the bundled strict compatibility workflow for complete builds and list unresolved fields such as GPU length, cooler clearance, power connectors, display outputs, or motherboard expansion details as pre-purchase checks.

Risk: Historical price lookup may contact a fixed GitHub repository for package price snapshots.

Mitigation: Install only if that limited online lookup is acceptable; the security evidence indicates no payments, credential handling, background services, or ordering behavior.

Risk: Gaming FPS and local LLM sizing guidance are reference estimates or cataloged samples, not guaranteed performance results.

Mitigation: Use only recorded samples or documented estimator outputs, state missing coverage clearly, and avoid promising speed, long-context behavior, or frame rates without matching evidence.

## Reference(s):

- [Demand Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Workflows](references/workflows.md)
- [Pricing Rules](references/pricing.md)
- [Compatibility Checks](references/compatibility.md)
- [Hardware Scope](references/hardware-scope.md)
- [Scenario Rules](references/scenarios.md)
- [Hardware FAQ](references/hardware-faq.md)
- [User Catalog Overlay](references/user-catalog.md)
- [Local LLM Hardware Fit](references/local-model-fit.md)
- [Game Performance Reference](references/game-performance.md)
- [Price History](references/price-history.md)
- [English Usage](references/english-usage.md)
- [User Overlay JSON Schema](references/user-overlay.schema.json)
- [Hugging Face Transformers Quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown prose with structured parts lists, prices, compatibility notes, trade-offs, and verification points.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dated CNY reference prices, budget differences, and compatibility caveats; does not place orders or handle payments.]

## Skill Version(s):

0.1.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
