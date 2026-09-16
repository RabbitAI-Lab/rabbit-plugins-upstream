## Description:

长期待摊费用摊销台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users run this skill during monthly close, reconciliation, or inventory review to check long-term prepaid expense amortization tables. It recalculates table arithmetic, totals, duplicates, and missing values, and cites source rows for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes an upsell prompt that asks an AI assistant to run an unpinned npx install and begin a paid SkillPay purchase flow.

Mitigation: Run only the local free checker unless you independently trust SkillPay, the npm package, and the paid-skill process; require the human user to confirm any wallet authorization or payment.

Risk: The free release omits five additional amortization checks, so results do not cover every possible table issue.

Mitigation: Treat output as limited to the listed free checks and review withheld or out-of-scope checks separately before relying on the result.

Risk: Incomplete or poorly formatted amortization table input can prevent a reliable conclusion.

Mitigation: Provide the table with recognizable headers and source rows; when input is insufficient, the skill reports what is missing instead of issuing a no-issue conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/long-term-amortization-check-free)
- [SkillPay shelf referenced by the artifact](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by the artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by the artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from a local Node CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally without network use; outputs scoped check results, withheld checks, insufficient-input status, and row-cited findings when available.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
