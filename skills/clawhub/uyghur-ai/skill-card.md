## Description:

Uyghur AI helps agents handle Chinese and Uyghur translation, Uyghur-language chat and writing, DOCX/PDF translation, and image OCR translation through the AI Skills service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to translate between Chinese and Uyghur, answer or write in Uyghur, extract and translate text from images, or translate DOCX and PDF documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional API endpoint override can redirect API keys and submitted text, documents, or images to an untrusted destination.

Mitigation: Use the default AI Skills endpoint unless you fully control and trust the replacement endpoint.

Risk: Submitted text, documents, and images are processed by the AI Skills service and its upstream model provider.

Mitigation: Use the skill only for content that is approved for that data-handling path, and avoid sensitive or regulated documents unless approval is in place.

Risk: API keys could be exposed if users paste them into chat, code, logs, filenames, or error messages.

Mitigation: Store UYGHUR_AI_SKILL_API_KEY as an environment variable and never echo the full key in responses, logs, files, or diagnostics.

Risk: Document and image workflows upload user-provided files for OCR or translation.

Mitigation: Upload only the content needed for the request and obtain user consent before sending files or sensitive long text.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/uyghur-ai)
- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/API-KEY.md)
- [Interface Routing](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/INTERFACE-ROUTING.md)
- [Text Translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/TRANSLATION.md)
- [Chat Completions](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/CHAT-COMPLETIONS.md)
- [Document Translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/DOCUMENT-TRANSLATION.md)
- [Image OCR Translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/IMAGE-OCR.md)
- [HTTP Request Examples](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/HTTP-REQUESTS.md)
- [Behavior, Error, and Retry Rules](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with translated text, OCR text, API usage guidance, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UYGHUR_AI_SKILL_API_KEY; document and image uploads should only occur with user consent.]

## Skill Version(s):

1.7.0 (source: server release and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
