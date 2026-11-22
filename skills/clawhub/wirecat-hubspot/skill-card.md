## Description:

Use the HubSpot CLI to read and update a HubSpot account's CRM, sync deal data to a local store, and review changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and account owners use this skill to inspect HubSpot CRM records, sync deal data for offline review, and manage CRM updates through the hubspot CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or permanently delete CRM records, associations, or tickets; the security review noted destructive CRM and ticket operations.

Mitigation: Review targets and permissions before changes, use --dry-run where available, and provide only the scopes needed for the task.

Risk: The security scan had partial coverage (83.3%) and some local references were unresolved, so parts of the skill were not fully evaluated.

Mitigation: Review the supplied release and bundled API references before use, and start with read-only access when writes are unnecessary.

## Reference(s):

- [HubSpot API overview](references/api.md)
- [HubSpot API: Basic operations](references/api/api-basic.md)
- [HubSpot API: Batch operations](references/api/api-batch.md)
- [HubSpot API: Search operations](references/api/api-search.md)
- [HubSpot API: Advanced operations](references/api/api-advanced.md)
- [HubSpot CLI skill release](https://clawhub.ai/wirecat/skills/wirecat-hubspot)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [HubSpot CLI commands with JSON responses and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON results and available actions depend on the account's permissions and configured scopes.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
