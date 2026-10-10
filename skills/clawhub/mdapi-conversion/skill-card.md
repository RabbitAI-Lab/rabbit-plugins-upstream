## Description:

Converts webpages, documents, images, and text into AI-ready Markdown or structured data using mdapi.io.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users convert public webpages, documents, images, or authorized text into Markdown or structured results for downstream analysis and extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected content is sent to mdapi.io, and its caching and retention statements conflict.

Mitigation: Do not send secrets, regulated data, private infrastructure URLs, or proprietary material without authorization and acceptance of uncertain retention.

Risk: Crypto payments are irreversible.

Mitigation: Require explicit confirmation before payment and verify payment details against the service response.

Risk: Paid access tokens and payment information could be exposed.

Mitigation: Keep tokens in a secret store and avoid exposing them in URLs, logs, or responses.

## Reference(s):

- [ClawHub mdapi-conversion release](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)

## Skill Output:

**Output Type(s):** [Markdown, Structured data, Guidance]

**Output Format:** [Markdown text or JSON; optional prompt-driven results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Streaming is available for long responses.]

## Skill Version(s):

0.1.14 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
