## Description:

cargo-gtm helps agents plan and execute compliant B2B go-to-market workflows in Cargo, including account research, contact enrichment and verification, lead scoring, outreach drafting, CRM sync, and signal monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue teams, GTM operators, and developers use this skill to build and qualify B2B account or contact lists, enrich records from licensed providers, draft send-ready outreach, and coordinate CRM or audience handoffs. The skill is intended for workflows with consent, suppression, volume, cost, and human-review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: B2B workflows may process sensitive sales data, including professional contact records, personal emails or phones, CRM records, ads audiences, LinkedIn actions, sequencer handoffs, or recurring plays without enough review.

Mitigation: Before running it, confirm consent or legitimate-interest basis, suppression fields, approved providers and vendor use, a policy for personal emails and phones, and explicit review before CRM, ads, LinkedIn, sequencer, or recurring-play actions.

Risk: Paid provider fan-out can create cost surprises or low-quality contact data at scale.

Mitigation: Run a small sample first, ask for approval before full enrollment, enforce volume and credit caps, provide receipts after paid actions, and use the bundled contact-accuracy scripts before acting on returned contacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-gtm)
- [Cargo publisher profile](https://clawhub.ai/user/cargo-ai)
- [OpenClaw metadata homepage](https://github.com/getcargohq/cargo-skills)
- [Acceptable use](references/acceptable-use.md)
- [Cost discipline](references/cost-discipline.md)
- [Contact accuracy](references/contact-accuracy.md)
- [Output retrieval](references/output-retrieval.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON payload examples, and TypeScript helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires @cargo-ai/cli; paid provider calls are gated by sampling, approval, consent, suppression, and cost controls.]

## Skill Version(s):

1.15.0 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
