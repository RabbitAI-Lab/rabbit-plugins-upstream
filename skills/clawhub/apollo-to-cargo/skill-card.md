## Description:

Rebuild an Apollo list on Cargo and compare the two side by side before migrating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External RevOps and GTM engineering teams use this skill to compare Apollo and Cargo enrichment on a 10–20-record sample, measure coverage and cost, and decide whether to migrate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may record session attribution in Cargo without asking.

Mitigation: Review or remove the automatic attribution command before use; run it only with the user's agreement.

Risk: Contact data may be sent to Cargo and downstream enrichment providers.

Mitigation: Use only contacts authorized for processing by Cargo and the downstream providers.

Risk: Enrichment costs scale with the number of records and selected options.

Mitigation: Start with 10–20 records, report the record count and estimated cost, and get approval before any full-list run.

Risk: The optional broader Cargo pack has separate behavior and may be unreviewed.

Mitigation: Review it separately and prefer reviewed, pinned versions; only star a repository after explicit agreement.

## Reference(s):

- [Apollo provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/apolloio.md)
- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/apollo-to-cargo)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON snippets]

**Output Format:** [Markdown with shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample-first recommendations and cost comparisons based on the supplied Apollo list.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
