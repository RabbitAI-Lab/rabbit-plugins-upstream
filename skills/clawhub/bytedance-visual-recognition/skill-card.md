## Description:

ByteDance Visual Recognition uses Doubao-Seed and Zhipu GLM multimodal models to recognize images and videos, produce text or code, support batch processing and follow-up prompts, and maintain local cache and history files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[etmnb](https://clawhub.ai/user/etmnb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to send selected images or videos to Doubao or Zhipu GLM cloud vision APIs for recognition, OCR-style text extraction, UI-to-code conversion, batch analysis, and follow-up questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, videos, and prompts are uploaded to Doubao or Zhipu cloud APIs.

Mitigation: Install only when cloud processing is acceptable for the media being analyzed, and avoid sending sensitive or restricted files.

Risk: API keys are stored in plaintext config.json.

Mitigation: Use the skill on non-shared machines and review or clear config.json when credentials should no longer remain on disk.

Risk: The skill persists cached media, recognition history, and follow-up context in Temp/, vision_history.json, and .last_response.

Mitigation: Review and clear these files when local retention is not desired.

Risk: Broad image-to-text trigger phrases could invoke the skill unexpectedly.

Mitigation: Review prompts before execution and use explicit phrasing when intending to upload media to cloud APIs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/etmnb/skills/bytedance-visual-recognition)
- [Publisher Profile](https://clawhub.ai/user/etmnb)
- [Volcengine Doubao Documentation](https://www.volcengine.com/docs/82379/1569618)
- [Volcengine Ark Console](https://console.volcengine.com/ark)
- [Zhipu Open Platform](https://open.bigmodel.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional code snippets and local JSON state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce recognition history, follow-up context, cached media copies, and generated config.json in the skill directory.]

## Skill Version(s):

3.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
