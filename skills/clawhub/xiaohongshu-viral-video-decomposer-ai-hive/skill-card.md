## Description:

Helps Xiaohongshu brands, creators, and content marketing teams turn authorized reference videos, product facts, audience details, usage scenarios, and account voice into a reviewable viral-video decomposition workflow, original scripts, generation prompts, runnable AI-HIVE commands, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to analyze authorized Xiaohongshu-style reference videos and produce original commercial short-video plans, scripts, prompts, commands, and task records. It is intended for user-directed marketing media workflows that require authorization checks, factual product claims, and review before paid AI-HIVE generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized or private media could be uploaded to a third-party AI-HIVE service.

Mitigation: Use only media the user is authorized to upload, avoid private customer materials, and confirm rights before any upload or generation command.

Risk: Marketing outputs can contain unsupported product claims, customer testimonials, or implied guarantees.

Mitigation: Ground product and brand statements in provided facts, review claims manually, and avoid promises about virality, ranking, sales, approval, or return on investment.

Risk: Generation commands can incur cost or route work differently than intended.

Mitigation: Review the prompt, routing mode, price snapshot, model configuration, and output directory before submitting tasks; run a small sample before batch generation.

Risk: API credentials may be exposed through commands, logs, screenshots, or configuration files.

Mitigation: Use environment variables or the local config helper, keep placeholder keys in examples, and avoid sharing logs or files that contain real API keys.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/xiaohongshu-viral-video-decomposer-ai-hive)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown responses with inline shell commands, Python helper usage, JSON blueprints, prompts, task IDs, status records, and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit user-approved AI-HIVE media generation tasks, poll asynchronous task status, upload authorized reference media, and download generated files.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
