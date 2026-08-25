## Description:

Tibetan AI helps agents translate between Chinese and Tibetan, handle Tibetan-language chat tasks, and translate text extracted from DOCX/PDF files through the AI Skills API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need Chinese-Tibetan translation, Tibetan question answering or writing assistance, or text-layer translation for DOCX/PDF files. It is suited for agent workflows that can make authenticated calls to the AI Skills API and return translated or generated text to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tibetan/Chinese text and selected DOCX/PDF contents may be sent to the remote AI Skills API.

Mitigation: Confirm user consent before uploading sensitive documents or long private text, and send only the content required for the request.

Risk: The required API key could be exposed through chat, files, logs, or error output.

Mitigation: Read the key from TIBETAN_AI_SKILL_API_KEY and never print, store, or ask the user to paste the full key.

Risk: Retried write requests could create billing or state uncertainty if idempotency is not handled consistently.

Mitigation: Use a stable Idempotency-Key for each logical request, reuse it for retries, and stop automatic retries when the request state is indeterminate.

Risk: Scanned PDFs, damaged files, empty extractions, or incomplete service responses may not produce usable translations.

Mitigation: Report the failure clearly, request copyable text or a text-layer document when needed, and do not fabricate missing translation or chat output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/tibetan-ai)
- [AI Skills API homepage](https://ai-skills.open-idea.net)
- [API Key Configuration](references/API-KEY.md)
- [Interface Routing](references/INTERFACE-ROUTING.md)
- [Text Translation](references/TRANSLATION.md)
- [Chat Completions](references/CHAT-COMPLETIONS.md)
- [Document Translation](references/DOCUMENT-TRANSLATION.md)
- [HTTP Request Examples](references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown, with optional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote API calls require TIBETAN_AI_SKILL_API_KEY; document translation returns translated text and does not preserve original DOCX/PDF layout.]

## Skill Version(s):

1.0.0 (source: server release evidence, package metadata, and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
