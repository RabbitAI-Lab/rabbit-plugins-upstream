## Description:

使用 AI Hive Seedance 2.5 将 PixVerse、PixVerse AI 或爱诗科技常见的社媒特效短片迁移为可审的动作与转场方案，支持文生、图片起动、参考节奏、视频编辑和片尾延长。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn PixVerse-style short video ideas into structured AI Hive Seedance 2.5 prompts and CLI workflows for text-to-video, image-to-video, reference-guided video, editing, and ending extension. It emphasizes authorized source media, protected subject or product areas, stable ending frames, and reviewable effect causality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected media files are sent to AI Hive or object storage for video generation.

Mitigation: Use only media you are authorized to upload, avoid sensitive content in prompts and files, and review the AI Hive service relationship before deployment.

Risk: The skill stores an AI Hive API key in ~/.ai-hive/config.json when initialized.

Mitigation: Keep the config file private, prefer environment or CLI-provided credentials in managed environments, and verify local file permissions after initialization.

Risk: Generated files may be downloaded to the default output directory.

Mitigation: Use --no-download to inspect task output as JSON or --output-dir to control where generated media is saved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/pixverse-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and CLI-generated JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI Hive video generation tasks, upload explicitly selected media, and download generated media files unless --no-download is used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
