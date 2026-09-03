## Description:

Generates a paid enterprise due-diligence report that combines business registration details with public risk signals for operating abnormality, enforcement, dishonesty, and consumption-restriction checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a paid pre-cooperation or supplier/customer risk check for a specific registered company name, registration number, or unified social credit code. The result is a concise due-diligence report for reference, not a credit report or legal opinion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the queried company name or registration code to Juhe as part of a paid lookup.

Mitigation: Use it only for intentional due-diligence checks on a specific company, after payment and privacy notice requirements are satisfied.

Risk: Reports may display public sensitive business or legal-risk information such as legal representative names, addresses, case numbers, or subject identifiers.

Mitigation: Minimize display and retention, avoid logging full sensitive identifiers, and mask values identified as natural-person identity-card numbers.

Risk: Risk modules return recent-page details and capped report rows rather than complete historical lists.

Mitigation: State that displayed records are partial recent records and direct users to official public channels for complete and current verification.

Risk: A report could be mistaken for legal advice, a credit report, or a cooperation decision.

Mitigation: Frame the output as a reference-only public-risk summary and do not provide deterministic legal or cooperate/do-not-cooperate recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-dd-pro-a2a)
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query)
- [Skill execution specification](artifact/SKILL.md)
- [Output format](artifact/OUT_FORMAT.md)
- [Product scope](artifact/PRODUCT.md)
- [Enterprise registration field reference](artifact/docs/工商主体信息.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown due-diligence report with tables, a risk-light summary, and concise caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one company keyword per paid lookup; report sections must minimize sensitive public-data display, mask recognized identity-card numbers, and avoid legal or cooperation recommendations.]

## Skill Version(s):

1.0.6 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
