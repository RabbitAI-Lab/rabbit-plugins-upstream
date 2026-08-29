## Description:

Helps directors, writers, manhua and short-drama teams, and AI video creators turn Chinese storyboard requests into shot plans, prompts, runnable AI-HIVE commands, task records, and continuity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative teams and developers use this skill to plan short-drama, commerce, advertising, marketing, livestream-sales, and social video storyboards, then prepare AI-HIVE image or video generation tasks after review. It emphasizes authorized source material, continuity anchors, pricing or route confirmation before paid generation, and delivery records for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied images, videos, and audio can be uploaded to AI-HIVE for generation workflows.

Mitigation: Use only media the user is authorized to process, avoid sensitive third-party data, and treat uploads as disclosure to AI-HIVE.

Risk: Generation tasks may be paid and can use different routing modes.

Mitigation: Confirm model configuration, pricing snapshot, route, and task parameters before submitting generation jobs.

Risk: The workflow requires an AI-HIVE API key and can store it in a local config file.

Mitigation: Prefer environment variables or a tightly protected config file and do not place real API keys in prompts, logs, screenshots, scripts, or version control.

Risk: Storyboard and marketing outputs can contain unsupported product, platform, copyright, or performance claims.

Mitigation: Require factual sources for claims and human review for copyright, brand, privacy, regulated-domain, and platform-rule constraints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/short-drama-storyboard-studio-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create blueprint JSON, upload authorized media to AI-HIVE, poll asynchronous generation tasks, download generated media, and run deterministic ffmpeg video edits when invoked by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
