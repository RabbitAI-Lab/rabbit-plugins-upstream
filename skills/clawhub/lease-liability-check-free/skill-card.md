## Description:

租赁负债摊销表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or review to check lease liability amortization tables for row-level arithmetic, totals, duplicates, blanks, and negative amounts. It reports only findings supported by the provided table and identifies missing required input instead of guessing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes optional purchase and install instructions that ask an agent to run remote payment tooling and follow external guidance.

Mitigation: Do not allow an agent to execute the payment or install block automatically; review the external SkillPay guide, package version, permissions, and any wallet or payment step yourself.

Risk: The free checker explicitly omits several validation checks, including interest-rate tie-out, negative liability detection, depreciation-over-cost detection, rate-range prompts, and lease-term mismatch detection.

Mitigation: Treat results as limited to the listed free checks and review the omitted and out-of-scope checks before relying on the output for financial close or audit decisions.

Risk: The skill makes accounting-oriented findings from user-provided table text and may be incomplete when source material is missing or headers are not recognized.

Mitigation: Provide the full lease liability amortization table with required headers and independently review material findings against source records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lease-liability-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay listing referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, json, analysis, shell commands, guidance]

**Output Format:** [Human-readable text or JSON with checks performed, findings, scope, omitted checks, and summary fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a lease amortization table as JSON text input or pasted plain text with headers]

## Skill Version(s):

1.0.3 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
