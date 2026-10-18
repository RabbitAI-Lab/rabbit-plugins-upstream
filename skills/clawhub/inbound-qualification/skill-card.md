## Description:

Helps developers adapt a website demo form to identify and qualify companies, record inbound contacts, notify sales in Slack, and offer qualified visitors a booking link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market teams use this skill to adapt and deploy an inbound demo-request form that qualifies companies against their criteria, records leads, and routes submissions to sales. An optional, initially disabled research play can tier qualified contacts and write a brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Anonymous form submissions can overwrite shared contact records.

Mitigation: Verify the email before updating authoritative contact fields, or restrict anonymous updates to append-only submission fields.

Risk: Unescaped personal data in Slack notifications can create misleading or unsafe messages.

Mitigation: Escape or render form fields as plain text, limit message lengths, and validate submitted page URLs.

Risk: Collected lead data may be shared with enrichment, Slack, and optional research services without adequate notice.

Mitigation: Confirm the privacy notice covers company enrichment, Slack sharing, model storage, retention, and optional research before deployment.

## Reference(s):

- [Form integration guide](references/form.md)
- [Contact and account data guide](references/data.md)
- [Project homepage (release metadata)](https://github.com/getcargohq/gtm-skills)
- [ClawHub skill listing](https://clawhub.ai/cargo-ai/skills/inbound-qualification)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with TypeScript examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment checks and optional lead-research setup.]

## Skill Version(s):

0.2.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
