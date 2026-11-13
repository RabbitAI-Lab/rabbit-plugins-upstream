## Description:

Verify Japanese companies and resolve company identifiers against public registries through JPVerify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT

## Use Case:

Employees and developers use this skill to identify or verify Japanese companies and review public-registry evidence before onboarding or payment. It can also retrieve EDINET filing metadata and check covered FSA registration datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company information is sent to an external API, and successful requests incur per-call charges.

Mitigation: Review the provider and the information being submitted; send only necessary data you are authorized to process, and check costs or an approved payment budget before calls.

Risk: A registry pre-check can have incomplete coverage or ambiguous matches and is not full KYB or a legal determination.

Mitigation: Review returned evidence and source dates, ask the user to resolve multiple candidates, and seek qualified review for consequential decisions.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Request examples](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 payment documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured company lookup results with concise textual interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include source and match information when available; the skill sends fields rather than files.]

## Skill Version(s):

1.3.0 (source: release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
