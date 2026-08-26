## Description:

AI开箱视频生成器｜AI-HIVE helps agents turn Chinese product-unboxing video requests into production briefs, storyboards, prompts, runnable AI-HIVE generation commands, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, marketers, and developers use this skill to plan and generate Chinese unboxing or product-display videos while preserving product facts, packaging order, platform format, budget, and review checkpoints. The skill can also guide AI-HIVE API use for model lookup, media upload, paid generation, task polling, downloads, and deterministic ffmpeg edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can incur paid jobs or route requests through external models and services.

Mitigation: Review prompts, model configuration, pricing snapshots, routing mode, and task parameters before submitting generation jobs; run a small sample before batch work.

Risk: The workflow may upload product images, reference videos, audio, logos, or other media.

Mitigation: Upload only media the user is authorized to use and avoid using the skill for protected-content copying, false product claims, fake testimonials, or platform-rule evasion.

Risk: The helper can store an AI-HIVE API key in a local configuration file.

Mitigation: Protect the API key, avoid placing it in logs, screenshots, or repositories, and remove or rotate it when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-unboxing-video-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSON briefs, AI-HIVE task records, downloaded media paths, and ffmpeg-derived video files when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
