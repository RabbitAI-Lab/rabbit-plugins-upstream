## Description:

HubSpot API integration with managed OAuth for CRM contacts, companies, deals, associations, properties, and approved HubSpot-triggered automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM operators use this skill to read, search, create, update, and delete HubSpot CRM records through a user-authorized Maton connection. They can also configure approved hosted functions and triggers for HubSpot-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM writes, deletions, function deployments, triggers, and destinations can change customer data or create persistent automation.

Mitigation: Confirm each write, deletion, deployment, trigger, and destination separately with the user before execution.

Risk: Overbroad OAuth grants can expose more HubSpot APIs than the CRM workflow requires.

Mitigation: Prefer OAuth and select only the HubSpot scopes required for the current task.

Risk: API keys, signing keys, or provider tokens can be exposed through commands, logs, scripts, or destination headers.

Mitigation: Avoid placing secrets directly in commands, logs, scripts, or destination headers; rotate any key that was exposed.

Risk: Installing and using this skill requires trusting the third-party Maton publisher and its managed OAuth gateway.

Mitigation: Verify trust in the Maton publisher before installation and use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/hubspot-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [HubSpot API Overview](https://developers.hubspot.com/docs/api/overview)
- [HubSpot CRM Search Reference](https://developers.hubspot.com/docs/api/crm/search)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated CRM API calls, Maton CLI commands, hosted function snippets, and trigger configuration steps for user review.]

## Skill Version(s):

1.2.6 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
