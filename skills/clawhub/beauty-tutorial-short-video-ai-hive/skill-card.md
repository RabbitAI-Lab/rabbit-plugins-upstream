## Description:

This skill helps beauty brands, creators, training teams, and ecommerce content teams turn beauty tutorial short-video requests into reviewable scripts, key frames, prompts, subtitles, product cards, runnable AI-HIVE commands, and acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External beauty brands, creators, training teams, and ecommerce content teams use this skill to plan and generate beauty tutorial short-video deliverables for ecommerce, advertising, social, and creator workflows. It turns product facts, official usage, authorized reference media, platform constraints, and duration targets into scripts, prompts, AI-HIVE task commands, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an AI-HIVE API key and may persist credentials in local configuration.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable when persistence is not desired, avoid exposing keys in files or logs, and review generated commands before running them.

Risk: Video or image generation can incur costs or launch asynchronous tasks.

Mitigation: Review prompts, routing mode, model configuration, and pricing snapshot before submitting generation tasks; use small samples before batch runs.

Risk: Reference media, brands, people, logos, or protected creative material may be unauthorized.

Mitigation: Use only media and brand assets the user has rights to use; if authorization is unclear, provide abstract structure guidance and new creative direction instead of replication.

Risk: Generated beauty content can imply unsupported product, medical, performance, or platform claims.

Mitigation: Mark unverified facts as pending review, avoid therapeutic or guaranteed performance claims, and require human review against product and platform requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/beauty-tutorial-short-video-ai-hive)
- [wubin1836 publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON snippets and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task records, pricing snapshots, task IDs, and local file paths when generation is submitted.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
