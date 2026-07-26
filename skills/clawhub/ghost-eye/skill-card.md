## Description: <br>
Ghost Eye lets a text-only LLM analyze images by sending them to an OpenAI-compatible vision model and returning OCR text plus a visual summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hunter-crk](https://clawhub.ai/user/hunter-crk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Ghost Eye to add image OCR and scene summarization to text-only LLM workflows through either automatic multimodal preprocessing or explicit tool calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images may be sent to a configured third-party vision API, including in automatic preprocessing mode. <br>
Mitigation: Deploy only where users and operators accept that image data is sent to the selected provider; use explicit tool-call mode for sensitive workflows. <br>
Risk: Extracted OCR and visual-summary text may be cached locally for the configured cache TTL. <br>
Mitigation: Disable caching with NEXN2_CACHE_ENABLE=false for sensitive data, or purge the cache regularly and shorten NEXN2_CACHE_TTL_DAYS. <br>
Risk: Silent automatic preprocessing can analyze private screenshots, IDs, medical records, legal documents, or business documents without clear end-user consent. <br>
Mitigation: Avoid auto-preprocess for private or regulated content and require an explicit user action before image analysis. <br>


## Reference(s): <br>
- [Ghost Eye ClawHub Skill Page](https://clawhub.ai/hunter-crk/skills/ghost-eye) <br>
- [multimodal-config.md](artifact/references/multimodal-config.md) <br>
- [SiliconFlow OpenAI-compatible API endpoint](https://api.siliconflow.cn/v1) <br>
- [OpenRouter OpenAI-compatible API endpoint](https://openrouter.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON result containing plain text or Markdown OCR and visual-summary content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires NEXN2_API_KEY; accepts image path, image URL, or base64 image input; cache entries may persist extracted text for the configured TTL.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
