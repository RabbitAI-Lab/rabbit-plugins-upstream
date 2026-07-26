## Description: <br>
解析TikTok视频地址，返回该视频的无水印/含水印下载地址、播放地址与封面地址，用于保存带货视频素材或离线分析。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and e-commerce operators use this skill to resolve a specific TikTok video URL into no-watermark or watermarked download links, a playback URL, and cover image URLs for saving promotional video material or offline analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls LinkFox with the user's API key and TikTok URL and consumes credits. <br>
Mitigation: Confirm the user has configured an appropriate LinkFox API key, explain credit consumption before repeated calls, and avoid speculative retries without user approval. <br>
Risk: The skill saves full API responses locally, which can retain TikTok URLs and returned media links. <br>
Mitigation: Tell users where responses are stored and clean the local LinkFox cache or result files when retained data is no longer needed. <br>
Risk: The security review flags external feedback reporting and a fallback install/download path as behavior users should review before installing. <br>
Mitigation: Review the feedback flow and onboarding fallback before use, and avoid automatic feedback reporting unless it is acceptable for the user's data handling requirements. <br>


## Reference(s): <br>
- [EchoTik TikTok 视频下载 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-get-video-download-url) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API results and local JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a TikTok video URL and a LinkFox API key; returned media URLs may expire and download URLs may be absent for restricted videos.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
