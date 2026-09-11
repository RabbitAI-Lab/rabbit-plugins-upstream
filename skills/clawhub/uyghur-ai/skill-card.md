## Description:

Supports Chinese-Uyghur translation, Uyghur question answering and writing, and DOCX/PDF text-layer translation through the AI Skills service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate between Chinese and Uyghur, answer or draft Uyghur-language content, and translate extractable DOCX/PDF text. It is intended for requests where the user provides text or supported documents and has configured the required API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested text, prompts, or document text layers are sent to the AI Skills service.

Mitigation: Avoid confidential documents unless approved, and upload only the content needed for the translation or chat request.

Risk: The required API key could be exposed if pasted into conversations, code, logs, filenames, or error output.

Mitigation: Store the key only in the intended OpenClaw environment configuration and do not ask users to share the full key.

Risk: DOCX/PDF translation only handles extractable text layers and does not perform OCR.

Mitigation: Ask for copyable text or a parseable document when scanned, damaged, empty, or image-only files cannot be extracted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/uyghur-ai)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/DOCUMENT-TRANSLATION.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces translated text, chat responses, and setup/API guidance; document translation returns extracted translated text rather than a reformatted replacement file.]

## Skill Version(s):

1.5.0 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
