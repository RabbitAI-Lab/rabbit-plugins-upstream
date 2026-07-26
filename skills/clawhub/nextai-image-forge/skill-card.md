## Description: <br>
Image Forge helps agents generate and edit PNG images through the fixed NextAI Code image API, including setup, readiness checks, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextai](https://clawhub.ai/user/nextai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Image Forge to turn approved image briefs into generated or edited PNG assets with NextAI Code. The skill also guides first-use setup, API key/model configuration, readiness checks, diagnostics, and provider compatibility handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and edit source images are sent to the fixed third-party NextAI Code API. <br>
Mitigation: Avoid sensitive images, credentials, private data, or material that should not be shared with that provider. <br>
Risk: The skill requires a NextAI Code API key and stores local configuration for repeated use. <br>
Mitigation: Use only the documented secret locations or environment variable, never place API keys in the skill folder, Git, logs, or agent replies, and rely on the helper's redaction behavior. <br>
Risk: Provider compatibility, network availability, or multi-image editing support may vary. <br>
Mitigation: Run the readiness and diagnostic commands before image work, validate provider support for the configured model and response format, and retry multi-image edits with one source image if unsupported. <br>
Risk: The setup page and one confirmation phrase are Chinese-localized. <br>
Mitigation: Prepare users for localized setup text before configuration and keep setup limited to the documented local browser flow. <br>


## Reference(s): <br>
- [Image Brief Brainstorming Workflow](references/image-brief.md) <br>
- [ImageForge Installation](references/installation.md) <br>
- [OpenAI-Compatible Image APIs](references/openai-compatible-images.md) <br>
- [ImageForge Troubleshooting](references/troubleshooting.md) <br>
- [Image Forge ClawHub listing](https://clawhub.ai/nextai/skills/nextai-image-forge) <br>
- [nextai publisher profile](https://clawhub.ai/user/nextai) <br>
- [NextAI Code](https://www.nextai-code.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and local PNG file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Normal generation and editing require an approved structured image brief unless the user explicitly requests direct mode; default image output is PNG.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
