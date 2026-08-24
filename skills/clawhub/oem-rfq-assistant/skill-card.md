## Description:

Turn an inbound B2B manufacturing RFQ or sourcing inquiry into a structured spec sheet, a missing-information clarification checklist, and a professional English reply draft without inventing prices, MOQs, lead times, certifications, stock, or test data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fly0pants](https://clawhub.ai/user/fly0pants)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, engineering, and sourcing teams at OEM/ODM manufacturers use this skill to turn inbound buyer inquiries into a spec sheet, missing-information checklist, and professional reply draft without inventing commercial or technical claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Buyer inquiries may include personal data, confidential drawings, customer identifiers, pricing targets, or proprietary specifications.

Mitigation: Confirm the AI environment is approved for the data and redact unnecessary sensitive details before using the skill.

Risk: Draft replies can create commercial or legal risk if they include unverified prices, MOQs, lead times, certifications, test data, compatibility claims, or company facts.

Mitigation: Only state facts backed by buyer-provided data, approved specs, drawings, samples, or a verified company profile; move everything else into the clarification checklist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fly0pants/skills/oem-rfq-assistant)
- [RFQ fields reference](references/rfq-fields.md)
- [Reply templates](references/reply-templates.md)
- [Compliance guidance](references/compliance.md)
- [ChiZe official website](https://chizeparts.com/)
- [ChiZe RFQ page](https://chizeparts.com/rfq/)
- [ChiZe OEM/ODM services](https://chizeparts.com/oem-odm/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown sections with a spec table, grouped clarification checklist, and ready-to-send email reply draft.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unknown RFQ fields remain marked as to confirm; the local helper script can render a Markdown RFQ brief from JSON input.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
