## Description: <br>
Complete Venice AI platform skill for text generation, vision and image analysis, web search, X/Twitter search, embeddings, TTS, speech-to-text, image generation, background removal, video creation, music generation, upscaling, and AI editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonisjongithub](https://clawhub.ai/user/jonisjongithub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call Venice AI from Python CLI wrappers for chat, multimodal analysis, embeddings, speech, image, video, music, and editing workflows. It is intended for users who can supply a Venice API key and review what prompts, files, media, and URLs are sent to external services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected prompts, files, images, audio, video, and URLs may be sent to Venice AI or related search providers. <br>
Mitigation: Avoid confidential or regulated data unless the applicable Venice model privacy terms have been reviewed and accepted. <br>
Risk: The skill requires a Venice API key and can create billable API activity. <br>
Mitigation: Use a dedicated API key with spending controls and rotate it if it may have been exposed. <br>
Risk: User-supplied URLs can be fetched for image, video, audio, and web-scraping workflows. <br>
Mitigation: Do not pass internal or sensitive URLs, and use network controls or sandboxing in shared environments. <br>


## Reference(s): <br>
- [Venice AI API Reference](references/api.md) <br>
- [Security Transparency](SECURITY.md) <br>
- [Venice AI](https://venice.ai) <br>
- [Venice AI Documentation](https://docs.venice.ai) <br>
- [Venice API Settings](https://venice.ai/settings/api) <br>
- [ClawHub Skill Page](https://clawhub.ai/jonisjongithub/skills/venice-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, JSON or text API responses, and generated media files at user-specified output paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and VENICE_API_KEY; selected prompts, files, media, and URLs may be sent to Venice AI or related search providers.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
