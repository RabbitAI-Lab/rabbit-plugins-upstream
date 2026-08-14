## Description:

Return a compact full report for one major-US credit card, covering fees, offer, earnings, redemption, credits, travel benefits, protections, mechanics, eligibility, and strategy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research one exact major U.S. credit-card variant and produce a whole-card report. The report covers fees, welcome offer, earning rates, redemption, credits, travel benefits, protections, account mechanics, eligibility, strategy, fit, similar cards, and confidence notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credit-card offers, fees, eligibility rules, and benefits change frequently, so generated guidance can become stale or incomplete.

Mitigation: Verify important fees, eligibility, benefits, and offer terms on the issuer page before applying or making financial decisions.

## Reference(s):

- [Card Full skill page](https://clawhub.ai/jiahongc/skills/card-full)
- [Publisher profile](https://clawhub.ai/user/jiahongc)
- [Card Identity](../card-identity/SKILL.md)
- [Source Policy](../card-shared/source-policy.yaml)
- [Section Definitions](../card-shared/section-definitions.md)
- [Command Contracts](../card-shared/command-contracts.yaml)
- [Confidence Rules](../card-shared/confidence-rules.md)
- [Normalization Rules](../card-shared/normalization-rules.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with required sections and hidden source YAML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bounded issuer-first research and marks unresolved optional details as unconfirmed.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
