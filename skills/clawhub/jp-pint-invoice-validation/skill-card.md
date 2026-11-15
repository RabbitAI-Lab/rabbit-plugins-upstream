## Description:

Validate Japanese JP PINT 1.1.3 UBL Invoice XML against OASIS UBL 2.1 and OpenPeppol rules, with an optional National Tax Agency seller T-number check through JPVerify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT

## Use Case:

Developers and finance or accounting teams use this skill to check whether a Japanese JP PINT e-invoice is valid before sending, accepting, or paying it. They can also request a check of the seller's qualified-invoice T-number in Japan's National Tax Agency registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complete invoice sent to JPVerify may contain sensitive personal or business information.

Mitigation: Before sending it, confirm that transmission is authorized and acceptable; send only data needed for the check and omit unnecessary personal details.

Risk: The security scan was partial, so its assessment is incomplete while referenced material remains unresolved.

Mitigation: Review the referenced material and the skill before installation, especially before sending invoice data to the service.

## Reference(s):

- [JPVerify endpoint reference](references/endpoints.md)
- [JPVerify request examples](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [JPVerify invoice validation endpoint](https://api.jpverify.com/v1/jp/invoices/validate-pint)

## Skill Output:

**Output Type(s):** [JSON, Guidance, API Calls, Shell commands, Code]

**Output Format:** [JSON validation results with Markdown guidance and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Validation uses the exact invoice XML string; registry_enhance optionally requests a seller T-number check. Results distinguish document validity from workflow decision and trust signals.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
