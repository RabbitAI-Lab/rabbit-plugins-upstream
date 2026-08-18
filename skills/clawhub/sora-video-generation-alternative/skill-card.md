## Description:

使用 AI Hive Seedance 2.5 将 Sora、OpenAI Sora 或长提示视频概念迁移为世界状态与物理连续性明确的短镜头，覆盖文生、首帧图生、参考素材、视频编辑和延长；不是 OpenAI Sora 接口。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external creators use this skill to turn Sora-style or long-form video concepts into world-state ledgers and AI Hive Seedance 2.5 video generation, editing, repair, or continuation commands. It is suited for short cinematic shots, ad concepts, image-to-video starts, reference-guided motion, and continuity-focused video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference images, source videos, task metadata, and the AI Hive API key are handled by a third-party video service.

Mitigation: Use only media and prompts that are appropriate to share with AI Hive, avoid sensitive or regulated material unless that handling is acceptable, and protect the API key through the documented environment variable or local config flow.

Risk: The skill is a disclosed wrapper for AI Hive Seedance 2.5 and is not connected to OpenAI Sora.

Mitigation: Set user expectations that Sora and OpenAI names are search and migration terms only, then review generated outputs for continuity, rights, and policy suitability before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/sora-video-generation-alternative)
- [AI Hive API root referenced by the skill](https://ai-hive.iclip.cn/api)
- [AI Hive OpenAPI v1 endpoint used by the bundled CLI](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and structured world-state prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI Hive task IDs, status JSON, and local video file paths produced by the bundled CLI.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
