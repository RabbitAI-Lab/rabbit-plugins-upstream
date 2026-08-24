## Description:

Cargo GTM helps agents perform B2B go-to-market work on Cargo, including account and buying-committee research, licensed contact enrichment and verification, lead scoring, permission-based outreach drafting, CRM sync, and buying-signal monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, RevOps, and GTM teams use this skill to move from an ICP or account list to researched, enriched, verified, scored, and sequencer-ready B2B prospect data. Agents use it to choose appropriate Cargo provider playbooks, apply consent and suppression gates, control paid fan-out, and produce compliant outreach drafts or activation handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support B2B prospecting and enrichment workflows that handle professional contact data.

Mitigation: Install only for approved B2B use cases, require lawful-basis, suppression-list, relevance, retention, and data-provider controls, and store downloaded or intermediate prospect data privately until it is deleted.

Risk: Paid fan-out, recurring extractors, CRM or ads writes, phone lookups, and LinkedIn actions can create spend, privacy, or account-action exposure.

Mitigation: Require explicit approval before these actions, sample before full runs, honor provider playbooks, and keep phone lookups limited to qualified leads with explicit user request.

Risk: Outreach drafts could be misused for unsolicited or deceptive bulk messaging.

Mitigation: Use the documented refusal rules for consumer targeting, purchased or scraped lists, suppression evasion, disguised sender identity, auto-dialing, SMS blasts, and undifferentiated fan-out.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Cargo GTM skill page](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Acceptable use](artifact/references/acceptable-use.md)
- [Cost discipline](artifact/references/cost-discipline.md)
- [Contact accuracy](artifact/references/contact-accuracy.md)
- [Stage action map](artifact/references/stage-action-map.md)
- [Output retrieval](artifact/references/output-retrieval.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and local TypeScript QA scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are gated by task-specific phase guides, provider playbooks, approval steps for paid actions, and local QA checks for contact data.]

## Skill Version(s):

1.16.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
