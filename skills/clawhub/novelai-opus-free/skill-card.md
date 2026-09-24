## Description:

Opus zero-Anlas NovelAI workflows for OpenClaw: fiction writing, cost-aware single-image generation, img2img, inpainting, pre-encoded Vibe use, annotation, selected free Director tools, and same-session verification reuse with strict account and balance guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[techotaku39](https://clawhub.ai/user/techotaku39)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to plan fiction workflows, estimate NovelAI image costs, and run tightly gated single-image or image-editing operations that must avoid NovelAI Image Anlas charges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a host-managed NovelAI token and may query account or subscription state.

Mitigation: Use only host-managed credentials, never paste the token into chat, and keep account responses, balances, and credentials out of prompts, logs, saved files, and metadata.

Risk: A zero-Anlas estimate does not mean every related service is free, and V5 zero-Anlas images can still consume the NovelAI Opus Usage Limit.

Mitigation: Review the displayed account, estimate, model, size, steps, and usage-limit information before allowing image generation.

Risk: Changing billing-affecting image parameters after verification can invalidate the prior zero-cost result.

Mitigation: Run a fresh account and cost gate whenever operation type, model, size, steps, image count, base image, mask, Vibe state, Director operation, or other billing-relevant fields change.

Risk: Ambiguous failures or billing/account warnings can make automatic retries unsafe.

Mitigation: Retry only clearly transient failures with identical parameters, stop on authentication, billing, account, usage-limit, parameter, or ambiguous processing signals, and recheck account state before continuing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/techotaku39/skills/novelai-opus-free)
- [Project homepage](https://github.com/techotaku39/openclaw-novelai/tree/main/variants/openclaw-novelai-opus-free)
- [Costs and quotas](docs/COSTS-AND-QUOTAS.md)
- [NovelAI Subscription](https://docs.novelai.net/en/subscription/)
- [NovelAI FAQ - Opus Usage Limits](https://docs.novelai.net/en/faq/)
- [Steps and Prompt Guidance](https://docs.novelai.net/en/image/stepsguidance/)
- [NovelAI Image Generation](https://docs.novelai.net/en/image/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls, Files]

**Output Format:** [Natural-language text and Markdown, with gated NovelAI tool calls and non-secret local generation metadata when an operation is allowed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a host-managed NOVELAI_TOKEN; image operations are limited to one request at a time and must pass explicit zero-Anlas checks.]

## Skill Version(s):

0.2.3 (source: frontmatter and changelog, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
