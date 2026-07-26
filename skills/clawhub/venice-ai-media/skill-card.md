## Description: <br>
Generate, edit, and upscale images; create videos from images via Venice AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nhannah](https://clawhub.ai/user/nhannah) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and creators use this skill to generate images, edit or upscale existing images, and create videos from images through Venice AI APIs. It is suited for agent workflows that need media outputs plus setup and troubleshooting guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, images, URLs, audio, and generated media may be sent to Venice AI as a third-party API provider. <br>
Mitigation: Do not submit sensitive photos, documents, private URLs, audio, or confidential prompt text unless Venice AI's policies are acceptable for the intended use. <br>
Risk: A long or high-resolution video job can create unexpected API costs. <br>
Mitigation: Use the documented --quote option before video generation and choose duration, model, and resolution deliberately. <br>
Risk: The Venice API key can authorize paid media generation if exposed. <br>
Mitigation: Use a dedicated revocable key, prefer VENICE_API_KEY environment configuration, and protect any local Clawdbot configuration file that stores the key. <br>
Risk: Safe mode is documented as disabled by default for image generation. <br>
Mitigation: Enable --safe-mode when content filtering is required for the workflow or audience. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nhannah/skills/venice-ai-media) <br>
- [Venice AI](https://venice.ai) <br>
- [Venice API Key Settings](https://venice.ai/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, configuration, guidance] <br>
**Output Format:** [Media files with terminal status text and MEDIA path lines; Markdown usage guidance with inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.10+ and VENICE_API_KEY; generated media is written to local output paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; changelog describes 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
