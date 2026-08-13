## Description:

Finance Consumer Guard screens Chinese financial-product marketing and sales text before publication for high-risk consumer-protection phrases and returns risk levels with remediation suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT

## Use Case:

External users, financial institutions, compliance teams, operations teams, and agents use this skill to screen draft financial-product marketing copy, sales scripts, advertisements, website descriptions, and public announcements before publication. It flags high-frequency risky phrases related to principal guarantees, exaggerated returns, weakened risk disclosure, misleading past performance, unqualified sales, and advertising superlatives.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users may treat the lightweight local screening result as legal advice or as a complete compliance audit.

Mitigation: Use the skill as a pre-publication screening aid and route material compliance decisions to qualified legal or compliance reviewers.

Risk: A rules-based scan can miss risky phrasing that depends on context or wording not covered by the current term list.

Mitigation: Review clean results before publication for context, suitability, licensing, and risk-disclosure obligations that the skill does not independently verify.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/finance-consumer-guard)
- [README](README.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a clean or flagged decision, highest risk level, finding count, matched terms, categories, severities, character positions, and remediation suggestions.]

## Skill Version(s):

1.0.0 (source: evidence release metadata, package.json, CHANGELOG released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
