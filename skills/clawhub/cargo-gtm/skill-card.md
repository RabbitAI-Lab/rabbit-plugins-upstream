## Description:

Guides B2B go-to-market work in Cargo, from account research and contact verification to lead qualification, permission-based outreach drafts, CRM updates, and buying-signal monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and marketing teams use the skill to research B2B accounts, find and verify professional contacts, score prospects, prepare relevant outreach, and manage approved Cargo workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing professional contact data or uploading ad audiences without an appropriate basis may expose or misuse personal information.

Mitigation: Confirm lawful basis, suppression lists, and recipient relevance before enrichment, outreach preparation, or audience uploads.

Risk: Paid enrichment calls and recurring Cargo workflows may incur unexpected spend.

Mitigation: Review estimated costs and pilot results, approve paid steps, and require explicit approval before scheduling recurring plays.

Risk: CRM writes, ad-audience changes, phone lookups, or sequencer handoffs may affect external systems and contacts.

Mitigation: Verify the active workspace and obtain explicit approval before each consequential write or handoff; review contact-accuracy results first.

Risk: An unpinned CLI dependency can change between installations.

Mitigation: Pin the Cargo CLI version when stricter supply-chain control is required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Project homepage (skill metadata)](https://github.com/getcargohq/cargo-skills)
- [Acceptable-use guidance](references/acceptable-use.md)
- [Cost discipline](references/cost-discipline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance, outreach drafts, and Cargo CLI commands with structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contact-verification checks and approval gates for paid actions and downstream changes]

## Skill Version(s):

2.3.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
