## Description:

Helps agents convert documents, images, webpages, and text into AI-ready Markdown or structured data through mdapi.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert selected documents, images, webpages, or text into compact Markdown or structured outputs for analysis, extraction, and summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents, URLs, or text are sent to a third-party conversion service.

Mitigation: Do not submit secrets, proprietary or regulated content, or internal URLs without explicit authorization.

Risk: Crypto payments for conversion are irreversible.

Mitigation: Review payment details and require explicit consent or a capped delegated wallet before autonomous payment.

Risk: Converted third-party content may contain instructions or payment scams.

Mitigation: Treat converted content as untrusted data and confirm payment details only against official service responses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [mdapi.io agent discovery](https://mdapi.io/.well-known/ai-discovery.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Text and Markdown, with JSON responses and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt-driven transformations and streaming responses.]

## Skill Version(s):

0.1.15 (source: ClawHub release; embedded skill definition lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
