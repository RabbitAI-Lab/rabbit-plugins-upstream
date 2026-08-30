## Description:

Helps eyewear brands, ecommerce merchants, and styling content teams turn authorized eyewear and portrait inputs into a reviewable Chinese workflow for AI eyewear try-on previews, scene variants, prompts, commands, and quality checks using AI-HIVE when generation is approved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, eyewear brands, ecommerce sellers, and content teams use this skill to plan and produce AI eyewear try-on previews, product-scene variants, prompts, runnable AI-HIVE commands, and delivery checklists. It is intended for authorized portraits and product materials, with human review before any paid generation task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API keys can be exposed if copied into shared logs, repositories, screenshots, or prompts.

Mitigation: Use environment variables or the local config path only, keep placeholders in examples, and avoid sharing files or logs that contain real API keys.

Risk: The init flow can store an API key locally at ~/.ai-hive/config.json.

Mitigation: Treat the local config as sensitive, keep file permissions restricted, and remove or rotate the key when the workspace is shared.

Risk: Generation calls may incur charges or consume quota.

Mitigation: Review prompt, model, routing mode, pricing snapshot, and batch size before submitting; start with small samples before batch generation.

Risk: User-provided portraits, product images, logos, or references may lack rights or consent.

Mitigation: Use only authorized media, avoid impersonation or false endorsement, and fall back to abstract creative guidance when rights are unclear.

Risk: Generated eyewear try-on images can be mistaken for medical fitting or prescription guidance.

Mitigation: Do not use generated previews for pupillary distance, prescription, fit, or medical decisions; require professional measurement for those needs.

Risk: Generated commercial content can overstate product claims, certifications, sales outcomes, or platform performance.

Mitigation: Mark unverified facts as pending review and require source-backed claims for pricing, inventory, efficacy, financing, service scale, and platform rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/eyewear-tryon-preview-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with bash command examples, Python script usage, JSON task records, prompts, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, upload authorized media to AI-HIVE, poll asynchronous generation tasks, and download generated images or videos when the user confirms parameters and cost-sensitive routing.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
