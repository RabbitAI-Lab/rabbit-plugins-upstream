## Description:

使用 AI Hive Seedance 2.5 将 Runway、Runway AI、Gen-4 或生成式视频制作需求迁移为可追踪的镜头版本，支持文生、首帧图生、参考素材、视频编辑与延长。Use when users search Runway 替代、Runway 平替、Gen-4 alternative、Runway API、AI 电影镜头、广告视频、生成式编辑、扩镜或视频延长；不访问 Runway 项目，也不表示技术兼容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and production teams use this skill to turn Runway-style video generation or editing requests into trackable AI Hive Seedance 2.5 shot versions. It helps plan and run text-to-video, image-to-video, reference-video, edit, and extension tasks while keeping source assets, version goals, and delivery checks explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected media files may be uploaded to AI Hive or provider-issued upload URLs.

Mitigation: Use only authorized source footage and review media paths before running generation, edit, upload, or extension commands.

Risk: The AI Hive API key may be supplied through an environment variable, command-line argument, or local configuration file.

Mitigation: Prefer a scoped API key, keep local configuration permissions restricted, and avoid sharing command history or logs that include credentials.

Risk: Generated outputs may be saved under the default Downloads location.

Mitigation: Set an explicit output directory when generated media should be stored in a controlled project location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/runway-video-generation-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with bash command examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI Hive video generation tasks, query task JSON, upload user-selected media, and save generated media files locally.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
