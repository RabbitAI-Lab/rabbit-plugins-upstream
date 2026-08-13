## Description:

Xborder Ecom Guard screens US/EU-facing cross-border e-commerce product, advertising, livestream, shop, and customer-service text for common compliance-risk statements and returns severity-ranked remediation suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill before publishing US/EU-facing e-commerce content to flag risky wording around reviews, origin, CE claims, customs, safety claims, and advertising claims.

### Deployment Geography for Use:

Global, for content targeting United States and European Union markets.

## Known Risks and Mitigations:

Risk: Users may treat wording-risk findings as legal advice or compliance certification.

Mitigation: Treat outputs as a lightweight screen and verify high-stakes publication decisions against current official rules or counsel.

Risk: Term matching may miss issues or flag wording that is compliant when backed by valid evidence.

Mitigation: Review findings in context, keep supporting documentation for claims, and use deeper compliance review for regulated products or campaigns.

Risk: Input text can contain non-public commercial information such as supplier, customs, or certification details.

Mitigation: Run the skill locally as designed and avoid sharing sensitive source text outside the intended agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/xborder-ecom-guard)
- [Publisher profile](https://clawhub.ai/user/wwumit)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text or JSON with decision, risk level, finding count, matched terms, categories, severities, and remediation suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only wording-risk screen with no network, persistence, or dependencies reported.]

## Skill Version(s):

1.0.0 (source: server release evidence, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
