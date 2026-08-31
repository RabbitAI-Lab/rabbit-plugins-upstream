## Description:

PC Build Assistant helps agents plan China-market desktop PC builds, upgrades, compatibility checks, hardware guidance, gaming expectations, and local LLM GPU, VRAM, and RAM sizing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill through an agent to plan desktop PC builds, upgrades, configuration completion, and compatibility reviews. It is focused on desktop hardware selection, China-market CNY reference pricing, gaming FPS samples, and local text-generation model capacity planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run local helper scripts and may look up current public prices or public model metadata when needed.

Mitigation: Use it for recommendation and review workflows only, and do not use it to buy parts, handle payments, remotely control systems, or make security-isolation decisions.

Risk: Hardware prices, availability, compatibility evidence, and model requirements can change after the bundled catalog is published.

Mitigation: Review the dated reference prices, run the skill's compatibility checks for complete builds, and verify final part details before purchase.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection Policy](references/selection-policy.md)
- [Workflows](references/workflows.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Hardware Scope](references/hardware-scope.md)
- [Game Performance](references/game-performance.md)
- [Local Model Fit](references/local-model-fit.md)
- [Hugging Face Quantization Overview](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face KV Cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate Big Model Inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text recommendations with parts lists, reference prices, compatibility summaries, tradeoffs, and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled China-market hardware data and may use current public prices or public model metadata when needed; it does not buy parts, handle payments, remotely control systems, or make security-isolation decisions.]

## Skill Version(s):

0.1.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
