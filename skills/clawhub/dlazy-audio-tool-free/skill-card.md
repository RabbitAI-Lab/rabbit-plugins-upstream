## Description: <br>
音频生成工具免费版 helps personal creators use the dlazy CLI to generate text-to-speech audio and basic sound effects from text prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and agent users use this skill to prepare dlazy CLI commands, API key setup guidance, and generation parameters for multilingual narration, audiobook chapters, social media audio, and simple sound effects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the external dlazy CLI and sends user prompts to dlazy's cloud audio service. <br>
Mitigation: Use it only when cloud processing is acceptable for the text being converted to speech or sound effects. <br>
Risk: The skill requires a dlazy API key for authentication. <br>
Mitigation: Keep the key private, prefer environment variables or a protected config file, and rotate the key if it may have been exposed. <br>
Risk: The free edition is scoped to TTS and basic sound-effect generation, not broad media editing or professional post-production. <br>
Mitigation: Confirm the requested task matches the documented free-edition models and route unsupported work to another tool. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/thcjp/skills/dlazy-audio-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, Python, text, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance is intended for TTS and basic sound-effect generation through the external dlazy CLI and cloud audio service.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
