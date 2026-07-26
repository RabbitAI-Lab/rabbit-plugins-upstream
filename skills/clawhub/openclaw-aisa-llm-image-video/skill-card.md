## Description: <br>
Generate images and videos with AIsa using Gemini 3 Pro Image for image generation and Qwen Wan 2.6 for video generation through one API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisadocs](https://clawhub.ai/user/aisadocs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creative teams use this skill to call AIsa image and video generation APIs from an agent workflow, including quick-start curl examples and a Python client for local media generation and video task polling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, reference image URLs, and bearer-authenticated requests are sent to AIsa. <br>
Mitigation: Avoid confidential prompts or private image URLs, and use this skill only where sending that data to AIsa is acceptable. <br>
Risk: The skill requires an AISA_API_KEY for authenticated API access. <br>
Mitigation: Use a dedicated, revocable API key and provide it through the environment or command option only when needed. <br>
Risk: Generated downloads can be large and can overwrite files at the selected output path. <br>
Mitigation: Use a dedicated output folder and review the output path before downloading generated media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aisadocs/skills/openclaw-aisa-llm-image-video) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa Gemini GenerateContent API](https://aisa.mintlify.app/api-reference/chat/chat-api/google-gemini-chat.md) <br>
- [AIsa video generation API](https://aisa.mintlify.app/api-reference/aliyun/video/video-generation.md) <br>
- [AIsa video task API](https://aisa.mintlify.app/api-reference/aliyun/video/task.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with bash examples and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated image files and downloaded MP4 files may be saved to local output paths; video generation uses asynchronous task polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
