## Description: <br>
Tencent VOD Intl. helps agents generate Tencent Cloud VOD Python commands for uploads, media processing, media queries, AIGC image and video workflows, chat, token usage, search, image processing, sub-app management, and task checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-mpaas-skills](https://clawhub.ai/user/tencent-mpaas-skills) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to turn Tencent Cloud VOD requests into concrete Python commands for upload, processing, AIGC generation, search, and status-query workflows. It is intended for external agent use where Tencent Cloud credentials and VOD billing are already authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can call billable Tencent Cloud VOD processing and AIGC services. <br>
Mitigation: Inspect generated commands, use --dry-run for costly work, require explicit confirmation before submission, and monitor Tencent Cloud billing controls. <br>
Risk: The skill may read or update local credential and history files such as .env files, mem/elements.json, and stored AIGC tokens. <br>
Mitigation: Use an isolated virtual environment, avoid exposing secrets in prompts or session context, and delete or protect local token and history files when they are no longer needed. <br>
Risk: The skill may install or upgrade Python packages before running Tencent VOD scripts. <br>
Mitigation: Review scripts and requirements before installation and run the skill in a controlled environment. <br>


## Reference(s): <br>
- [Tencent VOD Intl. ClawHub Page](https://clawhub.ai/tencent-mpaas-skills/skills/tencent-vod-intl) <br>
- [VOD Upload Reference](references/vod_upload.md) <br>
- [VOD Pull Upload Reference](references/vod_pull_upload.md) <br>
- [VOD Media Processing Reference](references/vod_process_media.md) <br>
- [VOD Image Processing Reference](references/vod_process_image.md) <br>
- [VOD Media Details Reference](references/vod_describe_media.md) <br>
- [VOD Task Query Reference](references/vod_describe_task.md) <br>
- [VOD AIGC Image Reference](references/vod_aigc_image.md) <br>
- [VOD AIGC Video Reference](references/vod_aigc_video.md) <br>
- [VOD AIGC Chat Reference](references/vod_aigc_chat.md) <br>
- [Tencent Cloud VOD Pricing](https://cloud.tencent.com/document/product/266/2838) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Configuration guidance] <br>
**Output Format:** [Plain shell commands with Markdown hyperlinks for returned media links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use python3 scripts/<script-name>.py form and may include --dry-run for previewing costly operations.] <br>

## Skill Version(s): <br>
1.1.2 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
