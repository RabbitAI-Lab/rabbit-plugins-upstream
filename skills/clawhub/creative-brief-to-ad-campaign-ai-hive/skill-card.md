## Description:

Creative Brief转广告全案｜AI-HIVE helps brand, agency, creative, and ecommerce teams turn a campaign brief into a reviewable ad plan, asset-generation tasks, runnable AI-HIVE commands, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing, advertising, creative, and ecommerce teams use this skill to convert a Creative Brief into Chinese campaign strategy, platform-specific content tasks, image and video prompts or commands, task records, and quality checks. It supports AI-HIVE image and video generation after the user reviews inputs, routing, budget-sensitive options, and authorized media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store an AI-HIVE API key in a local config file.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable when persistent local storage is not desired, and avoid placing real keys in prompts, logs, screenshots, or source packages.

Risk: The skill can upload selected campaign prompts and reference media to AI-HIVE.

Mitigation: Use only media that the user is authorized to upload or transform, and review prompts and reference files before any generation command is submitted.

Risk: Image and video generation jobs may cost money.

Mitigation: Review routing mode, model, prompt, batch size, and price snapshot before execution; run a small sample before batch generation.

Risk: Campaign outputs can contain unsupported product claims, copied creative elements, or misleading commercial promises.

Mitigation: Verify product facts, platform requirements, usage rights, and human approval before publishing or reusing generated campaign assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/creative-brief-to-ad-campaign-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON records and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON blueprints, submit AI-HIVE generation jobs, upload selected media, poll task status, and download generated images or videos when the user provides an API key and confirms execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
