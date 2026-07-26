## Description: <br>
Analyzes publicly accessible image URLs with a multimodal AI service to produce text descriptions, OCR-style extraction, visual question answering, and product-image analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and e-commerce operators use this skill to analyze image URLs, extract visible text, answer visual questions, and summarize product or marketing imagery. When given a local image path, the skill can upload it to obtain a temporary public URL before analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local images may be uploaded to a public URL before analysis. <br>
Mitigation: Use only images the user is comfortable sending to LinkFox, and avoid screenshots, documents, or other sensitive files unless the user explicitly approves upload. <br>
Risk: Saved response files may contain sensitive extracted text or image-analysis results. <br>
Mitigation: Run the skill from a controlled workspace and delete saved JSON outputs when they are no longer needed. <br>
Risk: A custom LINKFOX_TOOL_GATEWAY can redirect requests and credentials. <br>
Mitigation: Configure LINKFOX_TOOL_GATEWAY only to a trusted endpoint, or leave it unset to use the documented LinkFox gateway. <br>
Risk: Feedback can send user comments or result-quality details to an external service. <br>
Mitigation: Avoid including sensitive user content in feedback and confirm before reporting feedback that contains user-specific details. <br>


## Reference(s): <br>
- [图片识别 API 参考](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-recognize-image) <br>
- [LinkFox API Key Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance plus JSON API responses saved to files and summarized on stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under ./linkfox/<date>/<session>/data; responses over 8 KB are summarized unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
