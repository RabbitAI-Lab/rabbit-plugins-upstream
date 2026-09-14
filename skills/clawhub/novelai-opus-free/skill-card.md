## Description:

Opus zero-Anlas NovelAI workflows for OpenClaw: fiction writing, cost-aware single-image generation, img2img, inpainting, pre-encoded Vibe use, annotation, and selected free Director tools with strict account and balance guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[techotaku39](https://clawhub.ai/user/techotaku39)

### License/Terms of Use:

MIT

## Use Case:

External developers and creators use this OpenClaw skill to plan fiction workflows and run NovelAI Opus image operations only when account, estimator, and balance checks prove the request is zero Image Anlas. It is intended for cost-aware single-image generation, img2img, inpainting, existing Vibe use, annotation, and selected Director tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a NovelAI token through OpenClaw.

Mitigation: Use host-managed credentials only; do not request, print, store, or include NOVELAI_TOKEN in prompts, arguments, URLs, logs, files, or metadata.

Risk: Zero-Anlas V5 image generations can still consume the separate Opus Usage Limit.

Mitigation: Check the account before image operations, show the Usage Limit implication to the user, and monitor usage after successful generation.

Risk: An image request can spend paid Image Anlas if cost estimation is missing, ambiguous, or not matched to the final parameters.

Mitigation: Block image tool calls unless the exact final request returns an explicit numeric 0 Anlas estimate, then audit the balance after the operation and stop if it changed.

## Reference(s):

- [OpenClaw NovelAI Opus Free skill page](https://clawhub.ai/techotaku39/skills/novelai-opus-free)
- [Skill homepage](https://github.com/techotaku39/openclaw-novelai/tree/main/variants/openclaw-novelai-opus-free)
- [Opus Free Enhancement Mode: Costs and Quotas](docs/COSTS-AND-QUOTAS.md)
- [NovelAI Subscription](https://docs.novelai.net/en/subscription/)
- [NovelAI FAQ - Opus Usage Limits](https://docs.novelai.net/en/faq/)
- [NovelAI Steps and Prompt Guidance](https://docs.novelai.net/en/image/stepsguidance/)
- [NovelAI Image Generation](https://docs.novelai.net/en/image/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown or text guidance, optional generated image files, and non-secret generation metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image operations require a host-managed NOVELAI_TOKEN, an active Opus account, explicit zero-Anlas cost estimation, single-image normal-size parameters, and post-operation balance checks.]

## Skill Version(s):

0.2.0 (source: frontmatter and changelog, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
