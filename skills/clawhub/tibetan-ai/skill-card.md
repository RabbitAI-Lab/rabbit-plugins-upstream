## Description:

Tibetan AI helps agents translate between Chinese and Tibetan, answer or draft Tibetan-language content, translate DOCX/PDF files, and OCR/translate Tibetan or Chinese images using the configured API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Tibetan/Chinese translation, Tibetan-language Q&A or writing, DOCX/PDF translation, and image OCR translation requests through the AI Skills API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and user-provided documents or images may be sent to an arbitrary host if AI_SKILLS_API_URL is overridden or inherited.

Mitigation: Use the default trusted service URL, avoid untrusted AI_SKILLS_API_URL values, and rotate the API key if it may have been used with a suspect base URL.

Risk: Document, PDF, and image workflows upload user content to the service for processing.

Mitigation: Upload only user-provided files after consent, avoid logging file bytes or Base64 data, and keep needed OCR or translation results from the first response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/tibetan-ai)
- [AI Skills platform homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/API-KEY.md)
- [Interface routing](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/INTERFACE-ROUTING.md)
- [Text translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/TRANSLATION.md)
- [Chat completions](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/CHAT-COMPLETIONS.md)
- [Document translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/DOCUMENT-TRANSLATION.md)
- [Image OCR translation](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/IMAGE-OCR.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional shell commands and API request guidance; service calls return structured JSON fields such as data.tgtText or choices[0].message.content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TIBETAN_AI_SKILL_API_KEY; document and image workflows use multipart uploads and idempotency keys.]

## Skill Version(s):

1.7.0 (source: server release evidence and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
