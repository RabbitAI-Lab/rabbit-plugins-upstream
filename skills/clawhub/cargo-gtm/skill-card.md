## Description:

Cargo GTM helps agents perform B2B go-to-market workflows on Cargo, including account research, contact enrichment and verification, lead scoring, permission-based outreach drafting, CRM sync, and buying-signal monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, RevOps, and GTM teams use this skill to plan and execute compliant B2B prospecting, enrichment, qualification, outreach-preparation, CRM, advertising-audience, and signal-monitoring workflows through Cargo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive prospect and customer data and can interact with live CRM, advertising, LinkedIn, and recurring-workflow surfaces.

Mitigation: Review the skill before installation and use it only with authorized B2B data sources and approved provider, CRM, ads, and LinkedIn connections.

Risk: Actions involving personal contact data, phone numbers, personal email, visitor identification, LinkedIn engagement, recurring workflows, CRM writes, ads, or repository writes can create privacy, compliance, or operational risk.

Mitigation: Require explicit approval for those actions and enforce the documented basis, suppression, relevance, volume, and cost gates before execution.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Acceptable use](references/acceptable-use.md)
- [Cost discipline](references/cost-discipline.md)
- [Contact accuracy](references/contact-accuracy.md)
- [Stage to action map](references/stage-action-map.md)
- [Waterfall strategy](references/waterfall-strategy.md)
- [Output retrieval](references/output-retrieval.md)
- [Prompt library index](references/prompt-library/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with Cargo CLI commands, JSON payloads, TypeScript helper scripts, and structured workflow plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include send-ready outreach variables and workflow instructions, but the skill states that it does not send outreach directly.]

## Skill Version(s):

1.17.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
