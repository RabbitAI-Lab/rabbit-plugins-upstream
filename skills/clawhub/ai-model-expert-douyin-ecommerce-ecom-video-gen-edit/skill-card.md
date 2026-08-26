## Description:

AI大模型专家｜抖音电商 电商视频生成与编辑 helps ecommerce and content teams use AI-HIVE to generate, edit, extend, track, and download short-form product videos from text and optional media references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand product teams, livestream commerce teams, commercial content creators, and agents use this skill to prepare prompts, upload selected media, submit AI-HIVE video generation or editing jobs, poll task status, and retrieve generated product video assets. It supports text-to-video, image-to-video, reference-to-video, video editing, and video extension workflows for ads, product showcases, social commerce, short drama, and related ecommerce content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Implicit invocation can allow an agent to upload media or submit paid AI-HIVE video jobs without a clear user approval step.

Mitigation: Disable implicit invocation or require explicit approval before uploads, job submission, routing changes, and batch generation.

Risk: The workflow stores and uses an AI-HIVE API key for authenticated requests.

Mitigation: Use a dedicated least-privilege API key where available, store it only in the configured local secret file or environment variable, and rotate it if exposed.

Risk: Generated or edited ecommerce videos can contain incorrect product claims, unauthorized brand use, or inappropriate use of third-party reference media.

Mitigation: Require human review of product facts, brand assets, usage rights, platform policy compliance, and final video content before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-douyin-ecommerce-ecom-video-gen-edit)
- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples; runtime commands can submit jobs, print task metadata, and download generated video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may produce AI-HIVE task IDs, media IDs, status output, local output paths, and downloaded MP4/MOV video assets depending on runtime model support.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
