## Description:

beehiiv API integration with managed OAuth for managing newsletter publications, subscriptions, posts, custom fields, segments, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage beehiiv newsletter resources through Maton-managed OAuth, including subscriber, post, segment, tier, and automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated access can reach the connected beehiiv account.

Mitigation: Prefer OAuth, use the narrowest available beehiiv scopes, confirm the exact account and connection before use, and avoid printing or storing credentials.

Risk: The raw API passthrough can create, update, delete, publish, change subscriptions, or trigger automations.

Mitigation: Default to read and list operations, then confirm the target resource, payload, and intended effect before any write or high-impact operation.

## Reference(s):

- [ClawHub beehiiv Skill](https://clawhub.ai/byungkyu/skills/beehiiv)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [beehiiv Developer Documentation](https://developers.beehiiv.com/)
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference)
- [byungkyu Publisher Profile](https://clawhub.ai/user/byungkyu)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and Python or JavaScript SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected beehiiv account.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
