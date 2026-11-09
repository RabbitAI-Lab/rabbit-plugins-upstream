## Description:

Checks Japanese qualified-invoice T-numbers against the National Tax Agency registry, compares invoice issuer details and registration dates, and matches invoices to supplier master data through JPVerify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Accounts payable and finance teams use this skill to verify Japanese qualified-invoice registrations, compare invoice issuer details and registration dates with registry records, and match invoices to supplier master data.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Invoice-related fields are sent to JPVerify, an external service.

Mitigation: Send only the fields needed for the check and only data the user is authorized to process; avoid unrelated personal details.

Risk: Checks may use paid API credits or x402 payments.

Mitigation: Check the account balance before a large batch and confirm the total cost and budget before making paid batch calls.

Risk: The security scan was partial because some local references were unresolved.

Mitigation: Review the referenced skill files before installation; treat the benign verdict as limited rather than a guarantee of safety.

## Reference(s):

- [JPVerify](https://www.jpverify.com)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [Endpoints reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Natural-language verification summary based on registry responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize registration status, issuer comparisons, and date checks for one or more supplied records.]

## Skill Version(s):

1.2.1 (source: release evidence, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
