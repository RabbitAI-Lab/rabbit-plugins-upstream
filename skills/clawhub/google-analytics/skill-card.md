## Description:

Google Analytics API integration with managed OAuth for read-only reporting through the Data API and explicitly confirmed administrative account, property, and data stream changes through the Admin API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analytics operators use this skill to connect an agent to Google Analytics through Maton OAuth, run GA4 reports, inspect accounts and properties, and perform approved Admin API changes when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin API access can create, update, or delete Google Analytics accounts, properties, and data streams.

Mitigation: Prefer the read-only Data API for reporting, authorize Admin API access only when the task requires it, verify the exact target resource, and require explicit user approval before every write operation.

Risk: OAuth or API-key credentials could be exposed if printed, persisted, or passed through unsafe shell commands.

Mitigation: Use Maton's OAuth flow and operating-system credential storage where possible; never print, log, persist, or transmit credentials outside the documented Maton API flow.

Risk: Multiple Google Analytics or Maton connections can make the target account ambiguous.

Mitigation: List and confirm the intended connection, property, stream, or profile before acting, and pin requests to the selected connection when ambiguity exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-analytics)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Google Analytics Admin API Overview](https://developers.google.com/analytics/devguides/config/admin/v1)
- [Google Analytics Data API Overview](https://developers.google.com/analytics/devguides/reporting/data/v1)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Google Analytics API request paths, request payloads, report queries, connection guidance, and approval prompts for write-capable Admin API operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
