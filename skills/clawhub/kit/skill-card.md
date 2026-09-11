## Description:

Kit (formerly ConvertKit) API integration with managed OAuth for managing subscribers, forms, tags, sequences, broadcasts, custom fields, purchase records, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Kit email marketing resources through Maton-authenticated API calls, with read-first behavior and confirmation before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change email marketing account data through the connected Kit account.

Mitigation: Prefer read and list calls first, choose the narrowest Kit scopes available, and confirm every write, deletion, connection change, or webhook creation with the user.

Risk: API keys and provider-issued tokens can expose long-lived account access if printed, logged, or persisted.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, and avoid exporting or printing tokens.

Risk: Subscriber and purchase endpoints may return personal data and order details.

Mitigation: Retrieve only data needed for the current task and extract specific fields instead of dumping full responses into logs or files.

Risk: Broadcasts, sequence enrollment, tag changes, and webhooks can trigger outbound messaging or persistent data forwarding.

Mitigation: Confirm the exact target resource, payload, audience, destination host, and intended effect before executing high-impact operations.

## Reference(s):

- [Kit Skill Page](https://clawhub.ai/byungkyu/skills/kit)
- [Maton Homepage](https://maton.ai)
- [Kit API Overview](https://developers.kit.com/api-reference/overview)
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers)
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags)
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may include subscriber, purchase, and email marketing account data; users are guided to extract only needed fields.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
