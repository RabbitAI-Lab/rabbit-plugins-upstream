## Description:

Helps brand IP and virtual-avatar marketing teams turn content-calendar requests into a 30-day Chinese workflow with scripts, scenes, media-generation tasks, AI-HIVE commands, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing, ecommerce, advertising, and social-content teams use this skill to plan brand digital-avatar campaigns, produce scripts, storyboards, prompts, and shot lists, and run AI-HIVE image or video generation after reviewing billable task parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE media upload and generation can expose user-provided assets and may incur API costs.

Mitigation: Use only authorized assets, review prompts, model, routing mode, and pricing snapshot before execution, and run a small sample before batch generation.

Risk: API keys may be read from the environment or stored in ~/.ai-hive/config.json.

Mitigation: Prefer environment-scoped secrets where practical, restrict config-file permissions, and avoid placing keys in prompts, logs, screenshots, or committed files.

Risk: Brand-avatar outputs can create misleading endorsements, unauthorized likeness use, or unsupported product claims.

Mitigation: Confirm brand, likeness, reference-media, and claim authorization before generation, mark uncertain facts for review, and avoid fake testimonials or platform-rule evasion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/brand-avatar-content-calendar-ai-hive)
- [AI-HIVE chat entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown responses with bash command blocks, JSON task records, and local file paths from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model identifier, pricing snapshot, taskId, task status, download location, and quality checklist entries.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
