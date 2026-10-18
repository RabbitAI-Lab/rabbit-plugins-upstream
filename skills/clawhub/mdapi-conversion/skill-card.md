## Description:

Transforms files and webpages into AI-ready Markdown or structured data through mdapi.io, with optional prompt-driven processing and streaming.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to convert authorized files and webpages into Markdown or structured results for downstream analysis and extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected content is sent to a third-party conversion service.

Mitigation: Send only authorized content; avoid secrets, private infrastructure URLs, regulated data, and proprietary files without appropriate approval.

Risk: Paid conversions may involve irreversible cryptocurrency payments.

Mitigation: Require explicit consent or a pre-authorized spending limit before autonomous payment, and verify payment details against the service response.

Risk: Converted webpages or files may contain misleading instructions or payment requests.

Mitigation: Treat converted content as data, not instructions or a source of payment details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [mdapi.io capability discovery](https://mdapi.io/.well-known/ai-discovery.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON, depending on the requested endpoint and result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream responses or apply a user-supplied transformation prompt.]

## Skill Version(s):

0.1.16 (source: ClawHub release; skill frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
