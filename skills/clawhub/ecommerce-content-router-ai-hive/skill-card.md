## Description:

Routes e-commerce, advertising, marketing, short-form video, comic-video, product-selling, and social content requests into classified requirements, workflow choices, model modes, cost priorities, task queues, and optional AI-HIVE OpenAPI generation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, content operations teams, agencies, and developers use this skill to turn Chinese e-commerce content needs into reviewable production plans, prompts, runnable AI-HIVE commands, and quality checks. It can also guide confirmed image or video generation tasks after the user reviews parameters, routing mode, and likely cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media can be uploaded to AI-HIVE when the user runs generation commands.

Mitigation: Confirm the user has rights to the selected media and is comfortable sending it to AI-HIVE before running upload or generation steps.

Risk: Image and video generation can create paid tasks.

Mitigation: Review final prompts, model mode, routing mode, parameters, and pricing snapshot before submitting any generation job; use a small sample before batch work.

Risk: API keys may be stored locally if the init flow is used.

Mitigation: Use environment variables where practical, keep local config permissions restricted, and avoid placing API keys in scripts, logs, screenshots, or version control.

Risk: E-commerce content could include misleading claims, unauthorized imitation, or platform-rule evasion.

Mitigation: Keep factual claims sourced, require authorization for protected assets or brands, and avoid copied protected expression, fake testimonials, prohibited claims, or promises of sales and ranking outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-content-router-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured Chinese sections, inline shell commands, optional JSON task records, and downloaded media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs with user-provided credentials, upload selected reference media, poll asynchronous image or video tasks, and save generated files locally.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
