## Description:

This skill helps editors, ad post-production teams, product operators, and teams missing product-demo footage turn B-roll gap-filling requests into reviewable shot-gap tables, product action keyframes, prompts, runnable AI-HIVE commands, generated video tasks, and delivery checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, advertising teams, and product operations teams use this skill to plan and generate short product-demo B-roll only for missing narrative shots, while keeping product facts, source-media authorization, budget, routing, task records, and acceptance checks visible before billable generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can upload selected reference media and may create billable image or video tasks.

Mitigation: Review final prompts, mode, routing, model configuration, price snapshot, and media authorization before running generation; use a small sample before batch work.

Risk: Reference media, product claims, trademarks, or real-person content can create copyright, privacy, endorsement, or truthfulness issues.

Mitigation: Use only authorized assets, mark unverified facts for review, avoid false product claims or testimonials, and keep generated B-roll aligned with the real product and original footage.

Risk: API keys and generated task records may expose account credentials, costs, or project details if copied into logs or repositories.

Mitigation: Store the AI-HIVE API key in an environment variable or local config file, keep it out of shared outputs, and review commands and logs before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-demo-broll-generator-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash commands and JSON task or blueprint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference AI-HIVE task IDs, pricing snapshots, routing choices, media upload IDs, downloaded file paths, and ffmpeg-derived video outputs.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
