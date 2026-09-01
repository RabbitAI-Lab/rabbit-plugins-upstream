## Description:

Google Analytics provides managed OAuth access through the Maton CLI for GA4 reporting with the Data API and explicit-approval administrative configuration with the Admin API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to connect a Maton-managed Google Analytics account, run GA4 reports, inspect accounts and properties, and make administrative changes only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Google Analytics Admin API can create, update, or delete accounts, properties, and data streams.

Mitigation: Use the Data API for reporting-only tasks, default to read/list calls, and require explicit approval with exact account, property, data stream, payload, and consequence details before any Admin API write.

Risk: A connection or write request could target the wrong Google Analytics account or property when multiple Maton accounts or connections exist.

Mitigation: List and verify accessible resources first, specify the intended connection or profile when needed, and confirm resource identifiers with the user before making changes.

Risk: OAuth tokens or API keys could be exposed if copied, printed, logged, or passed through shell arguments.

Mitigation: Prefer Maton OAuth and the operating system credential store, use `maton whoami` for verification, avoid inspecting stored credentials, and feed fallback API keys through stdin only when the CLI cannot be installed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Analytics Admin API Overview](https://developers.google.com/analytics/devguides/config/admin/v1)
- [Google Analytics Data API Overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Related ClawHub API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON, Code]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, and SDK code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and Google Analytics authorization; defaults to read/list operations and requires confirmation for connection creation and write-capable Admin API calls.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
