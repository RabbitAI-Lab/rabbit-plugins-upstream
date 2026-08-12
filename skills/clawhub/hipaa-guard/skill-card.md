## Description:

HIPAA Guard screens pre-publication healthcare product copy, privacy-policy text, and product descriptions for common HIPAA-triggering or medical-privacy-risk phrases, then returns risk-ranked findings and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and compliance reviewers use this skill to check U.S.-market healthcare SaaS, telehealth, health-app, and patient-portal text before release. It helps identify common PHI, BAA, encryption, third-party disclosure, breach-notification, and patient-access wording risks for human review.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Keyword-based screening can miss nuanced HIPAA issues or flag text that is acceptable in context.

Mitigation: Use findings as advisory pre-release review signals and route material compliance decisions to qualified legal or compliance reviewers.

Risk: The skill may be mistaken for legal advice or proof of HIPAA compliance.

Mitigation: Present outputs as guidance only and require independent review for high-impact healthcare privacy decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/hipaa-guard)
- [Publisher profile](https://clawhub.ai/user/wwumit)

## Skill Output:

**Output Type(s):** [text, json, guidance, shell commands]

**Output Format:** [Plain text or JSON findings with risk level, matched terms, categories, locations, and remediation suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided text and does not persist input or require network access.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, and CHANGELOG released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
