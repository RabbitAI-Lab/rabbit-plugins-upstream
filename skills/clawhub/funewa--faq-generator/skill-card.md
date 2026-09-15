## Description:

Generates product-page FAQ suggestions from repeated questions in Amazon reviews and product fields, without providing customer-service replies, legal review, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and marketplace operators use this skill to turn review questions and product-detail signals into FAQ topics and evidence-backed answer guidance for product listings. It checks ARI capabilities, profile data, and cost before running paid analysis after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and sends Amazon ASIN, site, and workflow data to ari.funewa.com.

Mitigation: Install and run it only when this credential use and data sharing are acceptable for the account and products being analyzed.

Risk: Server security evidence flags broader paid ARI operation controls than the FAQ-only description promises.

Mitigation: Review the skill before deployment and confirm paid operations stay limited to the listing/faq workflow with explicit user confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/faq-generator)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [Amazon product FAQ workflow](references/operation-workflow.md)
- [Amazon product FAQ API reference](references/reference.md)
- [ARI service endpoint](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite available review or product evidence, state gaps when evidence is insufficient, and avoid exposing internal task identifiers or command logs unless requested.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
