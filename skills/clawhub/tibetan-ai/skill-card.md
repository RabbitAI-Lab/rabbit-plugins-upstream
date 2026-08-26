## Description:

Supports Chinese-Tibetan translation, Tibetan question answering and writing, and DOCX/PDF text-layer translation when TIBETAN_AI_SKILL_API_KEY is configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate Chinese and Tibetan text, process DOCX or text-layer PDF translation requests, and ask for Tibetan-language answers, rewrites, summaries, or creative writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User text and uploaded DOCX/PDF files are sent to the AI Skills platform for processing.

Mitigation: Tell users before uploading files or sensitive long text, obtain consent, and avoid sensitive or regulated content unless third-party processing is acceptable.

Risk: API key exposure could allow unauthorized use of the configured Tibetan AI service.

Mitigation: Keep TIBETAN_AI_SKILL_API_KEY in environment configuration and do not place full keys in chats, logs, code, filenames, or error messages.

Risk: Paid write requests can become ambiguous during retries or partial failures.

Mitigation: Use a stable Idempotency-Key for each logical request, reuse it for retries, and stop automatic retries when idempotency or billing state is indeterminate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/tibetan-ai)
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

**Output Format:** [Plain text or Markdown with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TIBETAN_AI_SKILL_API_KEY; document translation returns extracted text translation and does not preserve source document layout.]

## Skill Version(s):

1.2.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
