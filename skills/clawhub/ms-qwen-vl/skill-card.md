## Description: <br>
MS-Qwen-VL helps agents analyze user-selected images with ModelScope Qwen3-VL models through an OpenAI-compatible API, supporting image description, OCR, visual question answering, object detection, and chart analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crocketc](https://clawhub.ai/user/crocketc) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and agent users use this skill when they need a coding agent to inspect local or remote images, extract text, answer questions about image content, detect objects, or summarize charts through ModelScope Qwen3-VL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images and prompts selected by the user are sent to ModelScope for processing. <br>
Mitigation: Use the skill only with images and prompts that are approved for ModelScope processing; avoid sensitive screenshots, IDs, invoices, workplace documents, or regulated data unless authorized. <br>
Risk: The skill requires a ModelScope API key. <br>
Mitigation: Store MODELSCOPE_API_KEY in a protected environment variable or scripts/.env file and avoid committing or sharing the key. <br>
Risk: The skill installs Python dependencies for API access, image handling, and environment loading. <br>
Mitigation: Install dependencies in a virtual environment and keep dependency versions patched. <br>


## Reference(s): <br>
- [ModelScope API Guide](references/api-guide.md) <br>
- [ModelScope Vision Models](references/models.md) <br>
- [ModelScope multimodal model catalog](https://modelscope.cn/models?task=image-to-text) <br>
- [ClawHub skill page](https://clawhub.ai/crocketc/skills/ms-qwen-vl) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Plain text analysis, Markdown guidance, Python examples, shell commands, and optional text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local images are encoded for ModelScope API requests; responses are printed to stdout or written to a user-selected output file.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
