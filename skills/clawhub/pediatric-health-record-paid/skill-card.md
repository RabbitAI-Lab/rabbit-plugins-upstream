## Description:

Pediatric Health Record is a paid cloud skill that helps legal guardians organize voluntarily provided health details for children ages 0-3 into a structured pediatric health record.

This skill is ready for commercial/non-commercial use.

## Publisher:

[williswu](https://clawhub.ai/user/williswu)

### License/Terms of Use:

MIT-0

## Use Case:

External users who are the child's legal guardian use this skill to turn voluntarily provided infant and toddler health information into a structured record. The skill is for record organization only and is not intended for diagnosis, clinical interpretation, medication advice, or medical decision-making.

### Deployment Geography for Use:

Global, subject to availability of the WeChat payment flow and the merchant endpoint.

## Known Risks and Mitigations:

Risk: The skill handles children's health details and sends them to a named merchant server.

Mitigation: Use only after clear disclosure, legal guardian confirmation, explicit consent, and user comfort with the merchant-server data flow.

Risk: Security evidence flags weak retention and deployment safeguards for health data.

Mitigation: Add explicit cache expiration and deletion behavior, and avoid storing health data in synced or shared folders.

Risk: Payment and merchant credentials are required for operation.

Mitigation: Use managed secrets or strict file permissions for private keys and payment credentials.

Risk: Payment, retry, and refund state handling may affect user trust and service correctness.

Mitigation: Verify payment, retry, and refund behavior before production use, including failure and refund paths.

Risk: Dependency ranges allow future package changes.

Mitigation: Pin reviewed dependency versions before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/williswu/skills/pediatric-health-record-paid)
- [Server-resolved GitHub provenance](https://github.com/williswu/pediatric-health-record-paid)
- [Merchant resource endpoint disclosed by the skill](https://mch.1001058.xyz/api/resource)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown health record and structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a project directory, pediatric template, growth and vaccine checks, and general reminder text based on guardian-provided data after payment.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
