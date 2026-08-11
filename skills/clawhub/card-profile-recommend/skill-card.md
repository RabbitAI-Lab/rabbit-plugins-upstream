## Description:

Analyzes a multi-card portfolio, grades current cards, and recommends 2-3 next personal cards with signup-bonus strategy and issuer-rule checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to audit an existing credit-card wallet, identify portfolio gaps, and choose a short sequence of next personal-card applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit-card recommendations can affect application timing, fees, eligibility, rewards value, and credit impact.

Mitigation: Use the output for planning and verify annual fees, welcome offers, eligibility rules, and credit impact with the issuer or a qualified advisor before applying.

Risk: Issuer rules and offers may be partially unknown or change after the skill researches them.

Mitigation: Review the confidence notes and confirm issuer rules and offer terms directly with current issuer sources before acting.

Risk: Sensitive personal or financial identifiers could be unnecessary for a wallet audit.

Mitigation: Provide card names and opening dates when needed, but do not provide login credentials, Social Security numbers, or full account details unless a separate trusted workflow explicitly requires them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiahongc/skills/card-profile-recommend)
- [Publisher profile](https://clawhub.ai/user/jiahongc)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown portfolio audit with card grades, earning map, recommendations, signup-bonus strategy, issuer-rule checks, and confidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code or persistent data output; sources are kept in hidden YAML by the skill contract.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
