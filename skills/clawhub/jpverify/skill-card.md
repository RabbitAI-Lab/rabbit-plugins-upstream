## Description:

Routes agents to JPVerify checks for Japanese company and invoice verification, address validation, supplier checks, and JP PINT e-invoice validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT

## Use Case:

External users and business operations agents use this skill to choose the appropriate JPVerify endpoint for Japanese company, invoice issuer, supplier, address, or e-invoice checks. It routes requests and explains the evidence returned by each check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags examples for filings and regulatory-status checks beyond the stated verification purpose.

Mitigation: Confirm that these checks are needed for the user's task before selecting those endpoints.

Risk: Sending invoice contents to JPVerify may disclose sensitive business information to an external service.

Mitigation: Send only the fields needed for the check, and obtain the user's confirmation before uploading a complete invoice or XML document.

## Reference(s):

- [Endpoint guide](references/endpoints.md)
- [Request examples](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured API results with concise text summaries and endpoint guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and evidence vary by endpoint.]

## Skill Version(s):

1.3.0 (source: evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
