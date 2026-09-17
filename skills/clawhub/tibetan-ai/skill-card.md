## Description:

Provides Tibetan and Chinese translation, Tibetan question answering and writing assistance, DOCX/PDF translation, and Tibetan image OCR through the documented AI Skills service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Tibetan and Chinese translation, Tibetan-language chat or writing tasks, document translation, and image OCR translation through the AI Skills platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User text, DOCX/PDF contents, and images may be sent to the documented AI Skills service and its model backend for processing.

Mitigation: Use the skill only for material approved for that external processing, and avoid confidential or regulated content unless policy allows it.

Risk: The skill requires an API key for the AI Skills platform.

Mitigation: Store TIBETAN_AI_SKILL_API_KEY in environment configuration and keep it out of chats, logs, source files, and error output.

Risk: File and image translation can expose uploaded content to the service.

Mitigation: Upload files or images only when the user explicitly provides and agrees to process them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/tibetan-ai)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/API-KEY.md)
- [Interface Routing](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/INTERFACE-ROUTING.md)
- [Text Translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/TRANSLATION.md)
- [Chat Completions](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/CHAT-COMPLETIONS.md)
- [Document Translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/DOCUMENT-TRANSLATION.md)
- [Image OCR Translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/IMAGE-OCR.md)
- [HTTP Request Examples](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with API request details and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TIBETAN_AI_SKILL_API_KEY; may process user-provided text, DOCX/PDF files, and images through an external service.]

## Skill Version(s):

1.7.0 (source: server release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
