## Description:

Audit a multi-card wallet for overlap, gaps, and total annual cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to audit a set of credit cards they already hold, compare annual fees, earning coverage, benefits, credits, overlap, and gaps, and understand where their wallet may be redundant or incomplete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill researches current credit-card terms, which can change and may affect financial decisions.

Mitigation: Verify important fee, credit, earning, and benefit details against issuer sources before acting on the audit.

Risk: Users may provide sensitive financial information beyond what the skill requires.

Mitigation: Provide only card names; do not provide card numbers, account logins, statements, or other sensitive personal financial data.

Risk: The artifact references shared policy and normalization files outside this release artifact.

Mitigation: Review the installed shared policy, confidence, normalization, and command-contract files before relying on the skill in production.

## Reference(s):

- [Card Wallet ClawHub page](https://clawhub.ai/jiahongc/skills/card-wallet)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown wallet audit with annual cost, earning map, credits stack, overlap, gaps, and confidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sources are intended to remain in hidden YAML according to the skill artifact.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
