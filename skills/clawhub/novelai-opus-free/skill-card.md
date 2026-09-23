## Description:

Opus zero-Anlas NovelAI workflows for OpenClaw: fiction writing, cost-aware single-image generation, img2img, inpainting, pre-encoded Vibe use, annotation, selected free Director tools, and same-session verification reuse with strict account and balance guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[techotaku39](https://clawhub.ai/user/techotaku39)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to plan fiction workflows and run NovelAI Opus image operations only when the current account, estimator, and session checks support zero Image Anlas usage. It is intended for guarded single-image generation, img2img, inpainting, prompt planning, tag suggestions, annotation, and selected Director tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a host-managed NovelAI token and can query account status, estimate costs, and generate or edit one image at a time.

Mitigation: Confirm this access before installation, keep the token host-managed, and do not print, store, or include credentials in prompts, logs, files, URLs, or metadata.

Risk: The same-session cost lease intentionally avoids repeated estimator calls when billing-affecting parameters are unchanged.

Mitigation: Ask for a fresh cost verification when every image must be rechecked; otherwise invalidate the lease on new sessions, restarts, parameter changes, tool errors, account warnings, or account and usage discrepancies.

Risk: Zero-Anlas image generation is account- and parameter-sensitive and may still consume the separate Opus V5 Usage Limit.

Mitigation: Generate only after an explicit numeric zero-Anlas estimate or matching verified lease, limit requests to one normal-size image, and disclose that V5 Usage Limit may be consumed.

Risk: Paid or unverified NovelAI operations could spend Anlas if used outside the skill's guarded path.

Mitigation: Block new Vibe encoding, background removal, Precise Reference, Enhance, upscaling, batches, high-resolution work, automatic retries, and any paid fallback.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/techotaku39/skills/novelai-opus-free)
- [Costs and Quotas](docs/COSTS-AND-QUOTAS.md)
- [NovelAI Subscription](https://docs.novelai.net/en/subscription/)
- [NovelAI FAQ - Opus Usage Limits](https://docs.novelai.net/en/faq/)
- [Steps and Prompt Guidance](https://docs.novelai.net/en/image/stepsguidance/)
- [NovelAI Image Generation](https://docs.novelai.net/en/image/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or plain text guidance with image parameters, cost-check notes, prompts, and non-secret generation metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model, dimensions, steps, seed, explicit zero estimate, output path, and V5 Usage Limit notes; must not include credentials or account secrets.]

## Skill Version(s):

0.2.1 (source: frontmatter and changelog, released 2026-09-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
