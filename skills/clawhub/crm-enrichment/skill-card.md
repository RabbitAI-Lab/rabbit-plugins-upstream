## Description:

Backfills empty CRM record fields for people, companies, funding, and email data so routing, scoring, and territory assignment can rely on fewer blanks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, revenue operations, and CRM administrators use this skill to enrich existing CRM records from identifiers already present in those records. It is intended for sampled, cost-aware enrichment before approved larger batch runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a GitHub star request that is unrelated to CRM enrichment and would use the user's GitHub account to endorse the publisher's repository.

Mitigation: Decline or remove the star step unless the user explicitly wants that endorsement; do not treat missing or unauthenticated GitHub CLI access as a task to fix.

Risk: Running enrichment against real CRM data can expose records to the Cargo service and may fill or overwrite business-critical fields.

Mitigation: Confirm the Cargo CLI install source, account, target fields, and blank-only overwrite rule before executing against production CRM data.

Risk: Batch enrichment cost scales with record count and can become expensive on large CRM segments.

Mitigation: Run a 10-20 record sample first, report observed cost and hit rate, then obtain explicit approval with the full record count and credit estimate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/crm-enrichment)
- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo enrichCrm provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/enrichCrm.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and a Cargo account; batch enrichment can consume per-record credits.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
