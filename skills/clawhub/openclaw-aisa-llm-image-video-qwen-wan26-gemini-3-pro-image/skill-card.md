## Description: <br>
Generate images and videos with AIsa using Gemini 3 Pro Image and Qwen Wan 2.6 through one API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisadocs](https://clawhub.ai/user/aisadocs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers, AI agents, content creators, and businesses use this skill to generate images and create, poll, and optionally download AIsa video generation tasks from prompts and reference image URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, reference image URLs, task IDs, and API usage are sent to the AIsa API. <br>
Mitigation: Use AISA_API_KEY from the environment, avoid submitting secrets or private/internal URLs, and install only when AIsa and the publisher are trusted with this data. <br>
Risk: Generated video downloads can write files to local paths selected by the caller. <br>
Mitigation: Use --download only for expected generated media and choose explicit output paths in appropriate directories. <br>
Risk: Media generation can consume paid API quota. <br>
Mitigation: Monitor AIsa usage and quota before running automated or repeated generation workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aisadocs/skills/openclaw-aisa-llm-image-video-qwen-wan26-gemini-3-pro-image) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [AIsa Gemini GenerateContent documentation](https://aisa.mintlify.app/api-reference/chat/chat-api/google-gemini-chat.md) <br>
- [AIsa video generation documentation](https://aisa.mintlify.app/api-reference/aliyun/video/video-generation.md) <br>
- [AIsa video task documentation](https://aisa.mintlify.app/api-reference/aliyun/video/task.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files] <br>
**Output Format:** [Markdown instructions with CLI examples; the Python client emits JSON status and saves generated image or video files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY; optional downloads save generated media to caller-selected local paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
