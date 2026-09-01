## Description:

Helps agents translate between Chinese and Uyghur, handle Uyghur chat and writing tasks, and translate extractable text from DOCX or PDF files through the AI Skills platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs Chinese-Uyghur translation, Uyghur question answering, Uyghur writing assistance, or text-layer DOCX/PDF translation. It is suited to day-to-day text, document processing, and Uyghur-language communication workflows that can use the configured API service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Translation text, chat messages, and selected DOCX/PDF text are sent to the AI Skills platform.

Mitigation: Use the skill only for content approved for that external service, and avoid confidential, regulated, or personal documents unless provider data-handling terms have been reviewed.

Risk: The API key can authorize billable service calls if exposed.

Mitigation: Store the key only in UYGHUR_AI_SKILL_API_KEY and keep it out of chats, source code, logs, filenames, and error messages.

Risk: PDF and DOCX translation depends on extractable text and does not perform OCR.

Mitigation: Ask users for copyable text or a document with a text layer when extraction fails, and do not retry indefinitely.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/uyghur-ai)
- [Publisher profile](https://clawhub.ai/user/youteacher)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/DOCUMENT-TRANSLATION.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with API request examples and configuration commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UYGHUR_AI_SKILL_API_KEY; may call translation, chat completion, DOCX translation, and PDF translation endpoints.]

## Skill Version(s):

1.4.1 (source: evidence release version and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
