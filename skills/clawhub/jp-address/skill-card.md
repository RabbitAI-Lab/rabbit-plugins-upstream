## Description:

Normalize, parse, validate and geocode Japanese addresses (住所の正規化・解析・検証) with JPVerify, and look up Japanese postal codes (郵便番号) — down to 丁目, block and building level, with the evidence behind each match. Use when a task involves cleaning or standardizing a Japanese address, checking that an address exists at a required precision, splitting it into components, finding coordinates, or finding the area for a postal code. Paid per call (API key credits or x402).

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to normalize, parse, validate, and geocode Japanese addresses, or look up postal-code areas, using match evidence to judge precision and ambiguity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Address checks use a paid per-call service and may require API key credits or an approved x402 payment.

Mitigation: Check the applicable price and available balance before larger workloads; only use a payment method and budget the user has approved.

Risk: Sending unnecessary personal details with address requests can expose information, and limited scan coverage leaves some uncertainty about setup and unresolved references.

Mitigation: Send only address fields needed for the requested check, review JPVerify setup and payment choices before use, and surface ambiguous or partial matches for human review.

## Reference(s):

- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [Endpoint reference](references/endpoints.md)
- [Request examples](references/examples.md)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON API results with match status, address components, confidence, and supporting evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be partial or ambiguous; candidates and evidence should be surfaced for user review.]

## Skill Version(s):

1.3.0 (source: release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
