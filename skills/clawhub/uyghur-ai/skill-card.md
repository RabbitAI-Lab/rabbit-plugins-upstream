## Description:

Uyghur AI helps agents translate between Chinese and Uyghur, answer and write in Uyghur, and translate extractable text from DOCX or PDF documents using the configured AI Skills API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for Chinese-Uyghur translation, Uyghur-language question answering, writing, rewriting, summarization, and DOCX/PDF text-layer translation through the AI Skills service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected text or documents are sent to the remote AI Skills API.

Mitigation: Confirm user consent before uploading files or sensitive long text, and upload only the content needed for the request.

Risk: The skill depends on an API key for authentication.

Mitigation: Keep UYGHUR_AI_SKILL_API_KEY out of chats, logs, code, filenames, and user-visible error details.

Risk: Document translation handles extracted DOCX/PDF text and does not preserve original layout or OCR scanned PDFs.

Mitigation: Tell users that document output is translated extracted text, and request copyable text or a text-layer file when extraction fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/uyghur-ai)
- [AI Skills service homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](artifact/references/API-KEY.md)
- [Interface Routing](artifact/references/INTERFACE-ROUTING.md)
- [Text Translation](artifact/references/TRANSLATION.md)
- [Chat Completions](artifact/references/CHAT-COMPLETIONS.md)
- [Document Translation](artifact/references/DOCUMENT-TRANSLATION.md)
- [HTTP Request Examples](artifact/references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](artifact/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text or Markdown; setup guidance may include shell command blocks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UYGHUR_AI_SKILL_API_KEY and may send selected text or documents to the remote AI Skills API.]

## Skill Version(s):

1.2.0 (source: release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
