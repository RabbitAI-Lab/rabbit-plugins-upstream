## Description:

Verify Japanese companies against official registries with JPVerify: corporate number (法人番号) lookup by number or company name, active/closed status, registered address, a company pre-check report with risk flags, EDINET filings, and Financial Services Agency licence checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT

## Use Case:

Business users and analysts use this skill to confirm a Japanese company's corporate number, registered identity and status, review a registry-based pre-check, retrieve EDINET filing metadata, or check for records in covered FSA registration datasets before onboarding or payment.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Company queries are sent to an external paid API and successful calls may incur charges.

Mitigation: Confirm that sharing the query is appropriate, review per-call pricing, and use an API key or x402 wallet only within an approved budget.

Risk: Registry and covered licensing results are pre-checks and may be ambiguous, incomplete, or insufficient for a consequential decision.

Mitigation: Review the source evidence and freshness, ask the user to resolve multiple matches, and obtain appropriate human or legal review when needed.

## Reference(s):

- [JPVerify](https://www.jpverify.com)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [endpoints.md](artifact/references/endpoints.md)
- [examples.md](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured company and registry results with concise natural-language explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include corporate identity and status, match evidence, risk flags, filing metadata, or coverage-aware registration results.]

## Skill Version(s):

1.0.1 (source: release metadata, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
