## Description:

Routes agents to JPVerify services for Japanese company, invoice, supplier, document OCR, address, and JP PINT checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use the skill to choose JPVerify calls for Japanese company and invoice checks, supplier pre-checks, document OCR, address validation, and JP PINT invoice validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted business documents or other data may be sent to JPVerify.

Mitigation: Send only data the user is authorized to share, and consider whether the service's data handling is acceptable before processing it.

Risk: The security review was partial because six local references were unresolved.

Mitigation: Review the referenced material and any linked behavior before installing or relying on the skill.

## Reference(s):

- [JPVerify endpoint reference](references/endpoints.md)
- [JPVerify request examples](references/examples.md)
- [API key documentation](https://api.jpverify.com/docs/api-key)
- [x402 payment documentation](https://api.jpverify.com/docs/x402)
- [JPVerify ClawHub release](https://clawhub.ai/japanverify/skills/jpverify)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands, Code]

**Output Format:** [Structured API response data and concise text guidance, with optional curl or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include registry evidence, OCR fields, validation results, match status, and review signals.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata; artifact/SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
