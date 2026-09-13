## Description:

CallRail API integration with managed OAuth for tracking and analyzing calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to let an agent access authorized CallRail account data, list and analyze calls, manage tracking numbers and tags, and prepare approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Maton as the gateway and package publisher.

Mitigation: Install only when the user trusts Maton and has reviewed the available release evidence and package provenance.

Risk: API-key authentication can expose a long-lived credential through environment variables, logs, shell history, or copied output.

Mitigation: Prefer OAuth, keep any API key out of command lines and persisted files, never print it, and rotate it if it is exposed.

Risk: A broad or ambiguous CallRail connection can expose more accounts, scopes, or records than the task requires.

Mitigation: Connect only the needed CallRail account and scopes, specify the target connection when multiple connections exist, and delete unused connections.

Risk: Write operations and connection creation can change CallRail data or authorization state.

Mitigation: Default to read and list operations, verify identifiers and current state first, and require explicit approval for every POST, PUT, PATCH, DELETE, or new connection.

Risk: Hosted functions, triggers, and destinations can create persistent automation or ongoing data forwarding.

Mitigation: Use user-authored or user-reviewed handlers, prefer deny-all outbound network policy, disclose destination hosts and payload fields, obtain separate approval, and delete unused automations.

Risk: CallRail responses and trigger payloads may include personal, business, or confidential data.

Mitigation: Extract only the fields needed for the task and avoid dumping raw responses or event payloads into logs, files, shared surfaces, or unapproved destinations.

## Reference(s):

- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail Help Center - API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [CallRail Skill on ClawHub](https://clawhub.ai/byungkyu/skills/callrail)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, API request paths, JSON payloads, and approval guidance.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
