## Description:

COPPA Guard screens draft copy, privacy-policy text, and app-store descriptions for COPPA-triggering or child-privacy risk terms before publication, then returns risk-ranked findings and remediation suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, product teams, and compliance reviewers use this skill as a lightweight pre-publication guardrail for US-facing children's apps, games, e-commerce, education products, privacy policies, and app-store descriptions. It helps agents flag likely COPPA applicability and common child-privacy issue patterns before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dictionary-based screening can miss nuanced COPPA issues or produce false positives when product context changes the meaning of a term.

Mitigation: Use findings as a pre-publication prompt for qualified legal or compliance review, not as legal advice or a complete COPPA audit.

Risk: A clean result only means the bundled terms did not match the supplied text.

Mitigation: Review the full product data flow, parental consent process, third-party disclosures, and persistent identifier use before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/coppa-guard)
- [Project repository](https://github.com/wwumit/coppa-guard)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or structured JSON findings with risk levels, matched terms, categories, positions, and remediation suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python standard library only; accepts direct text or stdin input.]

## Skill Version(s):

1.0.0 (source: package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
