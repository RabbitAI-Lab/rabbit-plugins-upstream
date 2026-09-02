## Description:

Backfills empty fields on CRM records so routing, scoring, and territory assignment can use better person, company, funding, and email data through Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, revenue operations, and CRM administrators use this skill to enrich existing CRM records that are missing fields needed for routing, scoring, territory assignment, and account prioritization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM enrichment sends relevant CRM identifiers to Cargo and may process paid batches.

Mitigation: Confirm the data sharing posture, sample 10-20 records first, report observed cost and hit rate, and require explicit approval before any full-list run.

Risk: The skill includes session-attribution behavior that records usage metadata with Cargo.

Mitigation: Review the attribution step before installation and skip it when extra usage metadata should not be recorded.

Risk: The skill includes an optional GitHub repository star request that would act through the user's GitHub account.

Mitigation: Only perform the star action after the user explicitly approves it, and skip it when GitHub account activity is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/crm-enrichment)
- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Cargo enrichCrm provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/enrichCrm.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CLI-oriented enrichment guidance and approval checkpoints; enrichment results are returned by Cargo CLI batch actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
