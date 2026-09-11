## Description:

tibetan-ai helps agents perform Chinese-Tibetan translation, Tibetan question answering and writing, and text-layer translation for DOCX and PDF files through the AI Skills service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to translate between Chinese and Tibetan, answer or draft Tibetan-language content, or extract and translate the text layer from supported DOCX and PDF files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested text or selected DOCX/PDF contents are sent to the AI Skills service for processing.

Mitigation: Get user consent before uploading files or sensitive text, and avoid submitting confidential, regulated, or secret material unless authorized.

Risk: The API key authorizes calls to the remote service.

Mitigation: Store the key only in TIBETAN_AI_SKILL_API_KEY and do not paste it into chats, source files, logs, filenames, or error messages.

Risk: Document translation depends on extractable DOCX or PDF text and does not perform OCR or preserve the original document layout.

Mitigation: For scanned, damaged, empty, or image-only files, ask for copyable text or a document with a text layer instead of retrying indefinitely.

## Reference(s):

- [AI Skills platform](https://ai-skills.open-idea.net)
- [ClawHub skill page](https://clawhub.ai/youteacher/skills/tibetan-ai)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/DOCUMENT-TRANSLATION.md)
- [HTTP requests](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text, with shell command examples and API response content when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Translation responses use translated text from data.tgtText; chat responses use choices[0].message.content.]

## Skill Version(s):

1.5.0 (source: release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
