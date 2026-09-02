## Description:

Cargo GTM helps agents plan and carry out B2B go-to-market workflows on Cargo, including account research, contact enrichment and verification, lead scoring, outreach drafting, CRM sync, signal monitoring, and audience activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and go-to-market teams use this skill to move from an ICP or account list to researched companies, verified B2B contacts, scored leads, send-ready outreach, CRM updates, and monitored buying signals. It is intended for authorized B2B workflows with suppression, relevance, volume, and approval gates around personal data and external writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can move personal lead data into CRMs, sequencers, ad platforms, LinkedIn actions, webhooks, and recurring workflows.

Mitigation: Require a preview that shows destination, fields, record count, and explicit approval before any write, live external side effect, or recurring run.

Risk: B2B enrichment and outreach workflows can become unauthorized, overbroad, or expose unnecessary personal or confidential fields to providers.

Mitigation: Use only authorized B2B data, enforce basis, suppression, and relevance checks, avoid consumer-social scraping, and minimize personal or confidential fields sent to LLM and enrichment providers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Finding companies and contacts](guides/finding-companies-and-contacts.md)
- [Enriching and researching](guides/enriching-and-researching.md)
- [Writing outreach](guides/writing-outreach.md)
- [Acceptable use](references/acceptable-use.md)
- [Cost discipline](references/cost-discipline.md)
- [Waterfall strategy](references/waterfall-strategy.md)
- [Output retrieval](references/output-retrieval.md)
- [Contact accuracy](references/contact-accuracy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON-oriented CLI commands, configuration snippets, and structured decision steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cost estimates, approval gates, sample-result reviews, and operational receipts for Cargo actions.]

## Skill Version(s):

1.19.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
