## Description:

Cargo GTM helps agents perform B2B go-to-market work on Cargo, including account research, contact enrichment and verification, lead scoring, permission-based outreach drafting, CRM sync, signal monitoring, and campaign activation with built-in compliance and cost gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue, operations, and GTM teams use this skill to move from an ICP or account set to qualified prospects, verified B2B contact records, scored leads, send-ready outreach variables, CRM updates, and monitored buying signals. It is intended for authorized Cargo workspaces using licensed providers and documented basis, suppression, relevance, and volume checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: B2B contact enrichment, CRM sync, ads activation, and sequencer handoff can create privacy and compliance obligations for personal data.

Mitigation: Use only authorized Cargo workspaces and licensed providers; confirm lawful basis, suppression lists, vendor approvals, data minimization, and the destination before person-level workflows.

Risk: Broad cold outreach, personal emails, phone lookups, visitor-identification signals, or personality analysis can be misused beyond the skill's intended B2B scope.

Mitigation: Keep the workflow to qualified B2B professional identities, require narrow approved cases for sensitive lookups, and refuse consumer targeting, bulk unsolicited messaging, scraping, and suppressed records.

Risk: Paid provider actions can waste credits or scale incorrect results if run without validation.

Mitigation: Follow the sample, approval, full-run gate; report receipts after paid actions; and use the bundled deterministic QA scripts before CRM, sequencer, or audience handoff.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [ClawHub cargo-gtm skill page](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Acceptable use](references/acceptable-use.md)
- [Cost discipline](references/cost-discipline.md)
- [Contact accuracy](references/contact-accuracy.md)
- [Output retrieval](references/output-retrieval.md)
- [Stage action map](references/stage-action-map.md)
- [Waterfall strategy](references/waterfall-strategy.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands, JSON-oriented CLI output expectations, provider playbooks, recipes, and TypeScript QA script paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Cargo CLI and an authorized Cargo workspace; paid and person-level workflows are gated by sampling, approval, receipts, basis, suppression, relevance, and QA checks.]

## Skill Version(s):

1.13.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
