## Description:

Klaviyo API integration with managed OAuth for accessing profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, and webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and manage Klaviyo email marketing, customer data, campaign, flow, event, catalog, and webhook resources through a Maton-authenticated API workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize agent access to a connected Klaviyo account through Maton.

Mitigation: Install it only when that access is intended, review requested OAuth scopes, prefer read-only scopes, and revoke unused Maton/Klaviyo connections when finished.

Risk: Write operations, campaign sending, automation, webhook changes, or deletions can affect customers, data, cost, or sender reputation.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user confirmation for every write or campaign-sending action.

Risk: Credentials or provider-issued tokens could be exposed if printed, logged, persisted, or passed through unsafe command lines.

Mitigation: Use Maton OAuth and the operating system credential store where possible; do not print, export, dump, or persist credentials, and use the documented stdin-based fallback only when the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/klaviyo)
- [Maton Homepage](https://maton.ai)
- [Klaviyo API Documentation](https://developers.klaviyo.com)
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview)
- [Klaviyo Developer Portal](https://developers.klaviyo.com/en)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and API-call guidance; does not itself return Klaviyo data without authenticated execution.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
