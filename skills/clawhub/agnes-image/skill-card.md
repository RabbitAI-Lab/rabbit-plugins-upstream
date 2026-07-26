## Description: <br>
Generate and edit high-quality images from text or existing images, with support for multi-image composition, style transfer, and flexible resolutions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lutongsuo](https://clawhub.ai/user/lutongsuo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to generate, edit, and compose images through the Agnes Image 2.0 Flash API from text prompts, input image URLs, and batch prompt files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and input image URLs are sent to the Agnes hosted API. <br>
Mitigation: Avoid secrets, private internal URLs, confidential image descriptions, and sensitive source images unless the provider's data handling is approved for that use. <br>
Risk: Running generation scripts, especially batch generation, can consume paid API quota or incur usage costs. <br>
Mitigation: Test with small prompt sets first, monitor API usage, and require an explicitly configured API key before execution. <br>
Risk: Image-to-image and multi-image workflows require publicly reachable HTTPS image URLs. <br>
Mitigation: Use only approved public assets or access-controlled URLs that are safe to expose to the image-generation provider. <br>


## Reference(s): <br>
- [Agnes Image 2.0 Flash on ClawHub](https://clawhub.ai/lutongsuo/skills/agnes-image) <br>
- [API Documentation](references/API.md) <br>
- [Prompt Guide](references/PROMPT_GUIDE.md) <br>
- [Examples](references/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash command examples; runtime scripts return generated image URLs or save image/Base64 files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Agnes API key and public HTTPS input image URLs for image-to-image or multi-image workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
