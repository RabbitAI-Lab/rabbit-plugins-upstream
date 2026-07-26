## Description: <br>
Generate images & videos with AIsa. Gemini 3 Pro Image (image) + Qwen Wan 2.6 (video) via one API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to generate images with Gemini 3 Pro Image and create, poll, and optionally download Qwen Wan 2.6 video tasks through the AIsa API using one API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AIsa API credentials are required and could be exposed or overused if shared broadly. <br>
Mitigation: Use a dedicated or revocable AIsa API key and rotate or revoke it when no longer needed. <br>
Risk: Prompts and reference image URLs are sent to the provider and may contain sensitive information. <br>
Mitigation: Avoid sensitive prompts and private reference image URLs unless the provider handling is acceptable for the use case. <br>
Risk: Generated image and video downloads can overwrite local files at the selected output path. <br>
Mitigation: Choose output paths carefully and avoid reusing filenames for files that should be preserved. <br>
Risk: The optional video downloader saves provider-returned URLs without host validation or a maximum file-size limit. <br>
Mitigation: Use --download only for trusted provider responses and review downloaded files before further use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-image-video-models-wan2-6-gemini-3-pro-image-nano-banana) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa API documentation index](https://aisa.mintlify.app/llms.txt) <br>
- [AIsa Gemini GenerateContent documentation](https://aisa.mintlify.app/api-reference/chat/chat-api/google-gemini-chat.md) <br>
- [AIsa video generation documentation](https://aisa.mintlify.app/api-reference/aliyun/video/video-generation.md) <br>
- [AIsa video task polling documentation](https://aisa.mintlify.app/api-reference/aliyun/video/task.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash and Python command examples; JSON command responses; generated image or video files when commands are run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY plus python3 or curl. Image commands can save PNG, JPG, or WebP files; video commands create asynchronous tasks, poll status, and can download MP4 output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
