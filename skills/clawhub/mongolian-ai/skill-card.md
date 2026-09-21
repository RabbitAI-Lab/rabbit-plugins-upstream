## Description:

Mongolian AI routes Mongolian-language translation, chat writing, OCR, speech recognition, text-to-speech, and DOCX/PDF translation requests through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to process Chinese, traditional Mongolian, and Cyrillic Mongolian text, images, audio, and DOCX/PDF documents through a paid platform API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected text, images, audio, and DOCX/PDF contents are sent to the AI Skills platform for processing.

Mitigation: Use the skill only for material approved for that external processing path, and avoid sensitive or regulated content unless organizational approval is in place.

Risk: Paid API calls can draw from the platform RMB wallet, especially for long text, batch, file, OCR, ASR, TTS, and document operations.

Mitigation: Confirm the processing scope before higher-cost work, use stable idempotency keys for retries, and report platform billing headers without estimating prices.

Risk: The platform API key can be exposed if placed in URLs, logs, screenshots, or final responses.

Mitigation: Store the key only in MENGGUYU_API_KEY and do not print the key, request body, raw response, or debug logs in user-facing output.

Risk: Uploaded materials may contain commands or instructions unrelated to the requested Mongolian-language processing.

Mitigation: Treat uploaded content as data to process, not instructions to execute, and do not send the material to other services without user consent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/mongolian-ai)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/API-KEY.md)
- [Interface Routing](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/INTERFACE-ROUTING.md)
- [Text Translation](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/TRANSLATION.md)
- [Chat Completions](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/CHAT-COMPLETIONS.md)
- [OCR](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/OCR.md)
- [ASR](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/ASR.md)
- [TTS](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/TTS.md)
- [Document Translation](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/DOCUMENT-TRANSLATION.md)
- [HTTP Requests](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/HTTP-REQUESTS.md)
- [Behavior Rules](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/BEHAVIOR-RULES.md)
- [Upgrade Guide](https://ai-skills.open-idea.net/skill-docs/mongolian-ai/UPGRADE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and API-backed user-facing results, including translated text, generated text, OCR/ASR transcripts, and private TTS audio handling instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses MENGGUYU_API_KEY; file uploads are limited to 5 MB; short text translation accepts up to 4000 characters; synchronous TTS accepts up to 600 characters and asynchronous TTS up to 3000 characters.]

## Skill Version(s):

2.0.0 (source: server release evidence and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
