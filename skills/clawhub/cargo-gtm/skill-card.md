## Description:

Cargo GTM routes agents through Cargo prospecting, enrichment, verification, scoring, outreach, CRM sync, and signal-monitoring workflows with phase guides, recipes, provider playbooks, and QA scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this skill to plan and execute Cargo workflows for finding accounts and contacts, enriching and verifying data, scoring or personalizing outreach, syncing to CRM or sequencer tools, and monitoring buyer signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can process personal contact data and transfer records to connected enrichment or LLM providers.

Mitigation: Require explicit approval before third-party enrichment or LLM transfer, and treat downloaded CSV/JSON contact data as sensitive personal data.

Risk: The skill can guide CRM or sequencer writes, Slack or webhook posts, LinkedIn actions, and other connected-account operations.

Mitigation: Require explicit user approval before write actions, posts, LinkedIn actions, visitor-identification workflows, or workflow deployment.

Risk: Recurring plays can repeatedly spend credits or reprocess the same rows if cadence and gating are wrong.

Mitigation: Use the documented recurring-cost approval gate, state per-run and monthly cost, and monitor created runs after deployment.

Risk: Wrong-person enrichment or stale employment data can lead to inaccurate outreach.

Mitigation: Run the included email, LinkedIn-name, current-role, and contact-accuracy QA scripts before sending data to sequencers or CRMs.

Risk: Paid provider actions, especially phone lookup and broad searches, can create unexpected spend.

Mitigation: Follow the sample, approval, full-run gate; state record counts and credit estimates; receipt every paid action; require explicit user request before phone lookup.

## Reference(s):

- [Cargo GTM on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Finding companies and contacts](guides/finding-companies-and-contacts.md)
- [Enriching and researching](guides/enriching-and-researching.md)
- [Writing outreach](guides/writing-outreach.md)
- [Cost discipline](references/cost-discipline.md)
- [Contact accuracy](references/contact-accuracy.md)
- [Stage to action map](references/stage-action-map.md)
- [Output retrieval](references/output-retrieval.md)
- [Waterfall strategy](references/waterfall-strategy.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and TypeScript QA utilities]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference CSV/JSON outputs from Cargo workflows and local QA scripts.]

## Skill Version(s):

1.10.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
