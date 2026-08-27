## Description:

AI大模型专家｜AI漫剧剪辑 helps short-drama, comic-drama, advertising, ecommerce, paid-growth, and multi-platform operations teams turn existing media into rough cuts, refined edits, aspect-ratio variants, and original rewritten versions based on authorized reference structures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and marketing teams use this skill to plan comic-drama and short-video editing workflows, inspect media, produce ffmpeg command plans, create production briefs, and call AI-HIVE image or video generation when authorized source material needs generative replacement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE receives media files that the user explicitly uploads for generation or editing tasks.

Mitigation: Upload only media that the user is authorized to share with AI-HIVE and avoid including unnecessary personal, confidential, or third-party content.

Risk: The skill stores or reads an AI-HIVE API key from local configuration or environment variables.

Mitigation: Keep API keys out of public repositories and screenshots, restrict local file permissions, rotate keys if exposed, and prefer environment or local config storage.

Risk: The skill proposes and runs ffmpeg or ffprobe shell commands against local media files.

Mitigation: Review generated commands and paths before execution, keep source media backups, and run commands in a controlled working directory.

Risk: Reference-based comic-drama editing can create copyright, likeness, brand, or factual-accuracy issues if source material is not authorized or checked.

Mitigation: Use only authorized references, rewrite characters and scenes instead of copying protected expression, and verify claims, subtitles, product details, and platform requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-comic-drama-editing)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with bash snippets, JSON briefs, API task metadata, and generated or edited media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require ffmpeg, ffprobe, requests, local AI-HIVE API-key configuration, authorized media uploads, and review of generated commands before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
