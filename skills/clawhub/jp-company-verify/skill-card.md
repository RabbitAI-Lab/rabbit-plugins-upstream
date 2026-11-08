## Description:

Verify Japanese companies against official registries with JPVerify: identify a Japanese company from an English or romanized name, postal code, T-number, LEI or securities code with English output; corporate number (法人番号) lookup by number or company name, active/closed status, registered address, a company pre-check report with risk flags, company profile (capital, employees, website), listing, EDINET filings, Financial Services Agency licences and former names.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

External users can identify Japanese legal entities and check corporate status, registry details, filings, and covered financial registrations. Use the results as a public-registry pre-check when researching a company or preparing for onboarding or payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company identifiers and other supplied search details are sent to an external verification API, and successful paid calls use prepaid credits or an approved x402 payment.

Mitigation: Send only information the user is entitled to process; check the applicable call price and payment authorization before making a paid request.

Risk: A match, no-result, registry pre-check, or licensing lookup may be ambiguous or incomplete and does not establish full KYB/AML clearance or a legal conclusion.

Mitigation: Review the returned evidence and coverage notes, present multiple candidates for the user to choose from, and seek appropriate review for consequential decisions.

Risk: The security assessment is benign with medium confidence, but scan coverage is partial and its evidence is incomplete.

Mitigation: Review the skill and its external API use before installation, as advised by the security assessment.

## Reference(s):

- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [JPVerify](https://www.jpverify.com)
- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Guidance]

**Output Format:** [Structured verification results with explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include multiple candidates, match evidence, source and freshness details, and warnings; users should review ambiguous results.]

## Skill Version(s):

1.0.9 (source: release metadata, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
