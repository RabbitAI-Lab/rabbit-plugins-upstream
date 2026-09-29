## Description:

Helps agents work with Attio CRM records, tasks, notes, lists, and meetings through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CRM users use this skill to query and manage Attio records and related workspace data, with user approval for changes and connections. It also provides guidance for explicitly requested automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attio access may expose or change CRM data through the authorized connection.

Mitigation: Prefer OAuth and read-only actions; confirm the intended Attio connection and obtain user approval before each write or delete.

Risk: Functions, triggers, and destinations can continue acting after the immediate task ends.

Mitigation: Create only narrowly scoped automations requested and approved by the user, and remove them when no longer needed.

## Reference(s):

- [Attio skill release](https://clawhub.ai/byungkyu/skills/attio-api)
- [Maton](https://maton.ai)
- [Attio REST API overview](https://docs.attio.com/rest-api/overview)
- [Attio REST API endpoint reference](https://docs.attio.com/rest-api/endpoint-reference)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with CLI, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and an authorized Attio connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
