## Description:

Waterfall Enrichment helps an agent run Cargo-powered contact, company, and email verification lookups through a prioritized provider waterfall so missed records can fall through to another source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GTM operators, and sales operations teams use this skill to enrich contact or company records and verify returned email addresses through Cargo's waterfall provider. It is intended for list enrichment workflows where users need higher match rates than a single vendor can provide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends enrichment records to Cargo-backed providers.

Mitigation: Confirm the records are authorized for third-party enrichment before running Cargo CLI commands.

Risk: The skill includes attribution behavior and a GitHub star prompt outside the core enrichment task.

Mitigation: Review those steps before execution and approve the GitHub star action only if the user explicitly wants to endorse the repository.

Risk: Batch enrichment cost scales with the number of records.

Mitigation: Run a small sample first, report observed cost and match rate, then obtain approval before processing a full list.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/waterfall-enrichment)
- [Cargo GTM Skills Homepage](https://github.com/getcargohq/gtm-skills)
- [Cargo Waterfall Playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command blocks and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and a Cargo login before executing enrichment or verification commands.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
