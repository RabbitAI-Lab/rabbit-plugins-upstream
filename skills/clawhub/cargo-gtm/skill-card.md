## Description:

Cargo GTM helps agents perform B2B go-to-market work on Cargo, including account and contact research, licensed enrichment and verification, lead scoring, permission-based outreach drafting, CRM sync, and buying-signal monitoring with consent, suppression, and volume gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue teams and go-to-market operators use this skill to plan and execute Cargo workflows for prospecting, account research, contact enrichment, lead scoring, outreach preparation, CRM updates, signal monitoring, and paid-audience activation. It is intended for B2B professional identities and requires consent basis, suppression filtering, relevance checks, and user approval before paid or high-impact actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke unpinned Cargo npm package installs and uses Cargo or API credentials.

Mitigation: Review the skill before installation, pin and review Cargo npm package versions, avoid global installs as root, and use narrowly scoped Cargo or API tokens.

Risk: The skill can guide high-impact GTM workflows involving personal contact data, CRM or sequencer writes, ad-audience uploads, and recurring runs.

Mitigation: Require explicit user approval before CRM or sequencer writes, ad-audience uploads, recurring plays, or workflows that process personal contact data at scale.

Risk: Improper use could create non-compliant outreach, suppressed-contact handling, or excessive paid data processing.

Mitigation: Apply the skill's basis, suppression, relevance, volume, and cost-approval gates before enrichment, outreach preparation, sequencer handoff, or batch execution.

## Reference(s):

- [Cargo Skills Homepage](https://github.com/getcargohq/cargo-skills)
- [Acceptable Use](references/acceptable-use.md)
- [Cost Discipline](references/cost-discipline.md)
- [Finding Companies and Contacts](guides/finding-companies-and-contacts.md)
- [Enriching and Researching](guides/enriching-and-researching.md)
- [Writing Outreach](guides/writing-outreach.md)
- [Output Retrieval](references/output-retrieval.md)
- [Stage to Action Map](references/stage-action-map.md)
- [Waterfall Strategy](references/waterfall-strategy.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, configuration snippets, and generated files when recipes call for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires @cargo-ai/cli and authenticated Cargo workspace access; many workflows are asynchronous and may return CSV or JSON outputs through Cargo run-output retrieval.]

## Skill Version(s):

2.1.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
