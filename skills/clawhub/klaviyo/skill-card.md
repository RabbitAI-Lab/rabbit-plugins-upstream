## Description:

Klaviyo API integration with managed OAuth for accessing profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, and webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Klaviyo email marketing, customer data, and workflow integrations through authenticated Maton CLI and API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad write-capable Klaviyo access through Maton can affect campaigns, subscriptions, webhooks, and customer data.

Mitigation: Prefer read-only or least-privilege Klaviyo scopes, pin the intended connection, and require explicit confirmation for every write or send.

Risk: Ambiguous identifiers or accounts could cause destructive changes to the wrong Klaviyo resource.

Mitigation: Verify resource identifiers and account context before deleting connections, changing subscriptions, creating webhooks, or triggering campaigns.

Risk: Klaviyo API responses may contain untrusted external data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and keep credentials out of logs, files, and command lines.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/klaviyo)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Klaviyo API Documentation](https://developers.klaviyo.com)
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Klaviyo connection; default to read and list calls and require explicit confirmation for writes.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
