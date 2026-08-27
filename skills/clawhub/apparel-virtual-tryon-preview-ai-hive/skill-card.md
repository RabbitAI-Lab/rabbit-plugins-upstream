## Description:

Helps apparel merchants, consumer content tools, and styling operations teams create AI-HIVE virtual try-on image workflows, prompts, reference-image strategies, runnable commands, and review checklists for previewing garments on authorized people.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External apparel sellers, content operators, and developers use this skill to turn garment images, authorized person photos, scenes, poses, aspect ratios, and channel constraints into production-ready virtual try-on image plans and AI-HIVE generation commands. It supports ecommerce, advertising, marketing, livestream, social, short-drama, and comic-style content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API key exposure through prompts, logs, screenshots, or committed files.

Mitigation: Use environment variables or the local config flow, keep real keys out of prompts and generated artifacts, and review logs and task records before sharing.

Risk: Unauthorized or sensitive person and garment images may be uploaded to AI-HIVE or object storage.

Mitigation: Upload only images the user has rights to use, confirm privacy and commercial permissions for people and brands, and avoid sensitive personal media unless appropriate consent and review are in place.

Risk: Image or video generation can incur charges or create duplicate billable work.

Mitigation: Review prompt, model, routing mode, batch size, parameters, and pricing snapshot before submission; start with small batches and keep task records for deduplication.

Risk: Virtual try-on outputs may be mistaken for verified fit, fabric, comfort, sizing, or product-performance evidence.

Mitigation: Label outputs as visual previews, verify product facts separately, and avoid claims about real fit, material behavior, endorsements, or platform performance that are not independently supported.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/apparel-virtual-tryon-preview-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with inline bash commands, optional JSON task records, and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE model routing choices, pricing snapshots, task IDs, media IDs, download paths, and quality checklists.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
