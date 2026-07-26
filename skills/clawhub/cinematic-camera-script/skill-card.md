## Description: <br>
生成电影感运镜短视频脚本的技能。输出含逐秒分镜拆解、运镜参数和BGM卡点节奏的完整脚本及一键视频提示词，支持上传图片或文字描述生成，可直接用于实拍或AI视频生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[if530770](https://clawhub.ai/user/if530770) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, photographers, directors, and AI video users use this skill to turn images or natural-language scene descriptions into cinematic short-video scripts, second-by-second storyboard guidance, camera movement parameters, BGM beat-sync notes, and AI video prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional RedFox/Seedance video generation can send prompt or image-derived content to an external service and may incur costs. <br>
Mitigation: Confirm what content will be sent and what charges may apply before invoking API-backed video generation. <br>
Risk: The skill uses REDFOX_API_KEY for optional video generation. <br>
Mitigation: Use environment variables or safer secret storage, and do not print, paste, hard-code, log, or store API keys in plaintext. <br>
Risk: Bundled templates contain default visual and character assumptions. <br>
Mitigation: Review and customize templates when neutral, brand-specific, or audience-specific character demographics are required. <br>


## Reference(s): <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Camera Movements](references/camera-movements.md) <br>
- [Shot Composition](references/shot-composition.md) <br>
- [BGM Sync](references/bgm-sync.md) <br>
- [AI Prompts](references/ai-prompts.md) <br>
- [RedFoxHub API Keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown scripts and prompts with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include second-by-second storyboard sections, camera guidance, BGM timing notes, complete AI video prompts, and optional RedFox/Seedance API setup guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
