## Description:

Helps teams add a website demo form that qualifies work-email submissions, records accounts and contacts, notifies sales in Slack, and optionally researches qualified leads after the visitor receives a response.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, sales-development, and GTM engineering teams use this skill to adapt a Cargo-hosted demo form that qualifies inbound requests, records leads, and routes responses and notifications. An optional, initially disabled research play adds a tier and brief for qualified contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public submissions can alter existing sales records without verifying email ownership.

Mitigation: Require email verification or stage public submissions separately before updating existing contacts.

Risk: Visitor-provided personal content is posted to Slack without sufficient safeguards.

Mitigation: Send visitor fields as escaped plain text, minimize personal information, and restrict the destination channel.

Risk: Lead data is stored, shared, enriched, and may be synced to a CRM; optional research adds further processing.

Mitigation: Review the privacy notice for these uses and keep the research play disabled until tested with a real pilot contact.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cargo-ai/skills/inbound-qualification)
- [Publisher-provided project homepage](https://github.com/getcargohq/gtm-skills)
- [Form setup and privacy guidance](references/form.md)
- [Shared data models and CRM mapping](references/data.md)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance and TypeScript source files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a public form, lead-qualification workflow, and an optional research play that ships disabled.]

## Skill Version(s):

0.2.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
