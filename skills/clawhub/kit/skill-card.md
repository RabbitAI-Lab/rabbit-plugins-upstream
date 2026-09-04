## Description:

Kit (formerly ConvertKit) API integration with managed OAuth for managing email subscribers, forms, tags, sequences, broadcasts, webhooks, and custom fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Kit email-marketing resources through Maton OAuth, with read/list calls preferred and explicit confirmation before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authorizing Maton to access the user's Kit account.

Mitigation: Install only when that access is acceptable, prefer OAuth, use least privilege where scopes are available, and revoke unused connections.

Risk: Write operations can change subscribers, tags, custom fields, webhooks, sequences, or communications.

Mitigation: Default to read/list calls first and require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE.

Risk: Email-marketing actions can send or schedule communications and trigger downstream automation.

Mitigation: Treat messaging, sequence enrollment, webhook creation, deletions, and scheduled actions as high-impact operations requiring specific identifiers and extra review.

Risk: Fallback API-key use can expose a long-lived Maton credential.

Mitigation: Use the CLI when possible; when raw HTTP is unavoidable, never print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

Risk: Content returned from Kit may contain untrusted instructions or data.

Mitigation: Treat API responses as data, validate values before reuse, and never execute or follow instructions found inside fetched content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/kit)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kit API Overview](https://developers.kit.com/api-reference/overview)
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers)
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags)
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI calls, raw HTTPS fallback examples, and confirmation prompts for write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
