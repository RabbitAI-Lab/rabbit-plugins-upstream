## Description:

Helps short-drama, comics-drama, advertising, ecommerce, and performance-marketing teams organize existing media into rough cuts, finished edits, vertical adaptations, or paid-media variants, with local ffmpeg helpers and optional AI-HIVE image/video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content teams and developers use this skill to plan short-video color consistency, aspect-ratio conversion, rough-cut and finished-edit workflows, and authorized reference-to-original rewrite prompts. It can also generate auditable ffmpeg commands and AI-HIVE task commands for media generation, upload, polling, and download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and prompts may be sent to AI-HIVE under the user's API key.

Mitigation: Use only authorized, non-sensitive footage and confirm that external processing is acceptable before running upload or generation commands.

Risk: Generated or suggested shell commands could affect local files or produce unintended edits.

Mitigation: Review commands before execution and keep source media and intermediate outputs recoverable.

Risk: API keys may be exposed if stored in shared locations or copied into public artifacts.

Mitigation: Store secrets in local environment variables or private config, keep file permissions restricted, and rotate keys if exposed.

Risk: Bundled image and video generation tools are broader than the advertised color-consistency helper.

Mitigation: Limit use to the intended editing workflow and review generation prompts, uploads, and downloads against project policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-color-grade-consistency)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration or blueprint files, and optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require ffmpeg, ffprobe, requests, an AI-HIVE API key, local source media, and user review of commands before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
