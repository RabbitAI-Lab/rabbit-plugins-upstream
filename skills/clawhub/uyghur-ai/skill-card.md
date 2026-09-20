## Description:

使用场景: 用户要求处理维吾尔语或维文，包括汉维翻译、维吾尔语问答写作、DOCX/PDF 翻译或维文图片 OCR。

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to handle Uyghur and Chinese language tasks, including bidirectional text translation, Uyghur question answering and writing, DOCX/PDF translation, and image OCR translation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Translation text, DOCX/PDF files, and images are sent to the AI Skills cloud service and its model provider.

Mitigation: Use the skill only for material your organization has approved for external processing, and avoid confidential, regulated, or highly sensitive content unless that processing is authorized.

Risk: The API key controls access and billing for the skill.

Mitigation: Store UYGHUR_AI_SKILL_API_KEY as a protected environment variable, do not ask users to paste full keys into chat, and do not write keys into code, logs, filenames, or error messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/uyghur-ai)
- [AI Skills platform homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/DOCUMENT-TRANSLATION.md)
- [Image OCR translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/IMAGE-OCR.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses with API request guidance and shell commands where setup or direct calls are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses UYGHUR_AI_SKILL_API_KEY for authenticated calls to the AI Skills cloud service; document and image tasks may upload user-provided files.]

## Skill Version(s):

1.7.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
