## Description:

Supports Chinese-Uyghur translation, Uyghur chat, rewriting, summarization, and text-layer translation for DOCX/PDF files through the AI Skills API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate Chinese and Uyghur text, translate extractable DOCX/PDF text layers, and route Uyghur-language chat or writing tasks through a configured AI Skills API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Translations, chat prompts, and DOCX/PDF contents may be sent to ai-skills.open-idea.net or to a configured AI_SKILLS_API_URL endpoint.

Mitigation: Tell users before uploading files or sensitive long text, obtain consent, and avoid sending confidential documents unless the user accepts that service processing.

Risk: The skill requires an API key and could expose credentials if keys are pasted into chat, code, logs, filenames, or error messages.

Mitigation: Use UYGHUR_AI_SKILL_API_KEY from the environment and never display or store the full key in user-facing output or generated artifacts.

Risk: PDF translation only supports files with extractable text layers and does not perform OCR.

Mitigation: Ask users for copyable text or a parseable document when scanned, empty, damaged, or extraction-failing files are provided.

## Reference(s):

- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Interface Routing](references/INTERFACE-ROUTING.md)
- [Text Translation](references/TRANSLATION.md)
- [Chat Completions](references/CHAT-COMPLETIONS.md)
- [Document Translation](references/DOCUMENT-TRANSLATION.md)
- [HTTP Request Examples](references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with translated text, API guidance, and inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return translated text from API responses, chat content, billing header summaries when relevant, or document text translations without preserving original file layout.]

## Skill Version(s):

1.0.0 (source: server release metadata and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
