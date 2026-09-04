## Description:

Cargo GTM helps agents plan and run B2B go-to-market workflows in Cargo, including account research, contact enrichment and verification, lead scoring, outreach drafting, CRM sync, and buying-signal monitoring with consent, suppression, volume, and cost gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, revenue operations, and GTM teams use this skill to build qualified B2B account and contact lists, enrich and verify professional contact data, score leads, draft permission-based outreach variables, and route results into CRM, sequencer, or audience workflows. Agents use it as an operating guide for Cargo CLI workflows, provider selection, cost approval, and contact-quality review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide workflows that access business contact data and move results into CRM, sequencer, or ad-platform destinations.

Mitigation: Use it only in workspaces where Cargo-connected workflows are allowed to handle that data, and require consent basis, suppression filtering, and per-recipient relevance before outreach or audience activation.

Risk: Paid enrichment providers and recurring runs can create unexpected credit spend.

Mitigation: Require a sample run, exact record count, credit estimate, budget cap, and explicit approval before any large or recurring paid action.

Risk: Contact enrichment can produce stale roles, wrong-person matches, unsafe addresses, or incomplete rows.

Mitigation: Run the bundled contact QA scripts and route rows by their SEND, VERIFY, REVIEW, or REMOVE verdicts before handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Acceptable use](artifact/references/acceptable-use.md)
- [Cost discipline](artifact/references/cost-discipline.md)
- [Contact accuracy](artifact/references/contact-accuracy.md)
- [Output retrieval](artifact/references/output-retrieval.md)
- [Stage action map](artifact/references/stage-action-map.md)
- [Waterfall strategy](artifact/references/waterfall-strategy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, CLI recipes, and structured review or approval messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce send-ready outreach variables, lead scoring guidance, provider action plans, QA verdicts, and cost or approval summaries; the skill itself does not send outreach.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
