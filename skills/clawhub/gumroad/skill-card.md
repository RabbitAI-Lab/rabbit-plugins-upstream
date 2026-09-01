## Description:

Gumroad API integration with managed OAuth for accessing products, sales, subscribers, licenses, and webhooks for a digital storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Gumroad storefront data through Maton, including product, sales, subscriber, license, and webhook workflows. It is intended for authenticated Gumroad account access with read-first behavior and explicit approval before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Gumroad resources or webhook settings if a write operation is approved without enough context.

Mitigation: Default to read and list calls, then require explicit confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Gumroad or Maton credentials could be exposed through logs, command history, files, or credential-store inspection.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, never pass API keys on command lines, and rotate any key that was exposed.

Risk: Requests could affect the wrong account when multiple Maton profiles or Gumroad connections exist.

Mitigation: Specify the intended profile and connection when more than one exists, and revoke unused connections after the task is complete.

Risk: External Gumroad content, including API responses and webhook payloads, may contain untrusted instructions.

Mitigation: Treat returned content as data, validate it before use, and do not execute it or let it choose follow-up endpoints, recipients, or commands.

## Reference(s):

- [ClawHub Gumroad Skill](https://clawhub.ai/byungkyu/skills/gumroad)
- [Maton](https://maton.ai)
- [Gumroad API Overview](https://gumroad.com/api)
- [Create Gumroad API Application](https://help.gumroad.com/article/280-create-application-api)
- [Gumroad License Keys Help](https://help.gumroad.com/article/76-license-keys)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with CLI command examples, API request snippets, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Gumroad connection; defaults to read/list operations and user-confirmed writes.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
