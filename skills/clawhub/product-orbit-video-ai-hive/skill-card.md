## Description:

This skill helps product, ecommerce, advertising, and social-commerce teams turn product 360-degree orbit video requests into production briefs, shot prompts, AI-HIVE video tasks, runnable commands, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and visual production teams use this skill to plan short product orbit videos, prepare prompts and shot lists, submit AI-HIVE video tasks, and check generated assets before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may submit paid AI-HIVE generation tasks or upload user-provided media.

Mitigation: Review prompts, routing, model configuration, price snapshots, and media authorization before submitting tasks; run a small sample before batch generation.

Risk: API credentials are required for AI-HIVE calls.

Mitigation: Store the API key only on trusted machines, prefer environment or local config storage, and avoid placing keys in prompts, logs, screenshots, or version control.

Risk: Generated orbit videos may be mistaken for exact product scans or verified product claims.

Mitigation: Treat outputs as generative marketing assets, verify product facts and claims with authoritative sources, and do not use generated views for dimensional, structural, industrial, legal, medical, or financial validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-orbit-video-ai-hive)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown with inline bash commands, JSON task records, and generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create blueprint JSON files, submit asynchronous AI-HIVE generation tasks, upload user-provided media, and download generated image or video assets.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
