## Description:

Tibetan AI helps agents translate between Chinese and Tibetan, handle Tibetan question answering and writing tasks, and translate DOCX or text-layer PDF content through the AI Skills service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs Chinese-Tibetan translation, Tibetan-language Q&A, Tibetan writing support, or extraction-based DOCX/PDF text translation. The skill requires a configured TIBETAN_AI_SKILL_API_KEY and sends requested content to the AI Skills service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested text or uploaded documents are sent to an external AI Skills service for processing.

Mitigation: Use the skill only for content approved for that provider, and avoid confidential or regulated documents unless policy allows it.

Risk: The skill depends on a user-provided API key.

Mitigation: Configure the key through TIBETAN_AI_SKILL_API_KEY and keep it out of chats, logs, source files, filenames, and error messages.

Risk: Document translation depends on successful text extraction and does not perform OCR.

Mitigation: Use DOCX files or PDFs with extractable text layers; ask for copyable text or a parseable file when extraction fails.

## Reference(s):

- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Interface Routing](references/INTERFACE-ROUTING.md)
- [Text Translation](references/TRANSLATION.md)
- [Chat Completions](references/CHAT-COMPLETIONS.md)
- [Document Translation](references/DOCUMENT-TRANSLATION.md)
- [HTTP Requests](references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples and text translation or chat output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return translated text, chat content, or document-extracted translation text; PDF input must have a text layer and DOCX/PDF uploads are limited to 5 MB.]

## Skill Version(s):

1.3.0 (source: server release metadata and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
