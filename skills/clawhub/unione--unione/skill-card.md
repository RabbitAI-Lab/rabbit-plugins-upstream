## Description:

Guides developers in integrating UniOne transactional email through its Web API and SMTP relay, including SDK setup, templates, delivery webhooks, sending domains, and common production pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unione](https://clawhub.ai/user/unione)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build or maintain server-side applications that send transactional email through UniOne. It provides SDK and SMTP setup guidance, API examples, and help with delivery events and account configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign with medium confidence, but one referenced document was only partially inspected.

Mitigation: Review the partially inspected errors reference and confirm the guidance fits the intended UniOne integration before adopting it.

Risk: Exposing an API key in browser or mobile code can compromise the sending account.

Mitigation: Keep the key in server-side secret storage and make UniOne requests from server-side code.

Risk: Accepting webhook events without verifying their signature can allow untrusted delivery updates.

Mitigation: Verify the webhook signature against the raw request body before parsing or processing the event.

## Reference(s):

- [UniOne Web API reference](https://docs.unione.io/en/web-api-ref)
- [UniOne skill release](https://clawhub.ai/unione/skills/unione)
- [Installation and SDK packages](references/installation.md)
- [Sending email](references/sending.md)
- [SMTP setup](references/smtp.md)
- [Delivery webhooks](references/webhooks.md)
- [Sending domains and sandbox](references/domains.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code examples and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
