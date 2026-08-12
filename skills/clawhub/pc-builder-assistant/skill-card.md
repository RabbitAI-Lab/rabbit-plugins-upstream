## Description:

Helps agents plan desktop PC builds, upgrades, compatibility checks, configuration completion, local LLM GPU/VRAM/RAM sizing, and user-supplied local price catalogs, with bundled China-market CNY reference pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill to assemble or review desktop PC parts lists, estimate local LLM hardware fit, and produce purchase-oriented guidance with compatibility, price, and verification caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hardware prices, availability, warranty terms, and exact SKUs can change after the bundled catalog date or vary by seller.

Mitigation: Verify final prices, local availability, warranty coverage, and exact product pages before purchasing.

Risk: Bundled Python scripts may be run to query catalogs, check compatibility, import explicit overlays, or estimate model fit.

Mitigation: Review the skill package before deployment and provide overlay files only when they are intentionally supplied for the task.

Risk: Compatibility and local LLM sizing outputs are planning guidance, not guarantees of fit, performance, thermals, or long-context behavior.

Mitigation: Use the reported verification notes and confirm case clearances, power connectors, BIOS/QVL details, model configuration, and real-world performance before relying on the build.

Risk: The skill may use web searches or fixed GitHub/Hugging Face lookups when current prices or model configuration data are needed.

Mitigation: Treat retrieved external data as supporting evidence and cross-check purchase-critical or model-critical facts against primary sources.

## Reference(s):

- [Skill definition](SKILL.md)
- [Hardware scope](references/hardware-scope.md)
- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Workflows](references/workflows.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [User catalog overlay](references/user-catalog.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [Price history](references/price-history.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with part lists, prices, totals, compatibility findings, trade-offs, and verification notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled catalogs, explicit user overlays, and limited current-price or model-configuration lookups; final prices, SKU availability, local warranty, and exact purchasing terms require user verification.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
