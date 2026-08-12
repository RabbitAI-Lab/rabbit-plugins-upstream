## Description:

Shop Ad Guard checks ecommerce product titles, detail pages, live-shopping scripts, and promotion copy before publication for high-frequency advertising compliance terms and returns risk-ranked findings with suggested edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, livestream teams, and agent builders use this skill as a pre-publication advertising copy screen for Chinese ecommerce scenarios. It flags high-frequency risky terms, assigns high/medium/low severity, and gives revision guidance before copy is published.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Keyword-based checks may miss context-specific legal issues or produce false positives for terms whose compliance depends on surrounding copy.

Mitigation: Use the output as an auxiliary pre-publication screen, review flagged and clean results manually, and consult qualified counsel for high-stakes or ambiguous advertising claims.

Risk: Users may mistake the tool's findings for legal advice or a complete regulatory audit.

Mitigation: Present results as compliance guidance only and require human review before publishing or making legal compliance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/shop-ad-guard)
- [README](README.md)
- [Skill documentation](SKILL.md)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Plain text or structured JSON detection report with decision, risk level, finding count, matched terms, categories, severities, positions, and suggested edits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally against a built-in term list; no network, persistence, credential, or destructive behavior is evident in the authoritative security evidence.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, CHANGELOG released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
