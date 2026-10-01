## Description:

Guides agents in reading and managing Airtable bases, tables, and records through a Maton-authorized connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to query Airtable data and, with explicit approval, create, update, or delete records. They can also configure approved functions and scheduled or cross-app triggers for Airtable actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad Airtable authorization could expose more data than the task requires.

Mitigation: Ask before connecting an account and choose the narrowest available OAuth scopes.

Risk: Record changes or deletions could alter or remove user data.

Mitigation: Start with read-only requests and confirm the exact target and effect before each write or deletion.

Risk: A function or trigger destination may continue sending data after setup.

Mitigation: Confirm each automation and its destination separately; use a third-party host only when the user explicitly approves it.

Risk: A raw API key could expose a long-lived credential.

Mitigation: Prefer the Maton device login; use raw API keys only if the CLI cannot be installed and never include credentials in destinations or output.

## Reference(s):

- [Airtable skill release](https://clawhub.ai/byungkyu/skills/airtable)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Airtable API overview](https://airtable.com/developers/web/api/introduction)
- [Airtable formula reference](https://support.airtable.com/docs/formula-field-reference)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a network connection and an authorized Maton account.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
