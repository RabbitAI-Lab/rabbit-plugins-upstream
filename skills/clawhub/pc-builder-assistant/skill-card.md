## Description:

Use for budget desktop PC build planning and recommendations, PC hardware DIY, upgrades, configuration completion, compatibility checks, hardware guidance, local LLM GPU/VRAM/RAM sizing, and gaming, streaming, creator, aesthetic, compact or ITX builds. Bundled prices are China-market CNY references; explicit user overlays keep currencies separate. 中文支持预算装机、装机 DIY、整机推荐、旧机升级、配置补全、搭配或兼容检查、硬件问答，以及游戏直播、生产力、本地 AI、外观海景房和紧凑或 ITX 主机。 Do not use for laptops, server procurement, ordering or payment, remote control, security isolation, or standalone software, game or agent tutorials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users can use the skill to plan desktop PC builds, upgrades, and part substitutions for budgets and workloads such as gaming, content creation, and local AI. It provides compatibility checks, hardware guidance, and China-market CNY reference prices where available.

### Deployment Geography for Use:

Global; bundled price references are for the China market in CNY, with separate user-provided currency overlays supported.

## Known Risks and Mitigations:

Risk: The skill has file-reading and network capabilities that may not be obvious from its declared scope.

Mitigation: Limit access to the bundled catalogs, relevant user-provided details, and permitted public sources; do not provide credentials or unrelated filesystem access.

Risk: Some queries may produce unbounded output.

Mitigation: Use only the information needed for the request and summarize relevant results.

Risk: Desktop PC recommendations may not fit laptop requests.

Mitigation: Route laptop requests to a laptop-focused skill; this skill explicitly excludes laptops.

## Reference(s):

- [PC Build Assistant on ClawHub](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Hardware scope](references/hardware-scope.md)
- [Build and upgrade workflows](references/workflows.md)
- [Compatibility guidance](references/compatibility.md)
- [Pricing guidance](references/pricing.md)
- [Transformers quantization documentation](https://huggingface.co/docs/transformers/main/en/quantization)
- [Transformers KV cache documentation](https://huggingface.co/docs/transformers/kv_cache)
- [Accelerate big model inference documentation](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Analysis]

**Output Format:** [Markdown prose and component lists or tables, with pricing and compatibility notes when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Price references are dated China-market CNY data unless a separate user-provided currency overlay applies.]

## Skill Version(s):

0.1.56 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
