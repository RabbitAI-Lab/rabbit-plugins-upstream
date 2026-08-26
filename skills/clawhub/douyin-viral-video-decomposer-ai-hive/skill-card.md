## Description:

把抖音爆款短视频拆解需求转成可审查的中文商业短视频方案、逐镜脚本、生成提示词、AI-HIVE 命令和验收清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, media buyers, directors, and short-video operators use this skill to decompose authorized Douyin viral references into original commerce-video structures, scripts, shot tables, prompts, commands, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste real credentials into chats, logs, screenshots, or shared files.

Mitigation: Use environment variables or the local config flow, keep placeholders in shared examples, and review files and logs before sharing.

Risk: AI-HIVE generation commands can upload media and may create paid asynchronous tasks.

Mitigation: Confirm the selected media, model, routing mode, parameters, and price snapshot before submitting generation commands.

Risk: Short-video decomposition can drift into unauthorized copying, false endorsements, or overly similar recreations.

Mitigation: Use only authorized reference assets and preserve abstract structure while changing people, scenes, wording, shots, visual style, music, logos, and watermarks.

Risk: Commercial video outputs may contain unsupported product, pricing, performance, or platform-success claims.

Mitigation: Require factual sources for claims and avoid promising traffic, sales, search ranking, review approval, or return on investment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/douyin-viral-video-decomposer-ai-hive)
- [AI-HIVE Portal](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON files, upload user-selected media to AI-HIVE, poll asynchronous generation tasks, and download generated media when commands are run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
