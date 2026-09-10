## Description:

Provides Maton CLI and SDK guidance for using managed OAuth to call the Kit API for subscribers, forms, tags, sequences, broadcasts, custom fields, purchases, email templates, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a Kit account through Maton, inspect email marketing resources, and perform approved subscriber, tag, sequence, broadcast, custom field, purchase, email template, and webhook operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Kit API passthrough can expose more account capability than the narrower manifest description suggests.

Mitigation: Install only when broad Kit API reach is acceptable, use OAuth with the narrowest available scopes, and confirm the exact account and connection before use.

Risk: Write operations, webhook changes, and purchase-data access can create external side effects or expose sensitive business data.

Mitigation: Default to read/list calls, require explicit approval for every write or webhook operation, and verify target resource identifiers and payloads before execution.

Risk: Unpinned Maton CLI or SDK versions may change gateway behavior over time.

Mitigation: Prefer pinned or locked Maton CLI and SDK versions where the deployment environment supports version control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/kit)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kit API Overview](https://developers.kit.com/api-reference/overview)
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers)
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags)
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emphasizes read-first workflows, explicit approval for writes, OAuth credential handling, and connection selection.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
