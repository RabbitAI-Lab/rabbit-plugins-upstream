## Description:

Supports Chinese-Tibetan translation, Tibetan chat and writing, DOCX/PDF translation, and Tibetan image OCR through a hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users invoke this skill when an agent needs to translate between Chinese and Tibetan, answer or draft Tibetan-language content, translate DOCX/PDF documents, or extract and translate text from Tibetan images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, documents, and images submitted for translation or OCR are sent to the hosted ai-skills.open-idea.net service and may incur usage charges.

Mitigation: Send only user-approved content needed for the request and confirm the user is comfortable using the provider before uploading sensitive files.

Risk: The skill depends on a configured API key for authentication.

Mitigation: Keep the key in TIBETAN_AI_SKILL_API_KEY, do not paste full keys into chat, and avoid writing keys into code, logs, filenames, or error messages.

Risk: Network retries for paid requests can produce duplicate work or ambiguous billing if idempotency is mishandled.

Mitigation: Reuse the same Idempotency-Key for retries of the same logical request, create a new key only for a new request, and stop automatic retries when the service reports an indeterminate idempotency state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/tibetan-ai)
- [Publisher profile](https://clawhub.ai/user/youteacher)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/DOCUMENT-TRANSLATION.md)
- [Image OCR translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/IMAGE-OCR.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or plain text with optional shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translated text, OCR source text, document translation summaries, chat responses, retry guidance, and API setup instructions.]

## Skill Version(s):

1.7.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
