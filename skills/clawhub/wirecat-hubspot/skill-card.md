## Description:

Use the HubSpot CLI to query, sync, and manage CRM records, with profile selection, JSON answers, and safeguards for changes and customer data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and CRM operators use the skill to inspect HubSpot deals and related records, track changes, and make requested CRM updates from a terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that the API documentation includes destructive CRM actions and ticket-management features beyond the stated sales CRM scope.

Mitigation: Review whether these capabilities are needed; use --dry-run for writes and check the target records and owner permissions before confirming changes.

Risk: Ticket-management commands may exceed the scope of a sales CRM task.

Mitigation: Confirm the requested task includes ticket work before using those commands, and limit actions to the records needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-hubspot)
- [HubSpot API reference index](references/api.md)
- [HubSpot API basic operations](references/api/api-basic.md)
- [HubSpot API batch operations](references/api/api-batch.md)
- [HubSpot API search operations](references/api/api-search.md)
- [HubSpot API advanced operations](references/api/api-advanced.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Shell commands and JSON responses, with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses include structured records or error details; warnings are written to stderr.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
