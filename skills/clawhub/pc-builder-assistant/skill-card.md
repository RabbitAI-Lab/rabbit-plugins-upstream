## Description:

PC Build Assistant helps agents plan desktop PC builds and upgrades, check component compatibility, compare China-market reference pricing, estimate gaming performance, and size hardware for local LLM use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External PC builders and agent users use this skill to create or review desktop part lists, plan upgrades, fill missing configuration details, check compatibility, and size hardware for gaming, creator, compact, aesthetic, and local AI workloads. It uses bundled China-market CNY reference prices by default and supports user-provided catalog overlays when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled hardware prices may differ from current store listings.

Mitigation: Verify current listings before buying and preserve price reference dates in recommendations.

Risk: User catalog overlays may disclose hardware or pricing facts to the agent.

Mitigation: Provide only overlay files whose hardware and pricing facts are acceptable to share with the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [Hardware scope](references/hardware-scope.md)
- [Local model fit](references/local-model-fit.md)
- [Game performance](references/game-performance.md)
- [User catalog overlays](references/user-catalog.md)
- [Hugging Face Transformers quantization](https://huggingface.co/docs/transformers/main/en/quantization)
- [Hugging Face Transformers KV cache](https://huggingface.co/docs/transformers/kv_cache)
- [Hugging Face Accelerate big model inference](https://huggingface.co/docs/accelerate/main/concept_guides/big_model_inference)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with optional inline commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include price reference dates, compatibility conclusions, trade-offs, and buying verification notes when producing concrete PC part recommendations.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
