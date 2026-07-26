## Description: <br>
Generate images and videos with AIsa using Gemini 3 Pro Image for image generation and Qwen Wan 2.6 for video generation through one API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisapay](https://clawhub.ai/user/aisapay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and content workflow builders use this skill to generate images, create video generation tasks, poll video status, and download completed media through the AIsa API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, referenced image URLs, task IDs, and the AISA_API_KEY are sent to or used with the AIsa API. <br>
Mitigation: Use this skill only with trusted AIsa accounts, avoid submitting secrets or private media references, and keep API keys out of logs and committed files. <br>
Risk: Generated media can be saved or downloaded to local paths and may overwrite existing files when explicit output paths are reused. <br>
Mitigation: Choose output paths deliberately and review generated files before sharing or using them in downstream workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aisapay/skills/aisa-media-gen) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa API llms.txt](https://aisa.mintlify.app/llms.txt) <br>
- [Gemini GenerateContent through AIsa](https://aisa.mintlify.app/api-reference/chat/chat-api/google-gemini-chat.md) <br>
- [AIsa video generation](https://aisa.mintlify.app/api-reference/aliyun/video/video-generation.md) <br>
- [AIsa video task status](https://aisa.mintlify.app/api-reference/aliyun/video/task.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands, curl examples, Python CLI commands, JSON API responses, and generated media files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, curl, and AISA_API_KEY; image output may be saved as png, jpg, or webp, and video output may be downloaded as mp4.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
