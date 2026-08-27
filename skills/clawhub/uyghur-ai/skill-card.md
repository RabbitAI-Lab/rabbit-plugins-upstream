## Description:

Uyghur AI helps agents translate between Chinese and Uyghur, support Uyghur Q&A and writing, and translate text-layer DOCX/PDF content using a configured API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Chinese-Uyghur translation, Uyghur-language chat, text rewriting, content creation, and text-layer document translation requests through the AI Skills service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Translation requests and uploaded DOCX/PDF files are processed by an external AI Skills service using the configured API key.

Mitigation: Avoid sending confidential, regulated, or third-party documents unless approved and acceptable for that service to process.

Risk: API keys can be exposed if pasted into chat, code, logs, filenames, or error messages.

Mitigation: Configure UYGHUR_AI_SKILL_API_KEY as an environment variable and do not echo complete keys or raw diagnostic payloads.

Risk: Scanned PDFs and files without extractable text are unsupported and may fail document extraction.

Mitigation: Use PDFs with a text layer, DOCX files, or copyable plain text; do not retry extraction failures indefinitely.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/uyghur-ai)
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

**Output Format:** [Markdown guidance with API routes, request examples, and response-handling rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UYGHUR_AI_SKILL_API_KEY; document translation accepts DOCX/PDF files up to 5 MB and returns extracted translated text rather than a newly formatted document.]

## Skill Version(s):

1.3.0 (source: server release evidence and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
