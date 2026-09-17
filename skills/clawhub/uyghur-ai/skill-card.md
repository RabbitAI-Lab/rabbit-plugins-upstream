## Description:

Uyghur AI helps agents translate between Chinese and Uyghur, answer or write in Uyghur, translate DOCX/PDF files, and perform image OCR translation using a configured API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need Chinese-Uyghur translation, Uyghur-language Q&A or writing assistance, document translation for DOCX/PDF files, or OCR translation for user-provided images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text, documents, and images are sent to the AI Skills remote service and its upstream model provider.

Mitigation: Upload only content needed for the request, get approval before processing sensitive or regulated files, and avoid using the service for data that is not approved for that endpoint.

Risk: The API key could be exposed through chat, code, logs, filenames, or error messages.

Mitigation: Keep UYGHUR_AI_SKILL_API_KEY private, store it only as an environment variable, and do not echo or persist full keys in outputs.

Risk: Changing AI_SKILLS_API_URL can route requests to an untrusted service.

Mitigation: Use the trusted default endpoint unless the operator controls and trusts the replacement URL.

Risk: Translation, OCR, and chat outputs can be incomplete or inaccurate.

Mitigation: Review generated content before relying on it for user-facing, regulated, or high-impact decisions, and fail closed when expected response fields are missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/uyghur-ai)
- [AI Skills homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/DOCUMENT-TRANSLATION.md)
- [Image OCR translation](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/IMAGE-OCR.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown containing translated text, OCR text, chat responses, API request examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UYGHUR_AI_SKILL_API_KEY; document and image workflows upload user-provided files to the AI Skills remote service.]

## Skill Version(s):

1.7.0 (source: server release evidence and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
