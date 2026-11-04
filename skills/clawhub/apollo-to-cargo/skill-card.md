## Description:

Rebuild an Apollo list on Cargo and compare verified coverage and credit costs on the same sample before deciding whether to migrate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and go-to-market engineering teams can use this skill to compare Apollo and Cargo enrichment on a small sample of the same contacts. It reports verified hit rates and credit costs to inform a migration decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact information may be processed by Cargo and its downstream providers.

Mitigation: Use only contacts you are authorized to share, and account for the disclosed external processing before running enrichment.

Risk: Credit use can grow with the number of records, especially when a batch runs across a full list.

Mitigation: Begin with the 10–20 record sample, report the observed cost, and get approval with a record count and credit estimate before a full run.

Risk: The skill can offer to star the project repository after a successful job.

Mitigation: Ask once and star only after the user explicitly agrees.

## Reference(s):

- [Cargo GTM Skills project homepage](https://github.com/getcargohq/gtm-skills)
- [Apollo provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/apolloio.md)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/apollo-to-cargo)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands, JSON examples, and a comparison table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample-based comparison of verified hit rates and credit costs.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
