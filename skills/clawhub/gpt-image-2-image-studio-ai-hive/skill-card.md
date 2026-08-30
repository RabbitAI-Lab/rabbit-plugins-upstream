## Description:

This agent skill helps brand, ecommerce, and creative teams turn GPT Image 2 image generation and editing requests into Chinese production workflows, prompts, runnable AI-HIVE commands, batch variants, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, marketing, and creative teams use this skill to turn product or campaign image needs into reviewable Chinese briefs, prompts, AI-HIVE execution commands, task records, and acceptance checks. Developers can use the bundled scripts to create blueprint JSON, query AI-HIVE model options, upload authorized reference assets, submit image or video tasks, poll status, and download results after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses user-provided AI-HIVE API credentials and may persist them in ~/.ai-hive/config.json after initialization.

Mitigation: Prefer AI_HIVE_API_KEY for credential use without local persistence, or review ~/.ai-hive/config.json after running init.

Risk: AI-HIVE generation calls can incur charges and may upload user-provided assets.

Mitigation: Confirm parameters, routing, price snapshot, and asset rights before execution; start with a small batch before larger runs.

Risk: Commercial image workflows can create misleading claims, unauthorized likenesses, or overly similar recreations of protected material.

Mitigation: Use only assets the user has rights to use, avoid unsupported product claims or testimonials, and keep reference reuse to abstract structure unless authorization is confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/gpt-image-2-image-studio-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce blueprint JSON, AI-HIVE task records, status output, and downloaded generated media when the user confirms execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
