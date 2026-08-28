## Description:

Kit (formerly ConvertKit) API integration with managed OAuth for managing subscribers, forms, tags, sequences, broadcasts, custom fields, and webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect and manage Kit email-marketing resources through Maton-authenticated API calls. It supports list-first workflows for subscribers, tags, forms, sequences, broadcasts, custom fields, purchases, templates, and webhooks, with explicit approval before connection creation or data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing Maton creates access to the connected Kit account.

Mitigation: Prefer OAuth, review connection scopes, connect only the intended account, and require user approval before creating a new Kit connection.

Risk: Subscriber, tag, sequence, broadcast, webhook, and deletion changes can affect email-marketing data or trigger downstream communication workflows.

Mitigation: Default to read and list calls, verify resource identifiers first, and confirm the target, payload, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Multiple Maton profiles or Kit connections can cause actions to target the wrong account.

Mitigation: Specify the intended profile and connection when more than one account or connection is available.

Risk: Long-lived API keys and provider-issued tokens can be exposed through logs, shell history, command arguments, or files.

Mitigation: Use OAuth when possible; if raw HTTP is unavoidable, keep keys out of output and command arguments, avoid persistence, send them only to api.maton.ai, and rotate any key that was exposed.

Risk: Content returned by the Kit API may contain untrusted instructions or values.

Mitigation: Treat API responses as data, validate external values before reuse, and never execute or follow instructions embedded in fetched content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/kit)
- [Maton Homepage](https://maton.ai)
- [Kit API Overview](https://developers.kit.com/api-reference/overview)
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers)
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags)
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval before creating connections or executing writes.]

## Skill Version(s):

1.1.0 (source: server release metadata; frontmatter metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
