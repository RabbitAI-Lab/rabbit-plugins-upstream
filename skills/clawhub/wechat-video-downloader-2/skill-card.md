## Description: <br>
一键解析视频号视频的真实下载地址。粘贴视频号分享链接，即可获取视频标题、封面图和高清无水印下载地址。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, operations staff, and video editors use this skill to resolve WeChat Channels share links into video metadata, cover images, and temporary direct download URLs for authorized saving, archiving, or editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends WeChat share links and the REDFOX_API_KEY to a third-party RedFox API. <br>
Mitigation: Use a revocable or scoped API key when possible, avoid private or sensitive links, and install only if sending these inputs to RedFox is acceptable. <br>
Risk: The skill promotes watermark-free and competitor-video downloading, which may be inappropriate without authorization. <br>
Mitigation: Use it only for videos the user owns or is authorized to download, reuse, or archive. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/redfox-data/redfox-community/tree/main/skills/wechat-video-downloader) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-video-downloader-2) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Workflow](references/workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, API Calls, guidance] <br>
**Output Format:** [Markdown summary with links to the video title, cover image, and direct download URL; the helper script emits JSON for agent formatting.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Download URLs are described as temporary and should be saved promptly.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
