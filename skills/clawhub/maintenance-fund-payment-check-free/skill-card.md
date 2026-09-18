## Description:

维修资金与专项工程付款核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, property management, and owners committee users can use this skill during monthly closing, reconciliation, or inventory checks to recalculate maintenance fund and special project payment tables. It checks table arithmetic, totals, duplicates, missing placeholders, and negative amounts or ratios, while citing source rows for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary flags an optional paid upgrade flow that runs unpinned remote installer code and follows newly installed instructions.

Mitigation: Use the free local checker unless the user independently trusts the package source, reviews the resolved version, and explicitly chooses the payment and installation flow; wallet or payment confirmation should remain user-controlled.

Risk: The free edition reports only its declared local checks and omits several complete-edition checks, so users could overread a narrow result as a full financial or regulatory review.

Mitigation: Treat the output as table-consistency assistance, review the listed checks_not_run and out-of-scope items, and use responsible finance or regulatory review for decisions about maintenance fund use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/maintenance-fund-payment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional complete-edition purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Chinese human-readable text or structured JSON with check scope, findings, summary, omitted checks, and out-of-scope notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a JSON or plain-text table input and can emit JSON with --json.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
